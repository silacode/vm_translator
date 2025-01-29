"""Parser class."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Optional, Self, Type

from vm_translator.constants import ARITHMETIC_COMMANDS, COMMAND_TYPE_MAP, CommandType

if TYPE_CHECKING:
    from types import TracebackType


class Parser:
    """A context manager Parser class.

    It manages file handling and parses the vm code.
    """

    def __init__(self, file_path: Path) -> None:
        """Parser Constructor."""
        self.__file = file_path.open()
        self.current_command: Optional[str] = None

    def __enter__(self) -> Self:
        """Context manager enter method."""
        return self

    def __exit__(
        self, _type: Optional[Type[BaseException]], _value: Optional[BaseException], _traceback: Optional[TracebackType]
    ) -> None:
        """Context manager exit method."""
        if self.__file:
            self.__file.close()

    def has_more_commands(self) -> bool:
        """Check if there are more commands to process in the input file.

        Returns:
            bool: True if there are more commands, False otherwise.
        """
        pos = self.__file.tell()
        has_more = bool(self.__file.readline())
        self.__file.seek(pos)
        return has_more

    def advance(self) -> None:
        """Read next line."""
        while True:
            line = self.__file.readline()
            if not line:
                self.current_command = None
                return
            line = line.partition("//")[0].strip()
            if line:
                self.current_command = line
                return

    @property
    def command_type(self) -> CommandType:
        """Determine the command type from a given VM command string.

        Returns:
            CommandType enum value or None if invalid command
        """
        cmd = self.current_command.split()[0]
        if cmd in ARITHMETIC_COMMANDS:
            return CommandType.C_ARITHMETIC
        return COMMAND_TYPE_MAP.get(cmd)

    @property
    def args(self) -> list[str]:
        """Get args."""
        return self.current_command.split()
