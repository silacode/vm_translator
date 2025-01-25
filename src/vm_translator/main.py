"""Main entry point for the Hack vm-translator."""

from __future__ import annotations

import argparse
import sys
import uuid
from enum import IntEnum, StrEnum, auto
from pathlib import Path
from typing import TYPE_CHECKING, Literal, Optional, Type

from typing_extensions import Self

if TYPE_CHECKING:
    from io import TextIOWrapper
    from types import TracebackType

ARGUMENT_NUMBER = 2
ERROR_MSG = "No input file specified. Usage: python main.py <filename>"

# ARITHMETIC_DICT = ["add", "sub", "neg", "eq", "gt", "lt", "and", "or", "not"]

ARITHMETIC_COMMANDS = frozenset({"add", "sub", "neg", "eq", "gt", "lt", "and", "or", "not"})


# class Commands(StrEnum):
#     PUSH = "push"
#     POP = "pop"
#     LABEL = "label"
#     GOTO = "goto"
#     IF = "if-goto"
#     FUNCTION = "function"
#     RETURN = "return"
#     CALL = "call"


class CommandType(StrEnum):
    """Command type enum."""

    C_ARITHMETIC = auto()
    C_PUSH = auto()
    C_POP = auto()
    C_LABEL = auto()
    C_GOTO = auto()
    C_IF = auto()
    C_FUNCTION = auto()
    C_RETURN = auto()
    C_CALL = auto()


PUSH_or_POP = Literal[CommandType.C_PUSH, CommandType.C_POP]


# Direct mapping dictionary for O(1) lookups
COMMAND_TYPE_MAP = {
    "push": CommandType.C_PUSH,
    "pop": CommandType.C_POP,
    "label": CommandType.C_LABEL,
    "goto": CommandType.C_GOTO,
    "if-goto": CommandType.C_IF,
    "function": CommandType.C_FUNCTION,
    "return": CommandType.C_RETURN,
    "call": CommandType.C_CALL,
}

BASE_MEMORY_SEGMENT = frozenset({"local", "argument", "this", "that"})
SEGMENT_MAP = {
    "local": "LCL",
    "argument": "ARG",
    "this": "THIS",
    "that": "THAT",
    "constant": "CONSTANT",
    "static": "static",
    "pointer": "pointer",
    "temp": "5",
}

ARITHMETIC_VM_ASM_MAP = {
    "add": """
        @SP
        AM=M-1
        D=M
        A=A-1
        M=D+M""",
    "sub": """
        @SP
        AM=M-1
        D=M
        A=A-1
        M=M-D""",
    "neg": """
        @SP
        A=M-1
        M=-M""",
    "eq": """
        @SP
        AM=M-1
        D=M
        A=A-1
        D=M-D
        @JUMP_UQ
        D;JEQ
        @SP
        A=M-1
        M=0
        @CONTINUE_UQ
        0;JMP
    (JUMP_UQ)
        @SP
        A=M-1
        M=-1
    (CONTINUE_UQ)""",
    "gt": """
        @SP
        AM=M-1
        D=M
        A=A-1
        D=M-D
        @JUMP_UQ
        D;JGT
        @SP
        A=M-1
        M=0
        @CONTINUE_UQ
        0;JMP
    (JUMP_UQ)
        @SP
        A=M-1
        M=-1
    (CONTINUE_UQ)""",
    "lt": """
        @SP
        AM=M-1
        D=M
        A=A-1
        D=M-D
        @JUMP_UQ
        D;JLT
        @SP
        A=M-1
        M=0
        @CONTINUE_UQ
        0;JMP
    (JUMP_UQ)
        @SP
        A=M-1
        M=-1
    (CONTINUE_UQ)
        """,
    "and": """
        @SP
        AM=M-1
        D=M
        A=A-1
        M=D&M
        """,
    "or": """
        @SP
        AM=M-1
        D=M
        A=A-1
        M=D|M
        """,
    "not": """
        @SP
        A=M-1
        M=!M
        """,
}

PUSH_CMD = """
        @SP
        A=M
        M=D
        @SP
        M=M+1
        """

POP_CMD = """
        @SP
        AM=M-1
        D=M
        """

INITIAL_CODE = """
        @256
        D=A
        @SP
        M=D
        """
# Add initial sys.init fn call

COUNTER = 0


#  @2048
#         D=A
#         @LCL
#         M=D

#         @4096
#         D=A
#         @ARG
#         M=D

