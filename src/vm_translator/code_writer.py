"""Code writer class."""

from pathlib import Path
from types import TracebackType
from typing import Optional, Self, TextIO, Type

from vm_translator.constants import (
    ARITHMETIC_TEMPLATES,
    BASE_SEGMENTS,
    BOOTSTRAP_CODE,
    POP_BASE_SEGMENTS_TEMPLATE,
    POP_TEMPLATE,
    PUSH_BASE_SEGMENTS_TEMPLATE,
    PUSH_TEMPLATE,
    SEGMENT_MAP,
    CommandType,
)


class CodeWriter:
    """Context manager code writer class."""

    def __init__(self, output_path: Path) -> None:
        """CodeWriter Constructor."""
        self.file: Optional[TextIO] = None
        self.ouput_path = output_path
        self.label_counter = 0
        self.current_file = ""
        self.function_name = ""

    def __enter__(self) -> Self:
        """CodeWriter context enter method."""
        self.file = self.ouput_path.open("w")
        return self

    def set_source_filename(self, name: str) -> None:
        """Set filename."""
        self.ource_filename = name

    def __exit__(
        self, _type: Optional[Type[BaseException]], _value: Optional[BaseException], _traceback: Optional[TracebackType]
    ) -> None:
        """CodeWriter Context exit method."""
        if self.file:
            self.file.close()

    def set_filename(self, filename: str) -> None:
        """Set the current VM file being processed."""
        self.current_file = filename.stem  # TODO stem is invalid may be trying to get the name without extension

    def _write(self, text: str) -> None:
        if self.file:
            self.file.write(text.strip() + "\n\n")

    def write_init(self) -> None:
        """Writes the VM initialization code and bootstraps the program by calling Sys.init."""
        self._write(BOOTSTRAP_CODE)
        self.write_call("Sys.init", 0)

    def writer_arithmetic(self, command: str) -> None:
        """Writes assembly code for arithmetic commands."""
        if command in {"eq", "gt", "lt"}:
            self.label_counter += 1
            asm = ARITHMETIC_TEMPLATES[command].format(self.label_counter)
        else:
            asm = ARITHMETIC_TEMPLATES[command]
        self._write(f"//{command}\n{asm}\n")

    def write_push_pop(
        self,
        command: CommandType,
        segment: str,
        index: int,
    ) -> None:
        """Write assembly code for push/pop commands.

        Args:
            command: The command type (push or pop)
            segment: Memory segment
            index: Memory index
        """
        if command == CommandType.C_PUSH:
            self._handle_push(segment, index)
        else:
            self._handle_pop(segment, index)

    def _handle_push(self, segment: str, index: int) -> None:
        if segment == "constant":
            self._write(f"// push constant {index}\n@{index}\nD=A\n{PUSH_TEMPLATE}")
        elif segment == "static":
            self._write(f"// push static {index}\n@{self.current_file}.{index}\nD=M\n{PUSH_TEMPLATE}")
        elif segment in BASE_SEGMENTS:
            self._write(PUSH_BASE_SEGMENTS_TEMPLATE.format(index, SEGMENT_MAP[segment]))
        elif segment == "temp":
            self._write(f"// push temp {index}\n@{5 + index}\nD=M\n{PUSH_TEMPLATE}")
        elif segment == "pointer":
            self._write(f"// push pointer {index}\n@{'THIS' if index == 0 else 'THAT'}\nD=M\n{PUSH_TEMPLATE}")

    def _handle_pop(self, segment: str, index: int) -> None:
        if segment == "static":
            self._write(f"// pop static {index}\n{POP_TEMPLATE}@{self.current_file}.{index}\nM=D\n")
        elif segment in BASE_SEGMENTS:
            self._write(POP_BASE_SEGMENTS_TEMPLATE.format(index, SEGMENT_MAP[segment]))
        elif segment == "temp":
            self._write(f"// pop temp {index}\n{POP_TEMPLATE}@{5 + index}\nM=D\n")
        elif segment == "pointer":
            self._write(f"// pop pointer {index}\n{POP_TEMPLATE}@{'THIS' if index == 0 else 'THAT'}\nM=D\n")

    def write_label(self, label: str) -> None:
        """Label method."""
        self._write(f"({self.function_name}${label})\n")

    def write_goto(self, label: str) -> None:
        """GOTO method."""
        self._write(f"// goto {label}\n@{self.function_name}${label}\n0;JMP\n")

    def write_if(self, label: str) -> None:
        """IF method."""
        self._write(f"// if-goto {label}\n{POP_TEMPLATE}@{self.function_name}${label}\nD;JNE\n")

    def write_function(self, fn_name: str, n_vars: int) -> None:
        """Function declaration method."""
        self.function_name = fn_name
        self._write(f"({fn_name})\n")
        for _ in range(n_vars):
            self.write_push_pop(CommandType.C_PUSH, "constant", 0)

    def write_call(self, fn_name: str, n_args: int) -> None:
        """Function call method."""
        return_label = f"RETURN_{fn_name}_{self.label_counter}"
        self.label_counter += 1
        self._write(f"""// call {fn_name} {n_args}
        @{return_label}
        D=A
        {PUSH_TEMPLATE}
        @LCL
        D=M
        {PUSH_TEMPLATE}
        @ARG
        D=M
        {PUSH_TEMPLATE}
        @THIS
        D=M
        {PUSH_TEMPLATE}
        @THAT
        D=M
        {PUSH_TEMPLATE}
        @SP
        D=M
        @5
        D=D-A
        @{n_args}
        D=D-A
        @ARG
        M=D
        @SP
        D=M
        @LCL
        M=D
        @{fn_name}
        0;JMP
        ({return_label})
        """)

    def write_return(self) -> None:
        """Return method."""
        self._write(f"""// return
        @LCL
        D=M
        @R14
        M=D
        @5
        A=D-A
        D=M
        @R15
        M=D
        {POP_TEMPLATE}
        @ARG
        A=M
        M=D
        D=A+1
        @SP
        M=D
        @R14
        AM=M-1
        D=M
        @THAT
        M=D
        @R14
        AM=M-1
        D=M
        @THIS
        M=D
        @R14
        AM=M-1
        D=M
        @ARG
        M=D
        @R14
        AM=M-1
        D=M
        @LCL
        M=D
        @R15
        A=M
        0;JMP
        """)
