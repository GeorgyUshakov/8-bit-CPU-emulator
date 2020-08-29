RAM                 = {'0000':'00101101', # RAM address 0.
                       '0001':'01011111', # RAM address 1.
                       '0010':'00101110', # RAM address 2.
                       '0011':'01110000', # RAM address 3.
                       '0100':'01011110', # RAM address 4.
                       '0101':'10001010', # RAM address 5.
                       '0110':'00101101', # RAM address 6.
                       '0111':'00111111', # RAM address 7.
                       '1000':'01011111', # RAM address 8.
                       '1001':'11000010', # RAM address 9.
                       '1010':'00010000', # RAM address A.
                       '1011':'00000000', # RAM address B.
                       '1100':'00000000', # RAM address C.
                       '1101':'00001111', # RAM address D.
                       '1110':'00000101', # RAM address E.
                       '1111':'00000000'} # RAM address F.

BUS                 =  '00000000'         # Main 8-bit data BUS.
MEMLANE             =  '0000'             # Memory lane (4-bit RAM address bus).

PC                  =  '0000'             # Program counter register.
MAR                 =  '0000'             # Memory address register.
IR                  =  '0000'             # Instruction register.
ACT                 =  '00000000'         # Accumulator temporary register.
ACC                 =  '00000000'         # Accumulator.
CF                  =   0                 # Carry (ALU overflow) flag register.
ZF                  =   0                 # Zero flag register.

HLT                 =   0                 # Halt.
CI                  =   0                 # Increment PC.
CW                  =   0                 # Write lower nibble from BUS to PC.
CO                  =   0                 # Read from PC to MEMLANE.
MI                  =   0                 # Write upper nibble from BUS to MAR.
MO                  =   0                 # Read from MAR TO MEMLANE.
RI                  =   0                 # Write from BUS to RAM (at address indicated by MEMLANE).
RO                  =   0                 # Read from RAM (at address indicated by MEMLANE) to BUS.
II                  =   0                 # Write upper nibble from BUS to IR.
AI                  =   0                 # Write from BUS to ACT.
AW                  =   0                 # Write from ALU sum to ACC.
AO                  =   0                 # Read from ACC to BUS.
BI                  =   0                 # Add BUS content to ACT through ALU.
NE                  =   0                 # Negate ALU operand.
IN                  =   0                 # Increment ACC (first carry-in).
FI                  =   0                 # Write carry-out to CF AND ZF.

class PCI:                                # Program counter incrementer circuit.
    def __init__(self,C):
        self.C      =   C
    
    def IPC(self):
        Σ0          =   int(self.C[-1]) ^ 1
        C0          =   int(self.C[-1]) & 1
        Σ1          =   int(self.C[-2]) ^ C0
        C1          =   int(self.C[-2]) & C0
        Σ2          =   int(self.C[-3]) ^ C1
        C2          =   int(self.C[-3]) & C1
        Σ3          =   int(self.C[-4]) ^ C2
        return         (str(Σ3) + str(Σ2) + str(Σ1) + str(Σ0))

