                                         # Enter assembly code between the '''s:
cod = '''

'''

list = []                                 # Pre-assembler (string operations):
for i in cod:
    if i not in ('\n',' ',';'):
        list.append(i)
cod = list[0]
list.pop(0)
for i in list:
    cod += i
cod += 'NNN'

RAM = {'0000':'00000000', # RAM address 0.
       '0001':'00000000', # RAM address 1.
       '0010':'00000000', # RAM address 2.
       '0011':'00000000', # RAM address 3.
       '0100':'00000000', # RAM address 4.
       '0101':'00000000', # RAM address 5.
       '0110':'00000000', # RAM address 6.
       '0111':'00000000', # RAM address 7.
       '1000':'00000000', # RAM address 8.
       '1001':'00000000', # RAM address 9.
       '1010':'00000000', # RAM address A.
       '1011':'00000000', # RAM address B.
       '1100':'00000000', # RAM address C.
       '1101':'00000000', # RAM address D.
       '1110':'00000000', # RAM address E.
       '1111':'00000000'} # RAM address F.

def dec(i):
    if i == '0':
        return '0000'
    elif i == '1':
        return'0001'
    elif i == '2':
        return '0010'
    elif i == '3':
        return '0011'
    elif i == '4':
        return '0100'
    elif i == '5':
        return '0101'
    elif i == '6':
        return '0110'
    elif i == '7':
        return '0111'
    elif i == '8':
        return '1000'
    elif i == '9':
        return '1001'
    elif i == 'A':
        return '1010'
    elif i == 'B':
        return '1011'
    elif i == 'C':
        return '1100'
    elif i == 'D':
        return '1101'
    elif i == 'E':
        return '1110'
    elif i == 'F':
        return '1111'

sk1 = 'N'
sk2 = 'N'
sk3 = 'N'
sk4 = 'N'
sk5 = 'N'
sk6 = 'N'
sta = 0

