"""Constants and enums."""

from enum import StrEnum, auto


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


ARITHMETIC_COMMANDS = frozenset({"add", "sub", "neg", "eq", "gt", "lt", "and", "or", "not"})

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

BASE_SEGMENTS = frozenset({"local", "argument", "this", "that"})

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

ARITHMETIC_TEMPLATES = {
    "add": "@SP\nAM=M-1\nD=M\nA=A-1\nM=D+M",
    "sub": "@SP\nAM=M-1\nD=M\nA=A-1\nM=M-D",
    "neg": "@SP\nA=M-1\nM=-M",
    "eq": "@SP\nAM=M-1\nD=M\nA=A-1\nD=M-D\n@JUMP_{0}\nD;JEQ\n@SP\nA=M-1\nM=0\n@CONTINUE_{0}\n0;JMP\n(JUMP_{0})\n@SP\nA=M-1\nM=-1\n(CONTINUE_{0})",
    "gt": "@SP\nAM=M-1\nD=M\nA=A-1\nD=M-D\n@JUMP_{0}\nD;JGT\n@SP\nA=M-1\nM=0\n@CONTINUE_{0}\n0;JMP\n(JUMP_{0})\n@SP\nA=M-1\nM=-1\n(CONTINUE_{0})",
    "lt": "@SP\nAM=M-1\nD=M\nA=A-1\nD=M-D\n@JUMP_{0}\nD;JLT\n@SP\nA=M-1\nM=0\n@CONTINUE_{0}\n0;JMP\n(JUMP_{0})\n@SP\nA=M-1\nM=-1\n(CONTINUE_{0})",
    "and": "@SP\nAM=M-1\nD=M\nA=A-1\nM=D&M",
    "or": "@SP\nAM=M-1\nD=M\nA=A-1\nM=D|M",
    "not": "@SP\nA=M-1\nM=!M",
}


BOOTSTRAP_CODE = """@256
D=A
@SP
M=D
"""

PUSH_BASE_SEGMENTS_TEMPLATE = """@{0}
D=A
@{1}
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
"""

POP_BASE_SEGMENTS_TEMPLATE = """@{0}
D=A
@{1}
D=D+M
@R13
M=D
@SP
AM=M-1
D=M
@R13
A=M
M=D
"""


PUSH_TEMPLATE = "@SP\nA=M\nM=D\n@SP\nM=M+1\n"

POP_TEMPLATE = "@SP\nAM=M-1\nD=M\n"
