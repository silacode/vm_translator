@256
D=A
@SP
M=D

// call Sys.init 0
        @RETURN_Sys.init_0
        D=A
        @SP
A=M
M=D
@SP
M=M+1

        @LCL
        D=M
        @SP
A=M
M=D
@SP
M=M+1

        @ARG
        D=M
        @SP
A=M
M=D
@SP
M=M+1

        @THIS
        D=M
        @SP
A=M
M=D
@SP
M=M+1

        @THAT
        D=M
        @SP
A=M
M=D
@SP
M=M+1

        @SP
        D=M
        @5
        D=D-A
        @0
        D=D-A
        @ARG
        M=D
        @SP
        D=M
        @LCL
        M=D
        @Sys.init
        0;JMP
        (RETURN_Sys.init_0)

(Sys.init)

// push constant 6
@6
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 8
@8
D=A
@SP
A=M
M=D
@SP
M=M+1

// call Class1.set 2
        @RETURN_Class1.set_1
        D=A
        @SP
A=M
M=D
@SP
M=M+1

        @LCL
        D=M
        @SP
A=M
M=D
@SP
M=M+1

        @ARG
        D=M
        @SP
A=M
M=D
@SP
M=M+1

        @THIS
        D=M
        @SP
A=M
M=D
@SP
M=M+1

        @THAT
        D=M
        @SP
A=M
M=D
@SP
M=M+1

        @SP
        D=M
        @5
        D=D-A
        @2
        D=D-A
        @ARG
        M=D
        @SP
        D=M
        @LCL
        M=D
        @Class1.set
        0;JMP
        (RETURN_Class1.set_1)

// pop temp 0
@SP
AM=M-1
D=M
@5
M=D

// push constant 23
@23
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 15
@15
D=A
@SP
A=M
M=D
@SP
M=M+1

// call Class2.set 2
        @RETURN_Class2.set_2
        D=A
        @SP
A=M
M=D
@SP
M=M+1

        @LCL
        D=M
        @SP
A=M
M=D
@SP
M=M+1

        @ARG
        D=M
        @SP
A=M
M=D
@SP
M=M+1

        @THIS
        D=M
        @SP
A=M
M=D
@SP
M=M+1

        @THAT
        D=M
        @SP
A=M
M=D
@SP
M=M+1

        @SP
        D=M
        @5
        D=D-A
        @2
        D=D-A
        @ARG
        M=D
        @SP
        D=M
        @LCL
        M=D
        @Class2.set
        0;JMP
        (RETURN_Class2.set_2)

// pop temp 0
@SP
AM=M-1
D=M
@5
M=D

// call Class1.get 0
        @RETURN_Class1.get_3
        D=A
        @SP
A=M
M=D
@SP
M=M+1

        @LCL
        D=M
        @SP
A=M
M=D
@SP
M=M+1

        @ARG
        D=M
        @SP
A=M
M=D
@SP
M=M+1

        @THIS
        D=M
        @SP
A=M
M=D
@SP
M=M+1

        @THAT
        D=M
        @SP
A=M
M=D
@SP
M=M+1

        @SP
        D=M
        @5
        D=D-A
        @0
        D=D-A
        @ARG
        M=D
        @SP
        D=M
        @LCL
        M=D
        @Class1.get
        0;JMP
        (RETURN_Class1.get_3)

// call Class2.get 0
        @RETURN_Class2.get_4
        D=A
        @SP
A=M
M=D
@SP
M=M+1

        @LCL
        D=M
        @SP
A=M
M=D
@SP
M=M+1

        @ARG
        D=M
        @SP
A=M
M=D
@SP
M=M+1

        @THIS
        D=M
        @SP
A=M
M=D
@SP
M=M+1

        @THAT
        D=M
        @SP
A=M
M=D
@SP
M=M+1

        @SP
        D=M
        @5
        D=D-A
        @0
        D=D-A
        @ARG
        M=D
        @SP
        D=M
        @LCL
        M=D
        @Class2.get
        0;JMP
        (RETURN_Class2.get_4)

(Sys.init$END)

// goto END
@Sys.init$END
0;JMP

(Class1.set)

@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

// pop static 0
@SP
AM=M-1
D=M
@Class1.0
M=D

@1
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

// pop static 1
@SP
AM=M-1
D=M
@Class1.1
M=D

// push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

// return
        @LCL
        D=M
        @R14
        M=D
        @5
        A=D-A
        D=M
        @R15
        M=D
        @SP
AM=M-1
D=M

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

(Class1.get)

// push static 0
@Class1.0
D=M
@SP
A=M
M=D
@SP
M=M+1

// push static 1
@Class1.1
D=M
@SP
A=M
M=D
@SP
M=M+1

//sub
@SP
AM=M-1
D=M
A=A-1
M=M-D

// return
        @LCL
        D=M
        @R14
        M=D
        @5
        A=D-A
        D=M
        @R15
        M=D
        @SP
AM=M-1
D=M

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

(Class2.set)

@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

// pop static 0
@SP
AM=M-1
D=M
@Class2.0
M=D

@1
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1

// pop static 1
@SP
AM=M-1
D=M
@Class2.1
M=D

// push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1

// return
        @LCL
        D=M
        @R14
        M=D
        @5
        A=D-A
        D=M
        @R15
        M=D
        @SP
AM=M-1
D=M

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

(Class2.get)

// push static 0
@Class2.0
D=M
@SP
A=M
M=D
@SP
M=M+1

// push static 1
@Class2.1
D=M
@SP
A=M
M=D
@SP
M=M+1

//sub
@SP
AM=M-1
D=M
A=A-1
M=M-D

// return
        @LCL
        D=M
        @R14
        M=D
        @5
        A=D-A
        D=M
        @R15
        M=D
        @SP
AM=M-1
D=M

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