#         @8192
#         D=A
#         @THIS
#         M=D

#         @10000
#         D=A
#         @THAT
#         M=D


class Parser:
    """A context manager Parser class.

    It manages file handling and parses the vm code.
    """

    def __init__(self, filename: str) -> None:
        """Parser Constructor."""
        self.__filename = Path(filename)
        self.__file: TextIOWrapper | None = None
        self.__line_index = 0
        self.__total_lines = 0
        self.has_more_lines = True
        self.current_command: str | None = None

    def __enter__(self) -> Self:
        """Context manager enter method."""

        self.__file = self.__filename.open("r", encoding="utf-8")  # TODO - add validation for .vm extension
        self.__total_lines = len(self.__file.readlines())
        self.__file.seek(0)
        self.has_more_lines = bool(self.__total_lines)
        return self

    def __exit__(
        self, _type: Optional[Type[BaseException]], _value: Optional[BaseException], _traceback: Optional[TracebackType]
    ) -> None:
        """Context manager exit method."""
        if self.__file:
            self.__file.close()

    def advance(self) -> None:
        """Read next line."""
        if not self.has_more_lines:
            return
        self.current_command = self.__file.readline().strip()
        self.__line_index += 1
        if self.__line_index > self.__total_lines:
            self.has_more_lines = False

    def command_type(self, command: str) -> CommandType | None:
        """Determine the command type from a given VM command string.

        Args:
            command: The VM command string to parse
        Returns:
            CommandType enum value or None if invalid command
        """
        if command in ARITHMETIC_COMMANDS:
            return CommandType.C_ARITHMETIC
        return COMMAND_TYPE_MAP.get(command)

    # Should not called if current command ic C_RETURN
    def arg1(self) -> str:
        """Get first arg."""
        return self.current_command.split(" ")[0]

    # should be called only if the current command type is C_PUSH,C_POP,C_FUNCTION,C_CALL
    def arg2(self) -> str:
        """Get second arg."""
        return self.current_command.split(" ")[1]

    def arg3(self) -> str:
        """Get third arg."""
        return self.current_command.split(" ")[2]


