# 8-bit-CPU-emulator

This is a Python emulator for a simple 8-bit computer central processing unit.

Each instrution can run on only two clock cycles: a fetch phase and a decode/execute phase.



Data width      : 8 bits (1 byte).

Address width   : 4 bits (16 RAM addresses).

RAM             : 16 bytes.

Upper nibble    : Instruction opcode.

Lower nibble    : RAM address pointer.



Buses    :

BUS      : Bus         : Transfers instruction opcodes, RAM address pointers, data, ALU results.

MEMLANE  : Memory lane : Transfers RAM address pointers to RAM from PC and MAR.



Registers:

ACT : Accumulator temporary register : Stores ALU A-operand from BUS.

ACC : Accumulator                    : Stores ALU result, outputs to BUS.

IR  : Instruction register           : Stores current instruction opcode from BUS upper nibble.

MAR : Memory address register        : Stores RAM address pointer from BUS lower nibble, outputs to MEMLANE.

PC  : Program counter                : Stores RAM address pointer from PCI, BUS lower nibble, outputs to MEMLANE.

ZF  : Zero flag register             : Intakes and stores HIGH if enabled and if ALU output is zero.

CF  : Carry (overflow) flag register : Stores ALU final carry (overflow) bit.



Circuits:

PCI : Program counter incrementer    : Increments program counter through series of half-adder operations.

ALU : Arithmetic logic unit          : Performs addition of two operands: output of ACT, output of B-operand buffer/inverter.

BB  : B-operand inverting buffer     : Inverts (negates) ALU B-operand upon request.



Instruction set :

0000 XXXX : NOP : No operation.
                  
0001 XXXX : HLT : Halt.
                  
0010 AAAA : LDA : Load data at RAM address AAAA into register ACT, and pass data to ACC (through ALU).
                  
0011 AAAA : ADD : Add data at RAM address AAAA to ACT (through ALU).
                  
0100 AAAA : SUB : Subtract data at RAM address AAAA from ACT (through ALU).
                  
0101 AAAA : STA : Store data from ACC in RAM at address AAAA.
                  
0110 XXXX : INC : Increment ACT.
                  
0111 XXXX : DEC : Decremenet ACT.
                  
1000 AAAA : JCZ : Conditional jump if zero flag is HIGH to RAM address AAAA.
                  
1001 AAAA : JNZ : Conditional jump if zero flag is LOW to RAM address AAAA.
                  
1010 AAAA : JCC : Conditional jump if carry flag is HIGH to RAM address AAAA.
                  
1011 AAAA : JNC : Conditional jump if carry flag is LOW to RAM address AAAA.
                  
1100 AAAA : JMP : Unconditional Jump to RAM address AAAA.
                  
1101 AAAA : NOP : No operation. Yet.
                  
1110 AAAA : NOP : No operation. Yet.
                  
1111 AAAA : NOP : No operation. Yet.