for i in range(len(cod)):
    if i == len(cod) - 3:
        break
    if cod[i] == ':':
        i += 1
        n = i
        if n in (sk3,sk4,sk5,sk6):
            continue
        if cod[n] + cod[n+1] + cod[n+2] == 'NOP':
            RAM[dec(str(sta))] = '0000' + '0000'
            sk3 = n+1
            sk4 = n+2
        elif cod[n] + cod[n+1] + cod[n+2] == 'HLT':
            RAM[dec(str(sta))] = '0001' + '0000'
            sk3 = n+1
            sk4 = n+2
        elif cod[n] + cod[n+1] + cod[n+2] == 'LDA':
            sk3 = n+1
            sk4 = n+2
            sk5 = n+3
            RAM[dec(str(sta))] = '0010'+str(dec(cod[sk5]))
        elif cod[n] + cod[n+1] + cod[n+2] == 'ADD':
            sk3 = n+1
            sk4 = n+2
            sk5 = n+3
            RAM[dec(str(sta))] = '0011'+str(dec(cod[sk5]))
        elif cod[n] + cod[n+1] + cod[n+2] == 'SUB':
            sk3 = n+1
            sk4 = n+2
            sk5 = n+3
            RAM[dec(str(sta))] = '0100'+str(dec(cod[sk5]))
        elif cod[n] + cod[n+1] + cod[n+2] == 'STA':
            sk3 = n+1
            sk4 = n+2
            sk5 = n+3
            RAM[dec(str(sta))] = '0101'+str(dec(cod[sk5]))
        elif cod[n] + cod[n+1] + cod[n+2] == 'INC':
            sk3 = n+1
            sk4 = n+2
            RAM[dec(str(sta))] = '0110'+'0000'
        elif cod[n] + cod[n+1] + cod[n+2] == 'DEC':
            sk3 = n+1
            sk4 = n+2
            RAM[dec(str(sta))] = '0111'+'0000'
        elif cod[n] + cod[n+1] + cod[n+2] == 'JCZ':
            sk3 = n+1
            sk4 = n+2
            sk5 = n+3
            RAM[dec(str(sta))] = '1000'+str(dec(cod[sk5]))
        elif cod[n] + cod[n+1] + cod[n+2] == 'JNZ':
            sk3 = n+1
            sk4 = n+2
            sk5 = n+3
            RAM[dec(str(sta))] = '1001'+str(dec(cod[sk5]))
        elif cod[n] + cod[n+1] + cod[n+2] == 'JCC':
            sk3 = n+1
            sk4 = n+2
            sk5 = n+3
            RAM[dec(str(sta))] = '1010'+str(dec(cod[sk5]))
        elif cod[n] + cod[n+1] + cod[n+2] == 'JNC':
            sk3 = n+1
            sk4 = n+2
            sk5 = n+3
            RAM[dec(str(sta))] = '1011'+str(dec(cod[sk5]))
        elif cod[n] + cod[n+1] + cod[n+2] == 'JMP':
            sk3 = n+1
            sk4 = n+2
            sk5 = n+3
            RAM[dec(str(sta))] = '1100'+str(dec(cod[sk5]))
        elif cod[n] + cod[n+1] + cod[n+2] == 'PRT':
            sk3 = n+1
            sk4 = n+2
            sk5 = n+3
            RAM[dec(str(sta))] = '1101'+str(dec(cod[sk5]))
        sta += 1

    if cod[i] == sk1:
        continue
    if cod[i] == sk2:
        continue
    if cod[i] == '=':
        sk1 = cod[i+1]
        sk2 = cod[i+2]
        RAM[dec(cod[i-1])] = str(dec(sk1))+str(dec(sk2))

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
FI                  =   0                 # Write carry-out to CF.
ZI                  =   0                 # Write to ZF if ALU result is 0.
DI                  =   0                 # Write from BUS to binary-hexadecimal decoder.

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
          ZI        =   0
          DI        =   0
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
          ZI        =   0
          DI        =   0
       if IR        == '0001':            # OPCODE 1: HLT (Halt).
          HLT       =   1
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
          ZI        =   0
          DI        =   0
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
          ZI        =   0
          DI        =   0
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
          ZI        =   1
          DI        =   0
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
          FI        =   0
          ZI        =   1
          DI        =   0
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
          ZI        =   0
          DI        =   0
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
          ZI        =   1
          DI        =   0
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
          FI        =   0
          ZI        =   1
          DI        =   0
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
          ZI        =   0
          DI        =   0
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
          ZI        =   0
          DI        =   0
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
          ZI        =   0
          DI        =   0
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
          ZI        =   0
          DI        =   0
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
          ZI        =   0
          DI        =   0
       if IR        == '1101':            # OPCODE 0: PRT (Print data in RAM address).
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
          AW        =   0
          AO        =   0
          BI        =   0
          NE        =   0
          IN        =   0
          FI        =   0
          ZI        =   0
          DI        =   1
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
          ZI        =   0
          DI        =   0
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
          ZI        =   0
          DI        =   0

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
    
    if DI           ==  1:
        if  BUS[:4] ==  '0000':
            MON = '0'
        if  BUS[:4] ==  '0001':
            MON = '1'
        if  BUS[:4] ==  '0010':
            MON = '2'
        if  BUS[:4] ==  '0011':
            MON = '3'
        if  BUS[:4] ==  '0100':
            MON = '4'
        if  BUS[:4] ==  '0101':
            MON = '5'
        if  BUS[:4] ==  '0110':
            MON = '6'
        if  BUS[:4] ==  '0111':
            MON = '7'
        if  BUS[:4] ==  '1000':
            MON = '8'
        if  BUS[:4] ==  '1001':
            MON = '9'
        if  BUS[:4] ==  '1010':
            MON = 'A'
        if  BUS[:4] ==  '1011':
            MON = 'B'
        if  BUS[:4] ==  '1100':
            MON = 'C'
        if  BUS[:4] ==  '1101':
            MON = 'D'
        if  BUS[:4] ==  '1110':
            MON = 'E'
        if  BUS[:4] ==  '1111':
            MON = 'F'
        if  BUS[4:] ==  '0000':
            MON += '0'
        if  BUS[4:] ==  '0001':
            MON += '1'
        if  BUS[4:] ==  '0010':
            MON += '2'
        if  BUS[4:] ==  '0011':
            MON += '3'
        if  BUS[4:] ==  '0100':
            MON += '4'
        if  BUS[4:] ==  '0101':
            MON += '5'
        if  BUS[4:] ==  '0110':
            MON += '6'
        if  BUS[4:] ==  '0111':
            MON += '7'
        if  BUS[4:] ==  '1000':
            MON += '8'
        if  BUS[4:] ==  '1001':
            MON += '9'
        if  BUS[4:] ==  '1010':
            MON += 'A'
        if  BUS[4:] ==  '1011':
            MON += 'B'
        if  BUS[4:] ==  '1100':
            MON += 'C'
        if  BUS[4:] ==  '1101':
            MON += 'D'
        if  BUS[4:] ==  '1110':
            MON += 'E'
        if  BUS[4:] ==  '1111':
            MON += 'F'
        MON = str(CF) + MON
        print(MON)

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
          ZF        =   1
    else:
          ZF        =   0

    CYC          += 1                     # Increment cycle.