class CodeWriter:
    """Context manager code writer class."""

    def __init__(self, filename: str) -> None:
        """CodeWriter Constructor."""
        self.__filename = Path(filename)
        self.source_filename: str = None
        self.__output_file: TextIOWrapper | None = None

    def __enter__(self) -> Self:
        """CodeWriter context enter method."""
        self.__output_file = Path.open(f"{self.__filename.stem}.asm", "w")
        self.__output_file.write(INITIAL_CODE)
        self.write_call("Sys.init", 0)
        return self

    def set_source_filename(self, name: str) -> None:
        """Set filename."""
        self.ource_filename = name

    def __exit__(
        self, _type: Optional[Type[BaseException]], _value: Optional[BaseException], _traceback: Optional[TracebackType]
    ) -> None:
        """CodeWriter Context exit method."""
        if self.__output_file:
            self.__output_file.close()

    def writer_arithmetic(self, command: str) -> None:
        """Translates arithmetic code to assembly."""
        jump_id = str(uuid.uuid1()).replace("-", "")
        continue_id = str(uuid.uuid4()).replace("-", "")
        asm = ARITHMETIC_VM_ASM_MAP.get(command)
        asm = asm.replace("JUMP_UQ", f"JUMP{jump_id}")
        asm = asm.replace("CONTINUE_UQ", f"CONTINUE{continue_id}")
        self.__output_file.write(f"\n//{command}")
        self.__output_file.write(asm)

    def write_push_pop(
        self,
        command: PUSH_or_POP,
        segment: str,
        index: int,
    ) -> None:
        """Writes push and pop command."""
        # command push/pop, segment string, index int

        asm_code = ""
        index_cmd = f"""
                @{index}
                D=A
                """
        if COMMAND_TYPE_MAP.get(command) == CommandType.C_PUSH:
            # LCL,ARG,THIS,THAT, TEMP
            if segment.strip() in BASE_MEMORY_SEGMENT:
                segment_code = SEGMENT_MAP.get(segment)
                asm_code = f"""
                    {index_cmd}
                    @{segment_code}
                    A=D+M
                    D=M
                    {PUSH_CMD}
                    """
            elif segment == "temp":
                asm_code = f"""
                    {index_cmd}
                    @5
                    A=D+A
                    D=M
                    {PUSH_CMD}
                    """
            elif segment == "constant":
                asm_code = f"""
                    {index_cmd}
                    {PUSH_CMD}
                    """
            elif segment == "static":
                asm_code = f"""
                    @{self.source_filename}.{index}
                    D=M
                    {PUSH_CMD}
                    """
            else:
                point_int = "THIS" if index == 0 else "THAT"
                asm_code = f"""
                        @{point_int}
                        D=M
                        {PUSH_CMD}
                        """
        # pop
        elif segment in BASE_MEMORY_SEGMENT:
            segment_code = SEGMENT_MAP.get(segment)
            asm_code = f"""
                    {index_cmd}
                    @{segment_code}
                    D=D+M
                    @R13
                    M=D
                    {POP_CMD}
                    @R13
                    A=M
                    M=D
                    """
        elif segment == "temp":
            asm_code = f"""
                    {index_cmd}
                    @5
                    D=D+A
                    @R13
                    M=D
                    {POP_CMD}
                    @R13
                    A=M
                    M=D
                    """
        elif segment == "static":
            asm_code = f"""
                    {POP_CMD}
                    @{self.source_filename}.{index}
                    M=D
                    """
        else:
            point_int = "THIS" if index == 0 else "THAT"
            asm_code = f"""
                    {POP_CMD}
                    @{point_int}
                    M=D
                    """
        self.__output_file.write(f"\n//{command} {segment} {index} \n")
        self.__output_file.write(asm_code)

    def write_label(self, command: str) -> None:
        """Label method."""
        asm = f"({command})"
        self.__output_file.write(f"\n// label {command}")
        self.__output_file.write("\n")
        self.__output_file.write(asm)

    def write_goto(self, command: str) -> None:
        """GOTO method."""
        asm = f"""
        @{command}
        0;JMP
        """
        self.__output_file.write(f"\n// goto {command}")
        self.__output_file.write(asm)

    def write_if(self, command: str) -> None:
        """IF method."""
        asm = f"""
        @SP
        AM=M-1
        D=M
        @{command}
        D;JNE
        """
        self.__output_file.write(f"\n// if {command}")
        self.__output_file.write(asm)

    def write_function(self, fn_name: str, n_vars: int) -> None:
        """Function declaration method."""
        self.__output_file.write(f"\n// function {fn_name} {n_vars}")
        asm = f"""
        ({fn_name})
        """
        self.__output_file.write(asm)

        if n_vars != 0:
            for _i in range(n_vars):
                self.write_push_pop("push", "constant", 0)

    def write_call(self, fn_name: str, n_args: int) -> None:
        """Function call method."""
        return_address_label = "return_add_" + fn_name + "_" + str(uuid.uuid4()).replace("-", "")
        asm = f"""
        //call {fn_name} {n_args}
        @{return_address_label}
        D=A
        {PUSH_CMD}
        @LCL
        D=M
        {PUSH_CMD}
        @ARG
        D=M
        {PUSH_CMD}
        @THIS
        D=M
        {PUSH_CMD}
        @THAT
        D=M
        {PUSH_CMD}"""
        self.__output_file.write(asm)

        # reposition ARG
        asm = f"""
        @SP
        D=M
        @5
        D=D-A
        @{n_args}
        D=D-A
        @ARG
        M=D
        """
        self.__output_file.write(asm)
        # self.write_push_pop("push", "constant", 5)
        # self.writer_arithmetic("sub")
        # self.write_push_pop("push", "constant", n_args)
        # self.writer_arithmetic("sub")

        asm = f"""
        //LCL
        @SP
        D=M
        @LCL
        M=D
        //goto
        @{fn_name}
        0;JMP
        ({return_address_label})
        """
        self.__output_file.write(asm)

    def write_return(self) -> None:
        """Return method."""
        self.__output_file.write("\n//return")
        asm = """
        //frame
        @LCL
        D=M
        @R14
        M=D
        """
        self.__output_file.write(asm)

        # return address
        # asm = f"""
        # //@R14
        # //D=M
        # //////////////////////////////////////
        # {PUSH_CMD}
        # """
        # self.__output_file.write(asm)
        # self.write_push_pop("push", "constant", 5)
        # self.writer_arithmetic("sub")

        # asm = """
        # //@SP
        # //AM=M-1
        # D=M
        # @R15
        # M=D
        # //@SP
        # //M=M-1
        # ///////////////////////////////////////
        # """
        # self.__output_file.write(asm)

        # return address
        asm = """
        @5
        AD=D-A
        D=M
        @R15
        M=D
        """
        self.__output_file.write(asm)
        # reposition return value to arg
        self.write_push_pop("pop", "argument", 0)
        # reposition SP
        asm = """
        @ARG
        D=M+1
        @SP
        M=D
        //reposition THAT
        @R14
        DM=M-1
        A=D
        D=M
        @THAT
        M=D
        //reposition THIS
        @R14
        AM=M-1
        D=M
        @THIS
        M=D
        //reposition ARG
        @R14
        AM=M-1
        D=M
        @ARG
        M=D
        //reposition LCL
        @R14
        AM=M-1
        D=M
        @LCL
        M=D
        //goto
        @R15
        A=M
        0;JMP
        """
        self.__output_file.write(asm)


