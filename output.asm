
        @256
        D=A
        @SP
        M=D
        
        //call Sys.init 0
        @return_add_Sys.init_71f034e597ac4454b1a13d8a3bedcefa
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
        
        //LCL
        @SP
        D=M
        @LCL
        M=D
        //goto
        @Sys.init
        0;JMP
        (return_add_Sys.init_71f034e597ac4454b1a13d8a3bedcefa)
        
// function Sys.init 0
        (Sys.init)
        
//push constant 4 

                    
                @4
                D=A
                
                    
        @SP
        A=M
        M=D
        @SP
        M=M+1
        
                    
        //call Main.fibonacci 1
        @return_add_Main.fibonacci_652f1fbba960471e885301a305b56ef5
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
        @1
        D=D-A
        @ARG
        M=D
        
        //LCL
        @SP
        D=M
        @LCL
        M=D
        //goto
        @Main.fibonacci
        0;JMP
        (return_add_Main.fibonacci_652f1fbba960471e885301a305b56ef5)
        
// label END
(END)
// goto END
        @END
        0;JMP
        
// function Main.fibonacci 0
        (Main.fibonacci)
        
//push argument 0 

                    
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
        
                    
//push constant 2 

                    
                @2
                D=A
                
                    
        @SP
        A=M
        M=D
        @SP
        M=M+1
        
                    
//lt
        @SP
        AM=M-1
        D=M
        A=A-1
        D=M-D
        @JUMP8e0aa6c8dab311efa0bdd29fa7b56244
        D;JLT
        @SP
        A=M-1
        M=0
        @CONTINUEc81289e6191944d8b580e4b680acdb59
        0;JMP
    (JUMP8e0aa6c8dab311efa0bdd29fa7b56244)
        @SP
        A=M-1
        M=-1
    (CONTINUEc81289e6191944d8b580e4b680acdb59)
        
// if N_LT_2
        @SP
        AM=M-1
        D=M
        @N_LT_2
        D;JNE
        
// goto N_GE_2
        @N_GE_2
        0;JMP
        
// label N_LT_2
(N_LT_2)
//push argument 0 

                    
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
        
                    
//return
        //frame
        @LCL
        D=M
        @R14
        M=D
        
        @5
        AD=D-A
        D=M
        @R15
        M=D
        
//pop argument 0 

                    
                @0
                D=A
                
                    @ARG
                    D=D+M
                    @R13
                    M=D
                    
        @SP
        AM=M-1
        D=M
        
                    @R13
                    A=M
                    M=D
                    
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
        
// label N_GE_2
(N_GE_2)
//push argument 0 

                    
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
        
                    
//push constant 2 

                    
                @2
                D=A
                
                    
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
        //call Main.fibonacci 1
        @return_add_Main.fibonacci_b433bff6e68d40bda014619d44b0a58d
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
        @1
        D=D-A
        @ARG
        M=D
        
        //LCL
        @SP
        D=M
        @LCL
        M=D
        //goto
        @Main.fibonacci
        0;JMP
        (return_add_Main.fibonacci_b433bff6e68d40bda014619d44b0a58d)
        
//push argument 0 

                    
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
        
                    
//push constant 1 

                    
                @1
                D=A
                
                    
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
        //call Main.fibonacci 1
        @return_add_Main.fibonacci_c52bc624ea194d5ba389f3482036bd02
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
        @1
        D=D-A
        @ARG
        M=D
        
        //LCL
        @SP
        D=M
        @LCL
        M=D
        //goto
        @Main.fibonacci
        0;JMP
        (return_add_Main.fibonacci_c52bc624ea194d5ba389f3482036bd02)
        
//add
        @SP
        AM=M-1
        D=M
        A=A-1
        M=D+M
//return
        //frame
        @LCL
        D=M
        @R14
        M=D
        
        @5
        AD=D-A
        D=M
        @R15
        M=D
        
//pop argument 0 

                    
                @0
                D=A
                
                    @ARG
                    D=D+M
                    @R13
                    M=D
                    
        @SP
        AM=M-1
        D=M
        
                    @R13
                    A=M
                    M=D
                    
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
        