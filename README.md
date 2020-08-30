# 8-bit-CPU-emulator

This is a Python emulator for a simple 8-bit computer central processing unit.

Each instrution can run on only two clock cycles: a fetch phase and a decode/execute phase.



Data width      : 8 bits (1 byte).

Address width   : 4 bits (16 RAM addresses).

RAM             : 16 bytes.

Upper nibble    : Instruction opcode.

Lower nibble    : RAM address pointer.



*Buses    :*

BUS      : Bus         : Transfers instruction opcodes, RAM address pointers, data, ALU results.

MEMLANE  : Memory lane : Transfers RAM address pointers to RAM from PC and MAR.



*Registers:*

ACT : Accumulator temporary register : Stores ALU A-operand from BUS.

ACC : Accumulator                    : Stores ALU result, outputs to BUS.

IR  : Instruction register           : Stores current instruction opcode from BUS upper nibble.

MAR : Memory address register        : Stores RAM address pointer from BUS lower nibble, outputs to MEMLANE.

PC  : Program counter                : Stores RAM address pointer from PCI, BUS lower nibble, outputs to MEMLANE.

ZF  : Zero flag register             : Intakes and stores HIGH if enabled and if ALU output is zero.

CF  : Carry (overflow) flag register : Stores ALU final carry (overflow) bit.



*Circuits:*

PCI : Program counter incrementer    : Increments program counter through series of half-adder operations.

ALU : Arithmetic logic unit          : Performs addition of two operands: output of ACT, output of B-operand buffer/inverter.

BB  : B-operand inverting buffer     : Inverts (negates) ALU B-operand upon request.



*Instruction set with assembly :*

00 : NOP : No operation.
                  
10 : HLT : Halt.
                  
2X : LDA : Load data at RAM address X into register ACT, and pass data to ACC (through ALU).
                  
3X : ADD : Add data at RAM address X to ACT (through ALU).
                  
4X : SUB : Subtract data at RAM address X from ACT (through ALU).
                  
5X : STA : Store data from ACC in RAM at address X.
                  
60 : INC : Increment ACT.
                  
70 : DEC : Decremenet ACT.
                  
8X : JCZ : Conditional jump if zero flag is HIGH to RAM address X.
                  
9X : JNZ : Conditional jump if zero flag is LOW to RAM address X.
                  
AX : JCC : Conditional jump if carry flag is HIGH to RAM address X.
                  
BX : JNC : Conditional jump if carry flag is LOW to RAM address X.
                  
CX : JMP : Unconditional Jump to RAM address R.
                  
D0 : NOP : No operation. Yet.
                  
E0 : NOP : No operation. Yet.
                  
F0 : NOP : No operation. Yet.



* ASSEMBLY LANGUAGE :*

Spaces, newlines, semicolons (;) can be added and won't be read. Other characters will confuse the assembler.

For data input: Address = Value
e.g. F = 01
     Value 1 stored in RAM address F.

For instruction: Address : Instruction Operand
e.g. 0 : LDA F
     When program counter points to RAM address 0, data at RAM address F is loaded into ACT.