class ALU:                                # Arithmetic logic unit (ALU) circuit.
    def __init__(self,A,B,Ci):
       self.A       =   A
       self.B       =   B
       self.Ci      =   Ci
    
    def SUM(self):                        # ALU result output.
       Σ0           =  (int(self.A[-1]) ^ int(self.B[-1])) ^ int(self.Ci)
       C0           = ((int(self.A[-1]) ^ int(self.B[-1])) & int(self.Ci)) | (int(self.A[-1]) & int(self.B[-1]))
       Σ1           =  (int(self.A[-2]) ^ int(self.B[-2])) ^ C0
       C1           = ((int(self.A[-2]) ^ int(self.B[-2])) & C0) | (int(self.A[-2]) & int(self.B[-2]))
       Σ2           =  (int(self.A[-3]) ^ int(self.B[-3])) ^ C1
       C2           = ((int(self.A[-3]) ^ int(self.B[-3])) & C1) | (int(self.A[-3]) & int(self.B[-3]))
       Σ3           =  (int(self.A[-4]) ^ int(self.B[-4])) ^ C2
       C3           = ((int(self.A[-4]) ^ int(self.B[-4])) & C2) | (int(self.A[-4]) & int(self.B[-4]))
       Σ4           =  (int(self.A[-5]) ^ int(self.B[-5])) ^ C3
       C4           = ((int(self.A[-5]) ^ int(self.B[-5])) & C3) | (int(self.A[-5]) & int(self.B[-5]))
       Σ5           =  (int(self.A[-6]) ^ int(self.B[-6])) ^ C4
       C5           = ((int(self.A[-6]) ^ int(self.B[-6])) & C4) | (int(self.A[-6]) & int(self.B[-6]))
       Σ6           =  (int(self.A[-7]) ^ int(self.B[-7])) ^ C5
       C6           = ((int(self.A[-7]) ^ int(self.B[-7])) & C5) | (int(self.A[-7]) & int(self.B[-7]))
       Σ7           =  (int(self.A[-8]) ^ int(self.B[-8])) ^ C6
       return          (str(Σ7) + str(Σ6) + str(Σ5) + str(Σ4) + str(Σ3) + str(Σ2) + str(Σ1) + str(Σ0))
    
    def CAR(self):                        # ALU final carry (overflow) output.
       C0           = ((int(self.A[-1]) ^ int(self.B[-1])) & int(self.Ci)) | (int(self.A[-1]) & int(self.B[-1]))
       C1           = ((int(self.A[-2]) ^ int(self.B[-2])) & C0) | (int(self.A[-2]) & int(self.B[-2]))
       C2           = ((int(self.A[-3]) ^ int(self.B[-3])) & C1) | (int(self.A[-3]) & int(self.B[-3]))
       C3           = ((int(self.A[-4]) ^ int(self.B[-4])) & C2) | (int(self.A[-4]) & int(self.B[-4]))
       C4           = ((int(self.A[-5]) ^ int(self.B[-5])) & C3) | (int(self.A[-5]) & int(self.B[-5]))
       C5           = ((int(self.A[-6]) ^ int(self.B[-6])) & C4) | (int(self.A[-6]) & int(self.B[-6]))
       C6           = ((int(self.A[-7]) ^ int(self.B[-7])) & C5) | (int(self.A[-7]) & int(self.B[-7]))
       C7           = ((int(self.A[-8]) ^ int(self.B[-8])) & C6) | (int(self.A[-8]) & int(self.B[-8]))
       return          (str(C7))

CYC                 =   0                 # Initiate cycle number.

