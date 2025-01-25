
        @256
        D=A
        @SP
        M=D
        
        //call Sys.init 0
        @return_add_Sys.init_b68e8bbff177440990786f99824924fa
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
        (return_add_Sys.init_b68e8bbff177440990786f99824924fa)
        
// function Sys.init 0
        (Sys.init)
        
//push constant 4000 

                    
                @4000
                D=A
                
                    
        @SP
        A=M
        M=D
        @SP
        M=M+1
        
                    
//pop pointer 0 

                    
        @SP
        AM=M-1
        D=M
        
                    @THIS
                    M=D
                    
//push constant 5000 

                    
                @5000
                D=A
                
                    
        @SP
        A=M
        M=D
        @SP
        M=M+1
        
                    
//pop pointer 1 

                    
        @SP
        AM=M-1
        D=M
        
                    @THAT
                    M=D
                    
        //call Sys.main 0
        @return_add_Sys.main_280fc4b6bbcb4ff59dfa5eb46ea3bb35
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
        @Sys.main
        0;JMP
        (return_add_Sys.main_280fc4b6bbcb4ff59dfa5eb46ea3bb35)
        
//pop temp 1 

                    
                @1
                D=A
                
                    @5
                    D=D+A
                    @R13
                    M=D
                    
        @SP
        AM=M-1
        D=M
        
                    @R13
                    A=M
                    M=D
                    
// label LOOP
(LOOP)
// goto LOOP
        @LOOP
        0;JMP
        
// function Sys.main 5
        (Sys.main)
        
//push constant 0 

                    
                @0
                D=A
                
                    
        @SP
        A=M
        M=D
        @SP
        M=M+1
        
                    
//push constant 0 

                    
                @0
                D=A
                
                    
        @SP
        A=M
        M=D
        @SP
        M=M+1
        
                    
//push constant 0 

                    
                @0
                D=A
                
                    
        @SP
        A=M
        M=D
        @SP
        M=M+1
        
                    
//push constant 0 

                    
                @0
                D=A
                
                    
        @SP
        A=M
        M=D
        @SP
        M=M+1
        
                    
//push constant 0 

                    
                @0
                D=A
                
                    
        @SP
        A=M
        M=D
        @SP
        M=M+1
        
                    
//push constant 4001 

                    
                @4001
                D=A
                
                    
        @SP
        A=M
        M=D
        @SP
        M=M+1
        
                    
//pop pointer 0 

                    
        @SP
        AM=M-1
        D=M
        
                    @THIS
                    M=D
                    
//push constant 5001 

                    
                @5001
                D=A
                
                    
        @SP
        A=M
        M=D
        @SP
        M=M+1
        
                    
//pop pointer 1 

                    
        @SP
        AM=M-1
        D=M
        
                    @THAT
                    M=D
                    
//push constant 200 

                    
                @200
                D=A
                
                    
        @SP
        A=M
        M=D
        @SP
        M=M+1
        
                    
//pop local 1 

                    
                @1
                D=A
                
                    @LCL
                    D=D+M
                    @R13
                    M=D
                    
        @SP
        AM=M-1
        D=M
        
                    @R13
                    A=M
                    M=D
                    
//push constant 40 

                    
                @40
                D=A
                
                    
        @SP
        A=M
        M=D
        @SP
        M=M+1
        
                    
//pop local 2 

                    
                @2
                D=A
                
                    @LCL
                    D=D+M
                    @R13
                    M=D
                    
        @SP
        AM=M-1
        D=M
        
                    @R13
                    A=M
                    M=D
                    
//push constant 6 

                    
                @6
                D=A
                
                    
        @SP
        A=M
        M=D
        @SP
        M=M+1
        
                    
//pop local 3 

                    
                @3
                D=A
                
                    @LCL
                    D=D+M
                    @R13
                    M=D
                    
        @SP
        AM=M-1
        D=M
        
                    @R13
                    A=M
                    M=D
                    
//push constant 123 

                    
                @123
                D=A
                
                    
        @SP
        A=M
        M=D
        @SP
        M=M+1
        
                    
        //call Sys.add12 1
        @return_add_Sys.add12_415ce1f3372a40b4b33520fba4384729
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
        @Sys.add12
        0;JMP
        (return_add_Sys.add12_415ce1f3372a40b4b33520fba4384729)
        
//pop temp 0 

                    
                @0
                D=A
                
                    @5
                    D=D+A
                    @R13
                    M=D
                    
        @SP
        AM=M-1
        D=M
        
                    @R13
                    A=M
                    M=D
                    
//push local 0 

                    
                @0
                D=A
                
                    @LCL
                    A=D+M
                    D=M
                    
        @SP
        A=M
        M=D
        @SP
        M=M+1
        
                    
//push local 1 

                    
                @1
                D=A
                
                    @LCL
                    A=D+M
                    D=M
                    
        @SP
        A=M
        M=D
        @SP
        M=M+1
        
                    
//push local 2 

                    
                @2
                D=A
                
                    @LCL
                    A=D+M
                    D=M
                    
        @SP
        A=M
        M=D
        @SP
        M=M+1
        
                    
//push local 3 

                    
                @3
                D=A
                
                    @LCL
                    A=D+M
                    D=M
                    
        @SP
        A=M
        M=D
        @SP
        M=M+1
        
                    
//push local 4 

                    
                @4
                D=A
                
                    @LCL
                    A=D+M
                    D=M
                    
        @SP
        A=M
        M=D
        @SP
        M=M+1
        
                    
//add
        @SP
        AM=M-1
        D=M
        A=A-1
        M=D+M
//add
        @SP
        AM=M-1
        D=M
        A=A-1
        M=D+M
//add
        @SP
        AM=M-1
        D=M
        A=A-1
        M=D+M
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
        
// function Sys.add12 0
        (Sys.add12)
        
//push constant 4002 

                    
                @4002
                D=A
                
                    
        @SP
        A=M
        M=D
        @SP
        M=M+1
        
                    
//pop pointer 0 

                    
        @SP
        AM=M-1
        D=M
        
                    @THIS
                    M=D
                    
//push constant 5002 

                    
                @5002
                D=A
                
                    
        @SP
        A=M
        M=D
        @SP
        M=M+1
        
                    
//pop pointer 1 

                    
        @SP
        AM=M-1
        D=M
        
                    @THAT
                    M=D
                    
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
        
                    
//push constant 12 

                    
                @12
                D=A
                
                    
        @SP
        A=M
        M=D
        @SP
        M=M+1
        
                    
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
        