class ExitCode(IntEnum):
    """Exit code enum."""

    SUCCESS = 0
    ERROR = 1
    INVALID_ARGS = 2


def parse_arg() -> argparse.Namespace:
    """Argument parser fn."""
    parser = argparse.ArgumentParser(description="Translate vmcode to assembly")
    parser.add_argument("filename", type=Path, help="Path to input file")
    return parser.parse_args()


def main() -> None:
    """Main fn."""
    try:
        # 1. get the name of input source file from cmd arg
        args = parse_arg()
        filename: str = args.filename

        filename = Path(args.filename)
        if not filename.exists():
            raise FileNotFoundError(f"Directory not found: {filename}")
        if filename.is_file():
            print("working on file")

            with Parser(filename) as parser, CodeWriter(filename) as code_writer:
                code_writer.source_filename = str(filename).split(".")[0]
                while parser.has_more_lines:
                    parser.advance()
                    if parser.current_command != "" and parser.current_command[0:2] != "//":
                        command = parser.current_command.split(" ")[0]
                        command_type = parser.command_type(command)
                        arg1 = ""
                        arg2 = ""
                        arg3 = ""
                        if command_type != CommandType.C_RETURN:
                            arg1 = parser.arg1()

                        if (
                            command_type == CommandType.C_POP
                            or command_type == CommandType.C_PUSH
                            or command_type == CommandType.C_FUNCTION
                            or command_type == CommandType.C_CALL
                            or command_type == CommandType.C_LABEL
                            or command_type == CommandType.C_IF
                            or command_type == CommandType.C_GOTO
                            # command_type != CommandType.C_RETURN
                        ):
                            arg2 = parser.arg2()

                        if command_type in (CommandType.C_FUNCTION, CommandType.C_CALL):
                            arg3 = int(parser.arg3())

                        if command_type == CommandType.C_ARITHMETIC:
                            code_writer.writer_arithmetic(arg1)
                        elif command_type == CommandType.C_LABEL:
                            code_writer.write_label(arg2)
                        elif command_type == CommandType.C_GOTO:
                            code_writer.write_goto(arg2)
                        elif command_type == CommandType.C_IF:
                            code_writer.write_if(arg2)
                        elif command_type == CommandType.C_FUNCTION:
                            code_writer.write_function(arg2, arg3)
                        elif command_type == CommandType.C_CALL:
                            code_writer.write_call(arg2, arg3)
                        elif command_type == CommandType.C_RETURN:
                            code_writer.write_return()
                        else:
                            code_writer.write_push_pop(arg1, arg2, int(parser.current_command.split()[2]))
        elif filename.is_dir():
            with CodeWriter(filename) as code_writer:
                print("working on directory")
                all_files = list(filename.glob("*.*"))
                priority_file = "Sys.vm"
                # print(all_files)
                # print(Path.joinpath(filename, priority_file))
                sys_vm = next((f for f in all_files if f.name == priority_file), None)

                if sys_vm:
                    print("working on priority file")
                    file_path = Path.joinpath(filename, priority_file)
                    print(file_path)
                    print(filename)
                    print(type(file_path))
                    with Parser(file_path) as parser:
                        print(str(file_path).split(".")[0].split("/")[-1])
                        code_writer.source_filename = str(file_path).split(".")[0].split("/")[-1]
                        while parser.has_more_lines:
                            parser.advance()
                            if parser.current_command != "" and parser.current_command[0:2] != "//":
                                command = parser.current_command.split(" ")[0]
                                command_type = parser.command_type(command)
                                print(parser.current_command)
                                arg1 = ""
                                arg2 = ""
                                arg3 = ""
                                if command_type != CommandType.C_RETURN:
                                    arg1 = parser.arg1()

                                if (
                                    command_type == CommandType.C_POP
                                    or command_type == CommandType.C_PUSH
                                    or command_type == CommandType.C_FUNCTION
                                    or command_type == CommandType.C_CALL
                                    or command_type == CommandType.C_LABEL
                                    or command_type == CommandType.C_IF
                                    or command_type == CommandType.C_GOTO
                                    # command_type != CommandType.C_RETURN
                                ):
                                    arg2 = parser.arg2()

                                if command_type in (CommandType.C_FUNCTION, CommandType.C_CALL):
                                    arg3 = int(parser.arg3())

                                if command_type == CommandType.C_ARITHMETIC:
                                    code_writer.writer_arithmetic(arg1)
                                elif command_type == CommandType.C_LABEL:
                                    code_writer.write_label(arg2)
                                elif command_type == CommandType.C_GOTO:
                                    code_writer.write_goto(arg2)
                                elif command_type == CommandType.C_IF:
                                    code_writer.write_if(arg2)
                                elif command_type == CommandType.C_FUNCTION:
                                    code_writer.write_function(arg2, arg3)
                                elif command_type == CommandType.C_CALL:
                                    code_writer.write_call(arg2, arg3)
                                elif command_type == CommandType.C_RETURN:
                                    code_writer.write_return()
                                else:
                                    code_writer.write_push_pop(arg1, arg2, int(parser.current_command.split()[2]))

                print("working on other files")
                for file in all_files:
                    extension = Path(file).name.split(".")[-1]
                    file_name = Path(file).name.split("/")[-1]
                    static_file_name = file_name.split(".")[0]
                    if file_name != "Sys.vm" and extension == "vm":
                        with Parser(file) as parser:
                            print(str(file).split(".")[0].split("/")[-1])
                            x_name = str(file).split(".")[0].split("/")[-1]
                            print(type(x_name))
                            code_writer.source_filename = x_name
                            print("t")
                            while parser.has_more_lines:
                                parser.advance()
                                if parser.current_command != "" and parser.current_command[0:2] != "//":
                                    command = parser.current_command.split(" ")[0]
                                    command_type = parser.command_type(command)
                                    arg1 = ""
                                    arg2 = ""
                                    arg3 = ""
                                    if command_type != CommandType.C_RETURN:
                                        arg1 = parser.arg1()

                                    if (
                                        command_type == CommandType.C_POP
                                        or command_type == CommandType.C_PUSH
                                        or command_type == CommandType.C_FUNCTION
                                        or command_type == CommandType.C_CALL
                                        or command_type == CommandType.C_LABEL
                                        or command_type == CommandType.C_IF
                                        or command_type == CommandType.C_GOTO
                                        # command_type != CommandType.C_RETURN
                                    ):
                                        arg2 = parser.arg2()

                                    if command_type in (CommandType.C_FUNCTION, CommandType.C_CALL):
                                        arg3 = int(parser.arg3())

                                    if command_type == CommandType.C_ARITHMETIC:
                                        code_writer.writer_arithmetic(arg1)
                                    elif command_type == CommandType.C_LABEL:
                                        code_writer.write_label(arg2)
                                    elif command_type == CommandType.C_GOTO:
                                        code_writer.write_goto(arg2)
                                    elif command_type == CommandType.C_IF:
                                        code_writer.write_if(arg2)
                                    elif command_type == CommandType.C_FUNCTION:
                                        code_writer.write_function(arg2, arg3)
                                    elif command_type == CommandType.C_CALL:
                                        code_writer.write_call(arg2, arg3)
                                    elif command_type == CommandType.C_RETURN:
                                        code_writer.write_return()
                                    else:
                                        code_writer.write_push_pop(arg1, arg2, int(parser.current_command.split()[2]))

        # with open(file_path, 'r') as file:
        #     print(file.read()

        return ExitCode.SUCCESS
    except ValueError:
        return ExitCode.INVALID_ARGS
    except (FileNotFoundError, PermissionError) as e:
        raise type(e)(f"Error reading file {filename}: {str(e)}")
    except Exception:
        return ExitCode.ERROR

    # 2. construct parser

    # 3. parse input file

    # 4. create poutput file .asm

    # 5. enters loop, iterate through the vm commands in the input file

    # 6. for line uses Parser and CodeWriter services


if __name__ == "__main__":
    sys.exit(main())
