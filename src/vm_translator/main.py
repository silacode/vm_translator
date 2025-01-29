"""Main entry point for the Hack vm-translator."""

import sys
from enum import IntEnum
from pathlib import Path
from typing import List

from vm_translator.cli import parse_args
from vm_translator.code_writer import CodeWriter
from vm_translator.constants import CommandType
from vm_translator.parser import Parser


class ExitCode(IntEnum):
    """Exit code enum."""

    SUCCESS = 0
    ERROR = 1
    INVALID_ARGS = 2


def get_vm_files(path: Path) -> List[Path]:
    """Get list of VM files from a path.

    Args:
        path: Path to a single VM file or directory containing VM files

    Returns:
        List of Path objects pointing to VM files
    """
    if path.is_file():
        return [path]
    return sorted([f for f in path.glob("*.vm") if f.is_file()])


def prioritize_sys(files: List[Path]) -> List[Path]:
    """Reorder VM files to ensure Sys.vm is processed first if present.

    Args:
        files: List of Path objects pointing to VM files

    Returns:
        Reordered list with Sys.vm as the first element if present, otherwise unchanged list
    """
    sys_vm = next((f for f in files if f.name == "Sys.vm"), None)
    if sys_vm:
        return [sys_vm] + [f for f in files if f != sys_vm]
    return files


def process_vm_file(vm_file: Path, writer: CodeWriter) -> None:
    """Process a single VM file and translate it to assembly using the CodeWriter.

    Args:
        vm_file: Path to the VM file to process
        writer: CodeWriter instance to write the assembly code
    """
    writer.set_filename(vm_file)
    with Parser(vm_file) as parser:
        while parser.has_more_commands():
            parser.advance()
            cmd_type = parser.command_type
            args = parser.args

            if cmd_type == CommandType.C_ARITHMETIC:
                writer.writer_arithmetic(args[0])
            elif cmd_type == CommandType.C_RETURN:
                writer.write_return()
            elif cmd_type in (CommandType.C_PUSH, CommandType.C_POP):
                writer.write_push_pop(cmd_type, args[1], int(args[2]))
            elif cmd_type in (CommandType.C_LABEL, CommandType.C_GOTO, CommandType.C_IF):
                writer.write_label(args[1]) if cmd_type == CommandType.C_LABEL else writer.write_goto(
                    args[1]
                ) if cmd_type == CommandType.C_GOTO else writer.write_if(args[1])
            elif cmd_type == CommandType.C_FUNCTION:
                writer.write_function(args[1], int(args[2]))
            elif cmd_type == CommandType.C_CALL:
                writer.write_call(args[1], int(args[2]))


def main() -> ExitCode:
    """Main function that processes VM files and translates them to assembly code.

    Returns:
        ExitCode: The exit status of the program execution
    """
    try:
        args = parse_args()
        path: Path = args.path.resolve()
        output_path = path.with_suffix(".asm") if path.is_file() else path.parent / f"{path.name}.asm"
        vm_files = get_vm_files(path)

        with CodeWriter(output_path) as writer:
            if path.is_dir() and any(f.name == "Sys.vm" for f in vm_files):
                writer.write_init()

            for vm_file in prioritize_sys(vm_files):
                process_vm_file(vm_file, writer)

            return ExitCode.SUCCESS
    except ValueError:
        return ExitCode.INVALID_ARGS
    except (FileNotFoundError, PermissionError) as e:
        error_msg = f"Error reading file {path}: {e}"
        raise type(e)(error_msg) from e
    except OSError:
        return ExitCode.ERROR


if __name__ == "__main__":
    sys.exit(main())