while HLT           ==  0:                # Instruction cycle.
    if CYC%2        ==  0:                # Fetch phase (even CYC, i.e. LOW clock).
          HLT       =   0
          CI        =   0
          CW        =   0
          CO        =   1
          MI        =   1
          MO        =   0
          RI        =   0
          RO        =   1
          II        =   1
          AI        =   0
          AW        =   0
          AO        =   0
          BI        =   1
          NE        =   0
          IN        =   0
          FI        =   0
    if CYC%2        !=  0:                # Decode/execute phase (odd CYC, i.e. LOW clock).
       if IR        == '0000':            # OPCODE 0: NOP (No operation).
          HLT       =   0
          CI        =   0
          CW        =   0
          CO        =   0
          MI        =   0
          MO        =   0
          RI        =   0
          RO        =   0
          II        =   0
          AI        =   0
          AW        =   0
          AO        =   0
          BI        =   0
          NE        =   0
          IN        =   0
          FI        =   0
       if IR        == '0001':            # OPCODE 1: HLT (Halt).
          HLT       =  1
          CI        =  0
          CW        =  0
          CO        =  0
          MI        =  0
          MO        =  0
          RI        =  0
          RO        =  0
          II        =  0
          AI        =  0
          AW        =  0
          AO        =  0
          BI        =  0
          NE        =  0
          IN        =  0
          FI        =  0
       if IR        == '0010':            # OPCODE 2: LDA (Load ACT from RAM).
          HLT       =   0
          CI        =   1
          CW        =   0
          CO        =   0
          MI        =   0
          MO        =   1
          RI        =   0
          RO        =   1
          II        =   0
          AI        =   1
          AW        =   1
          AO        =   0
          BI        =   0
          NE        =   0
          IN        =   0
          FI        =   0
       if IR        == '0011':            # OPCODE 3: ADD (Add BUS to ACT).
          HLT       =   0
          CI        =   1
          CW        =   0
          CO        =   0
          MI        =   0
          MO        =   1
          RI        =   0
          RO        =   1
          II        =   0
          AI        =   0
          AW        =   1
          AO        =   0
          BI        =   1
          NE        =   0
          IN        =   0
          FI        =   1
       if IR        == '0100':            # OPCODE 4: SUB (Subtract BUS from ACT).
          HLT       =   0
          CI        =   1
          CW        =   0
          CO        =   0
          MI        =   0
          MO        =   1
          RI        =   0
          RO        =   1
          II        =   0
          AI        =   0
          AW        =   1
          AO        =   0
          BI        =   1
          NE        =   1
          IN        =   1
          FI        =   1
       if IR        == '0101':            # OPCODE 5: STA (Store ACC in RAM).
          HLT       =   0
          CI        =   1
          CW        =   0
          CO        =   0
          MI        =   0
          MO        =   1
          RI        =   1
          RO        =   0
          II        =   0
          AI        =   0
          AW        =   0
          AO        =   1
          BI        =   0
          NE        =   0
          IN        =   0
          FI        =   0
       if IR        == '0110':            # OPCODE 6: INC (Increment ACT).
          HLT       =   0
          CI        =   1
          CW        =   0
          CO        =   0
          MI        =   0
          MO        =   0
          RI        =   0
          RO        =   0
          II        =   0
          AI        =   0
          AW        =   1
          AO        =   0
          BI        =   0
          NE        =   0
          IN        =   1
          FI        =   1
       if IR        == '0111':            # OPCODE 7: DEC (Decrement ACT).
          HLT       =   0
          CI        =   1
          CW        =   0
          CO        =   0
          MI        =   0
          MO        =   0
          RI        =   0
          RO        =   0
          II        =   0
          AI        =   0
          AW        =   1
          AO        =   0
          BI        =   0
          NE        =   1
          IN        =   0
          FI        =   1
       if IR        == '1000':            # OPCODE 8: JCZ (Jump to RAM address if HIGH ZF).
          HLT       =   0
          CI        =   1 & int(not(ZF))
          CW        =   1 & ZF
          CO        =   0
          MI        =   0
          MO        =   0
          RI        =   0
          RO        =   1 & ZF
          II        =   0
          AI        =   0
          AW        =   1 & ZF
          AO        =   0
          BI        =   0
          NE        =   0
          IN        =   0
          FI        =   0
       if IR        == '1001':            # OPCODE 9: JNZ (Jump to RAM address if LOW ZF).
          HLT       =   0
          CI        =   1 & ZF
          CW        =   1 & int(not(ZF))
          CO        =   0
          MI        =   0
          MO        =   0
          RI        =   0
          RO        =   1 & int(not(ZF))
          II        =   0
          AI        =   0
          AW        =   1 & int(not(ZF))
          AO        =   0
          BI        =   0
          NE        =   0
          IN        =   0
          FI        =   0
       if IR        == '1010':            # OPCODE A: JCC (Jump to RAM address if HIGH CF).
          HLT       =   0
          CI        =   1 & int(not(CF))
          CW        =   1 & CF
          CO        =   0
          MI        =   0
          MO        =   0
          RI        =   0
          RO        =   1 & CF
          II        =   0
          AI        =   0
          AW        =   1 & CF
          AO        =   0
          BI        =   0
          NE        =   0
          IN        =   0
          FI        =   0
       if IR        == '1011':            # OPCODE B: JNC (Jump to RAM address if LOW CF).
          HLT       =   0
          CI        =   1 & CF
          CW        =   1 & int(not(CF))
          CO        =   0
          MI        =   0
          MO        =   0
          RI        =   0
          RO        =   1 & int(not(CF))
          II        =   0
          AI        =   0
          AW        =   1 & int(not(CF))
          AO        =   0
          BI        =   0
          NE        =   0
          IN        =   0
          FI        =   0
       if IR        == '1100':            # OPCODE C: JMP (Jump to RAM address).
          HLT       =   0
          CI        =   0
          CW        =   1
          CO        =   0
          MI        =   0
          MO        =   0
          RI        =   0
          RO        =   1
          II        =   0
          AI        =   0
          AW        =   1
          AO        =   0
          BI        =   0
          NE        =   0
          IN        =   0
          FI        =   0
       if IR        == '1101':            # OPCODE 0: NOP (No operation).
          HLT       =   0
          CI        =   0
          CW        =   0
          CO        =   0
          MI        =   0
          MO        =   0
          RI        =   0
          RO        =   0
          II        =   0
          AI        =   0
          AW        =   0
          AO        =   0
          BI        =   0
          NE        =   0
          IN        =   0
          FI        =   0
       if IR        == '1110':            # OPCODE 0: NOP (No operatoin).
          HLT       =   0
          CI        =   0
          CW        =   0
          CO        =   0
          MI        =   0
          MO        =   0
          RI        =   0
          RO        =   0
          II        =   0
          AI        =   0
          AW        =   0
          AO        =   0
          BI        =   0
          NE        =   0
          IN        =   0
          FI        =   0
       if IR        == '1111':            # OPCODE 0: NOP (No operation).
          HLT       =   0
          CI        =   0
          CW        =   0
          CO        =   0
          MI        =   0
          MO        =   0
          RI        =   0
          RO        =   0
          II        =   0
          AI        =   0
          AW        =   0
          AO        =   0
          BI        =   0
          NE        =   0
          IN        =   0
          FI        =   0

    if CI           ==  1:                # Control flow: read to BUS/MEMLANE.
        PC          =   PCI(PC).IPC()
    if CO           ==  1:
       MEMLANE      =   PC
    if MO           ==  1:
       MEMLANE      =   MAR
    if RO           ==  1:
       BUS          =   RAM[MEMLANE]
    if AO           ==  1:
       BUS          =   ACC
    
    if II           ==  1:                # Control flow: write from BUS
       IR           =   BUS[:4]
    if MI           ==  1:
       MAR          =   BUS[4:]
    if CW           ==  1:
       PC           =   BUS[4:]
    if AI           ==  1:
       ACT          =   BUS
    if BI           ==  0:
       BB           =  '00000000'
    if BI           ==  1:
       BB           =   BUS
    
    B0              =   int(BB[-1]) ^ NE  # ALU operand buffer/inverter.
    B1              =   int(BB[-2]) ^ NE
    B2              =   int(BB[-3]) ^ NE
    B3              =   int(BB[-4]) ^ NE
    B4              =   int(BB[-5]) ^ NE
    B5              =   int(BB[-6]) ^ NE
    B6              =   int(BB[-7]) ^ NE
    B7              =   int(BB[-8]) ^ NE
    BB              =   str(B7) + str(B6) + str(B5) + str(B4) + str(B3) + str(B2) + str(B1) + str(B0)

    if AW           ==  1:                # Control flow: write from ALU/BUS.
       ACC          =   ALU(ACT,BB,IN).SUM()
    if RI           ==  1:
       RAM[MEMLANE] =   BUS
    if FI           ==  1:
       CF           =   ALU(ACT,BB,IN).CAR()
       if ACC       == '00000000':
          ZF     =  1
       else:
          ZF        =   0

    CYC          += 1                     # Increment cycle.

print(RAM)                                # Display RAM contents.
