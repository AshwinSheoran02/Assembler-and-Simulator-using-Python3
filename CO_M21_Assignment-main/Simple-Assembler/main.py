import sys

class Register:
    # address is a 3 bit string
    def __init__(self, address):
        self.value = 0;
        self.address = address

    def addr(self):
        return self.address

    def val(self):
        return self.value

# class Variable:
#     def __init__(self, name):
#         self.value = 0;
#         self.name = name;

def Addition(r1, r2, r3): #Performs reg1 = reg2+ reg3. If the computation overflows, then the overflow flag is set 
    # r1 r2 and r3 are the classes
    a = r1.addr()
    b = r2.addr()
    c = r3.addr()
    return "00000" + "00" + a + b + c
    # if overflow-----flag(1,0,0,0)
    # pass
    #if not overflows----flag(0,0,0,0)
# to print the opcode

def Subtraction(r1, r2, r3):  #Performs reg1 = reg2- reg3. In case reg3> reg2, 0 is written to reg1 and overflow flag is set. 
    # r1 r2 and r3 are the classes
    a = r1.addr()
    b = r2.addr()
    c = r3.addr()
    return "00001" + "00" + a + b + c
    
    # pass

def Move_Immediate(r1, x): #Performs reg1 = $Imm where Imm is a 8 bit value.
    # x is int
    bnr = bin(x)
    bnr = bnr.replace('0b','')
    while len(bnr)<8:
        bnr = "0" + bnr

    a = r1.addr()
    # flag(0,0,0,0)

    return "00010" + a + bnr

def Move_Register(r1, r2):
    #r1 and r2 are the classes 
    a = r1.addr()
    b = r2.addr()
    # flag(0,0,0,0)  # call flag here

    return "00011" + "00000" + a + b

def Load(r1, x):
    # x is integer
    a = r1.addr()
    bnr = bin(x)
    bnr = bnr.replace('0b','')
    while len(bnr)<8:
        bnr = "0" + bnr
    # flag(0,0,0,0)
    return "00100" + a + bnr

def Store(r1, x):
    # x is integer
    a = r1.addr()
    bnr = bin(x)
    bnr = bnr.replace('0b','')
    while len(bnr)<8:
        bnr = "0" + bnr
    # flag(0,0,0,0)
    return "00101" + a + bnr

def Multiply(r1, r2, r3):
    # r1 r2 and r3 are the classes
    a = r1.addr()
    b = r2.addr()
    c = r3.addr()
    return "00110" + "00" + a + b + c
            


def Divide(r3, r4):
    a = r3.addr()
    b = r4.addr()
    # flag(0,0,0,0)
    return "00111" + "00000" + a + b
    


def Right_Shift(r1, x):
    # x is int
    bnr = bin(x)
    bnr = bnr.replace('0b','')
    while len(bnr)<8:
        bnr = "0" + bnr

    a = r1.addr()
    # flag(0,0,0,0)
    return "01000" + a + bnr
   


def Left_Shift(r1, x):
    # x is int
    bnr = bin(x)
    bnr = bnr.replace('0b','')
    while len(bnr)<8:
        bnr = "0" + bnr

    a = r1.addr()
    # flag(0,0,0,0)
    return "01001" + a + bnr


def XOR(r1, r2, r3):
    # r1 r2 and r3 are the classes
    a = r1.addr()
    b = r2.addr()
    c = r3.addr()
    # flag(0,0,0,0)
    return "01010" + "00" + a + b + c
            
def OR(r1, r2, r3):
    # r1 r2 and r3 are the classes
    a = r1.addr()
    b = r2.addr()
    c = r3.addr()
    # flag(0,0,0,0)
    return "01011" + "00" + a + b + c
        

def AND(r1, r2, r3):
    # r1 r2 and r3 are the classes
    a = r1.addr()
    b = r2.addr()
    c = r3.addr()
    # flag(0,0,0,0)
    return "01100" + "00" + a + b + c 
    

def Invert(r1, r2):
    a = r1.addr()
    b = r2.addr()
    # flag(0,0,0,0)
    return "01101" + "00000" + a + b

def Compare(r1, r2):
    #r1 and r2 are the classes 
    a = r1.addr()
    b = r2.addr()
    # call flag here
    return "01110" + "00000" + a + b
    

def Unconditional_Jump(x):
    bnr = bin(x)
    bnr = bnr.replace('0b','')
    while len(bnr)<8:
        bnr = "0" + bnr
    

    return "01111" + "000" + bnr
    

def Jump_if_Less_Than(x):
    bnr = bin(x)
    bnr = bnr.replace('0b','')
    while len(bnr)<8:
        bnr = "0" + bnr
    
    return "10000" + "000" + bnr

def Jump_if_Greater_Than(x):
    bnr = bin(x)
    bnr = bnr.replace('0b','')
    while len(bnr)<8:
        bnr = "0" + bnr
    
    return "10001" + "000" + bnr

def Jump_if_Equal(x):
    bnr = bin(x)
    bnr = bnr.replace('0b','')
    while len(bnr)<8:
        bnr = "0" + bnr
    
    return "10010" + "000" + bnr

def Halt():
    # flag(0,0,0,0)
    return "1001100000000000"
    

# def Flag(v, l, g, e):
#     pass
'''main
input 
mul r1 r2 r3
  if list[0]==Multiply:
      mul()
add r1 r2 r3 
 if list[0]== Addition:
     add()

l=[0,1,2,3,4,5,6,7,8,9......,19]
input
list=[]
split().
if list[0] not in l:
    error()


for varible:
    list of inputs:
    after last element first Variable
    variable=8 bit binary 

    x value 10
    x memory adress 7 (list last index+1)
    hlt 6 line '''

global R0;
global R1;
global R2;
global R3;
global R4;
global R5;
global R6;
global FLAGS;
global OutputFile;
global all_registers;
global variable_dict;
global all_resistors_1;
global variable_counter;
global label_dict;

R0 = Register("000")
R1 = Register("001")
R2 = Register("010")
R3 = Register("011")
R4 = Register("100")
R5 = Register("101")
R6 = Register("110")
FLAGS = Register("111")
OutputFile = [];
all_registers = ["R0", "R1", "R2", "R3", "R4", "R5", "R6"];
all_registers_1 = ["R0", "R1", "R2", "R3", "R4", "R5", "R6","FLAGS"];
variable_dict = {}
label_dict = {}
instructions = sys.stdin.readlines()
variable_counter = 0;

for instr in range(len(instructions)):
    if "/n" in instructions[instr]:
        instructions[instr].replace("/n", "")

    ins = list((instructions[instr]).split())
    if len(ins)==0:
        continue
    elif ins[0]=="var":
        variable_counter += 1
    else:
        break
#print(instructions)
for instr in range(len(instructions)):
    #print(instr, len(instructions))
    if "/n" in instructions[instr]:
        instructions[instr].replace("/n", "")
    
    ins = list((instructions[instr]).split())
    if len(ins)==0:
        continue

    elif " :" in instructions[instr]:
        OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error (gap before ':')"]
        instructions = []
        break

    elif ins[0][len(ins[0]) - 1]==":":
        d = ins[0][0:len(ins[0])-1]
        
        if d in label_dict.keys():
            OutputFile = ["Error in line number: " + str(instr+1) + "; Illegal use of labels/variables name"]
            instructions = []
            break
        else:
            label_dict[d] = instr - variable_counter
    
    else:
        continue
    



# def flag(v,l,g,e):
#     a="000000000000"
#     b=str(v)+str(l)+str(e)+str(e)
#     return a+b

for instr in range(len(instructions)):
    if "/n" in instructions[instr]:
        instructions[instr].replace("/n", "")
    ins = list((instructions[instr]).split())  #use default split

    

    if len(ins)==0:
        continue

    if ins[0][-1]==":":
        ins = ins[1:]
 
    if ins[0]=="hlt":
        if instr==len(instructions)-1:
            OutputFile.append(Halt());
            break
        else:
            OutputFile = ["Error in line number: " + str(instr+2) + "; 'hlt' not being used as the last instruction"]
            break
    
    elif ins[0]=="var":
        if len(ins)!=2:
            OutputFile = ["Error : variable not correctly assigned"]
            break
        
        elif len(variable_dict)==variable_counter:
            OutputFile = ["Error in line number: " + str(instr+1) + "; Variable defined in between code"]
            break

        elif ins[1] in label_dict.keys():
            OutputFile = ["Error : Duplicate Label Found"]
            break

        elif ins[1] in variable_dict.keys():
            OutputFile = ["Error : Duplicate Variable Found"]
            break
        
        else:
            d = ins[1]
            #if d in
            variable_dict[d] = len(instructions) + len(variable_dict) - variable_counter


    elif ins[0]=="add":
        if len(ins)==4:
           
            if (ins[1] not in all_registers) or (ins[2] not in all_registers) or (ins[3] not in all_registers):
                OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error, Valid Register not found"]
                break

            else:
                #1st register detection
                if ins[1]=="R0":
                    r1 = R0
                elif ins[1]=="R1":
                    r1 = R1
                elif ins[1]=="R2":
                    r1 = R2
                elif ins[1]=="R3":
                    r1 = R3
                elif ins[1]=="R4":
                    r1 = R4
                elif ins[1]=="R5":
                    r1 = R5
                elif ins[1]=="R6":
                    r1 = R6

                #2nd register detection
                if ins[2]=="R0":
                    r2 = R0
                elif ins[2]=="R1":
                    r2 = R1
                elif ins[2]=="R2":
                    r2 = R2
                elif ins[2]=="R3":
                    r2 = R3
                elif ins[2]=="R4":
                    r2 = R4
                elif ins[2]=="R5":
                    r2 = R5
                elif ins[2]=="R6":
                    r2 = R6

                #3rd register detection
                if ins[3]=="R0":
                    r3 = R0
                elif ins[3]=="R1":
                    r3 = R1
                elif ins[3]=="R2":
                    r3 = R2
                elif ins[3]=="R3":
                    r3 = R3
                elif ins[3]=="R4":
                    r3 = R4
                elif ins[3]=="R5":
                    r3 = R5
                elif ins[3]=="R6":
                    r3 = R6

                OutputFile.append(Addition(r1, r2, r3));

        else:
            OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error"]
            break

    elif ins[0]=="sub":
        if len(ins)==4:
           
            if (ins[1] not in all_registers) or (ins[2] not in all_registers) or (ins[3] not in all_registers):
                OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error, Valid Register not found"]
                break

            else:
                #1st register detection
                if ins[1]=="R0":
                    r1 = R0
                elif ins[1]=="R1":
                    r1 = R1
                elif ins[1]=="R2":
                    r1 = R2
                elif ins[1]=="R3":
                    r1 = R3
                elif ins[1]=="R4":
                    r1 = R4
                elif ins[1]=="R5":
                    r1 = R5
                elif ins[1]=="R6":
                    r1 = R6

                #2nd register detection
                if ins[2]=="R0":
                    r2 = R0
                elif ins[2]=="R1":
                    r2 = R1
                elif ins[2]=="R2":
                    r2 = R2
                elif ins[2]=="R3":
                    r2 = R3
                elif ins[2]=="R4":
                    r2 = R4
                elif ins[2]=="R5":
                    r2 = R5
                elif ins[2]=="R6":
                    r2 = R6

                #3rd register detection
                if ins[3]=="R0":
                    r3 = R0
                elif ins[3]=="R1":
                    r3 = R1
                elif ins[3]=="R2":
                    r3 = R2
                elif ins[3]=="R3":
                    r3 = R3
                elif ins[3]=="R4":
                    r3 = R4
                elif ins[3]=="R5":
                    r3 = R5
                elif ins[3]=="R6":
                    r3 = R6

                OutputFile.append(Subtraction(r1, r2, r3));

        else:
            OutputFile = ["Error in line number: " + str(instr+1), "; Syntax Error"]
            break

    elif ins[0]=="mov":
        if len(ins)==3:
           
            if (ins[1] not in all_registers):
                OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error, Valid Register not found"]
                break

            else:
                #1st register detection
                if ins[1]=="R0":
                    r1 = R0
                elif ins[1]=="R1":
                    r1 = R1
                elif ins[1]=="R2":
                    r1 = R2
                elif ins[1]=="R3":
                    r1 = R3
                elif ins[1]=="R4":
                    r1 = R4
                elif ins[1]=="R5":
                    r1 = R5
                elif ins[1]=="R6":
                    r1 = R6

            if (ins[2])[0]=="$":  #this is detection of imm
                x = int(ins[2][1:])
                if x<0 or x>255:
                    OutputFile = ["Error in line number: " + str(instr+1) + "Illegal Immidiate Value"]
                    break
                else:
                    OutputFile.append(Move_Immediate(r1, x))
                    continue
                    
            
            elif (ins[2] not in all_registers_1) :
                OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error, Valid Register not found"]
                break

            else:
                #2nd register detection
                if ins[2]=="R0":
                    r2 = R0
                elif ins[2]=="R1":
                    r2 = R1
                elif ins[2]=="R2":
                    r2 = R2
                elif ins[2]=="R3":
                    r2 = R3
                elif ins[2]=="R4":
                    r2 = R4
                elif ins[2]=="R5":
                    r2 = R5
                elif ins[2]=="R6":
                    r2 = R6
                else:
                    r2 = FLAGS

            OutputFile.append(Move_Register(r1, r2))

        else:
            OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error"]
            break

    elif ins[0]=="ld":
        if len(ins)==3:
           
            if (ins[1] not in all_registers):
                OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error, Valid Register not found"]
                break

            else:
                #1st register detection
                if ins[1]=="R0":
                    r1 = R0
                elif ins[1]=="R1":
                    r1 = R1
                elif ins[1]=="R2":
                    r1 = R2
                elif ins[1]=="R3":
                    r1 = R3
                elif ins[1]=="R4":
                    r1 = R4
                elif ins[1]=="R5":
                    r1 = R5
                elif ins[1]=="R6":
                    r1 = R6

            jj = ins[2]

            if jj not in variable_dict.keys():
                OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error, Variable not defined"]
                break
            else:
                x = variable_dict[jj]
                OutputFile.append(Load(r1, x))

        else:
            OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax error"]
            break
    
    elif ins[0]=="st":
        if len(ins)==3:
           
            if (ins[1] not in all_registers):
                OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error, Valid Register not found"]
                break

            else:
                #1st register detection
                if ins[1]=="R0":
                    r1 = R0
                elif ins[1]=="R1":
                    r1 = R1
                elif ins[1]=="R2":
                    r1 = R2
                elif ins[1]=="R3":
                    r1 = R3
                elif ins[1]=="R4":
                    r1 = R4
                elif ins[1]=="R5":
                    r1 = R5
                elif ins[1]=="R6":
                    r1 = R6

            jj = ins[2]

            if jj not in variable_dict.keys():
                OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error, Variable not defined"]
                break
            else:
                x = variable_dict[jj]
                OutputFile.append(Store(r1, x))

        else:
            OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error"]
            break
    
    elif ins[0]=="mul":
        if len(ins)==4:
           
            if (ins[1] not in all_registers) or (ins[2] not in all_registers) or (ins[3] not in all_registers):
                OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error, Valid Register not found"]
                break

            else:
                #1st register detection
                if ins[1]=="R0":
                    r1 = R0
                elif ins[1]=="R1":
                    r1 = R1
                elif ins[1]=="R2":
                    r1 = R2
                elif ins[1]=="R3":
                    r1 = R3
                elif ins[1]=="R4":
                    r1 = R4
                elif ins[1]=="R5":
                    r1 = R5
                elif ins[1]=="R6":
                    r1 = R6

                #2nd register detection
                if ins[2]=="R0":
                    r2 = R0
                elif ins[2]=="R1":
                    r2 = R1
                elif ins[2]=="R2":
                    r2 = R2
                elif ins[2]=="R3":
                    r2 = R3
                elif ins[2]=="R4":
                    r2 = R4
                elif ins[2]=="R5":
                    r2 = R5
                elif ins[2]=="R6":
                    r2 = R6

                #3rd register detection
                if ins[3]=="R0":
                    r3 = R0
                elif ins[3]=="R1":
                    r3 = R1
                elif ins[3]=="R2":
                    r3 = R2
                elif ins[3]=="R3":
                    r3 = R3
                elif ins[3]=="R4":
                    r3 = R4
                elif ins[3]=="R5":
                    r3 = R5
                elif ins[3]=="R6":
                    r3 = R6

                OutputFile.append(Multiply(r1, r2, r3));

        else:
            OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error"]
            break
    
    elif ins[0]=="div":
        if len(ins)==3:
           
            if (ins[1] not in all_registers) or (ins[2] not in all_registers):
                OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error, Valid Register not found"]
                break

            else:
                #1st register detection
                if ins[1]=="R0":
                    r1 = R0
                elif ins[1]=="R1":
                    r1 = R1
                elif ins[1]=="R2":
                    r1 = R2
                elif ins[1]=="R3":
                    r1 = R3
                elif ins[1]=="R4":
                    r1 = R4
                elif ins[1]=="R5":
                    r1 = R5
                elif ins[1]=="R6":
                    r1 = R6

                #2nd register detection
                if ins[2]=="R0":
                    r2 = R0
                elif ins[2]=="R1":
                    r2 = R1
                elif ins[2]=="R2":
                    r2 = R2
                elif ins[2]=="R3":
                    r2 = R3
                elif ins[2]=="R4":
                    r2 = R4
                elif ins[2]=="R5":
                    r2 = R5
                elif ins[2]=="R6":
                    r2 = R6

            OutputFile.append(Divide(r1, r2))

        else:
            OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error"]
            break

    elif ins[0]=="rs":
        if len(ins)==3:
           
            if (ins[1] not in all_registers):
                OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error, Valid Register not found"]
                break

            else:
                #1st register detection
                if ins[1]=="R0":
                    r1 = R0
                elif ins[1]=="R1":
                    r1 = R1
                elif ins[1]=="R2":
                    r1 = R2
                elif ins[1]=="R3":
                    r1 = R3
                elif ins[1]=="R4":
                    r1 = R4
                elif ins[1]=="R5":
                    r1 = R5
                elif ins[1]=="R6":
                    r1 = R6

            if (ins[2])[0]=="$":  #this is detection of imm
                x = int(ins[2][1:])
                if x<0 or x>255:
                    OutputFile = ["Error in line number: " + str(instr+1) + "; Illegal Immediate values"]
                    break
                else:
                    OutputFile.append(Right_Shift(r1, x))
                    continue
            else:
                OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax error"]
                break

        else:
            OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax error"]
            break
    
    elif ins[0]=="ls":
        if len(ins)==3:
           
            if (ins[1] not in all_registers):
                OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error, Valid Register not found"]
                break

            else:
                #1st register detection
                if ins[1]=="R0":
                    r1 = R0
                elif ins[1]=="R1":
                    r1 = R1
                elif ins[1]=="R2":
                    r1 = R2
                elif ins[1]=="R3":
                    r1 = R3
                elif ins[1]=="R4":
                    r1 = R4
                elif ins[1]=="R5":
                    r1 = R5
                elif ins[1]=="R6":
                    r1 = R6

            if (ins[2])[0]=="$":  #this is detection of imm
                x = int(ins[2][1:])
                if x<0 or x>255:
                    OutputFile = ["Error in line number: " + str(instr+1) + "; Illegal Immediate values"]
                    break
                else:
                    OutputFile.append(Left_Shift(r1, x))
                    continue
            else:
                OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax error"]
                break

        else:
            OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax error"]
            break
    
    elif ins[0]=="xor":
        if len(ins)==4:
           
            if (ins[1] not in all_registers) or (ins[2] not in all_registers) or (ins[3] not in all_registers):
                OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error, Valid Register not found"]
                break

            else:
                #1st register detection
                if ins[1]=="R0":
                    r1 = R0
                elif ins[1]=="R1":
                    r1 = R1
                elif ins[1]=="R2":
                    r1 = R2
                elif ins[1]=="R3":
                    r1 = R3
                elif ins[1]=="R4":
                    r1 = R4
                elif ins[1]=="R5":
                    r1 = R5
                elif ins[1]=="R6":
                    r1 = R6

                #2nd register detection
                if ins[2]=="R0":
                    r2 = R0
                elif ins[2]=="R1":
                    r2 = R1
                elif ins[2]=="R2":
                    r2 = R2
                elif ins[2]=="R3":
                    r2 = R3
                elif ins[2]=="R4":
                    r2 = R4
                elif ins[2]=="R5":
                    r2 = R5
                elif ins[2]=="R6":
                    r2 = R6

                #3rd register detection
                if ins[3]=="R0":
                    r3 = R0
                elif ins[3]=="R1":
                    r3 = R1
                elif ins[3]=="R2":
                    r3 = R2
                elif ins[3]=="R3":
                    r3 = R3
                elif ins[3]=="R4":
                    r3 = R4
                elif ins[3]=="R5":
                    r3 = R5
                elif ins[3]=="R6":
                    r3 = R6

                OutputFile.append(XOR(r1, r2, r3));

        else:
            OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax error"]
            break

    elif ins[0]=="or":
        if len(ins)==4:
           
            if (ins[1] not in all_registers) or (ins[2] not in all_registers) or (ins[3] not in all_registers):
                OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error, Valid Register not found"]
                break

            else:
                #1st register detection
                if ins[1]=="R0":
                    r1 = R0
                elif ins[1]=="R1":
                    r1 = R1
                elif ins[1]=="R2":
                    r1 = R2
                elif ins[1]=="R3":
                    r1 = R3
                elif ins[1]=="R4":
                    r1 = R4
                elif ins[1]=="R5":
                    r1 = R5
                elif ins[1]=="R6":
                    r1 = R6

                #2nd register detection
                if ins[2]=="R0":
                    r2 = R0
                elif ins[2]=="R1":
                    r2 = R1
                elif ins[2]=="R2":
                    r2 = R2
                elif ins[2]=="R3":
                    r2 = R3
                elif ins[2]=="R4":
                    r2 = R4
                elif ins[2]=="R5":
                    r2 = R5
                elif ins[2]=="R6":
                    r2 = R6

                #3rd register detection
                if ins[3]=="R0":
                    r3 = R0
                elif ins[3]=="R1":
                    r3 = R1
                elif ins[3]=="R2":
                    r3 = R2
                elif ins[3]=="R3":
                    r3 = R3
                elif ins[3]=="R4":
                    r3 = R4
                elif ins[3]=="R5":
                    r3 = R5
                elif ins[3]=="R6":
                    r3 = R6

                OutputFile.append(OR(r1, r2, r3));

        else:
            OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax error"]
            break

    elif ins[0]=="and":
        if len(ins)==4:
           
            if (ins[1] not in all_registers) or (ins[2] not in all_registers) or (ins[3] not in all_registers):
                OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error, Valid Register not found"]
                break

            else:
                #1st register detection
                if ins[1]=="R0":
                    r1 = R0
                elif ins[1]=="R1":
                    r1 = R1
                elif ins[1]=="R2":
                    r1 = R2
                elif ins[1]=="R3":
                    r1 = R3
                elif ins[1]=="R4":
                    r1 = R4
                elif ins[1]=="R5":
                    r1 = R5
                elif ins[1]=="R6":
                    r1 = R6

                #2nd register detection
                if ins[2]=="R0":
                    r2 = R0
                elif ins[2]=="R1":
                    r2 = R1
                elif ins[2]=="R2":
                    r2 = R2
                elif ins[2]=="R3":
                    r2 = R3
                elif ins[2]=="R4":
                    r2 = R4
                elif ins[2]=="R5":
                    r2 = R5
                elif ins[2]=="R6":
                    r2 = R6

                #3rd register detection
                if ins[3]=="R0":
                    r3 = R0
                elif ins[3]=="R1":
                    r3 = R1
                elif ins[3]=="R2":
                    r3 = R2
                elif ins[3]=="R3":
                    r3 = R3
                elif ins[3]=="R4":
                    r3 = R4
                elif ins[3]=="R5":
                    r3 = R5
                elif ins[3]=="R6":
                    r3 = R6

                OutputFile.append(AND(r1, r2, r3));

        else:
            OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax error"]
            break

    elif ins[0]=="not":
        if len(ins)==3:
           
            if (ins[1] not in all_registers) or (ins[2] not in all_registers):
                OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error, Valid Register not found"]
                break

            else:
                #1st register detection
                if ins[1]=="R0":
                    r1 = R0
                elif ins[1]=="R1":
                    r1 = R1
                elif ins[1]=="R2":
                    r1 = R2
                elif ins[1]=="R3":
                    r1 = R3
                elif ins[1]=="R4":
                    r1 = R4
                elif ins[1]=="R5":
                    r1 = R5
                elif ins[1]=="R6":
                    r1 = R6

                #2nd register detection
                if ins[2]=="R0":
                    r2 = R0
                elif ins[2]=="R1":
                    r2 = R1
                elif ins[2]=="R2":
                    r2 = R2
                elif ins[2]=="R3":
                    r2 = R3
                elif ins[2]=="R4":
                    r2 = R4
                elif ins[2]=="R5":
                    r2 = R5
                elif ins[2]=="R6":
                    r2 = R6

            OutputFile.append(Invert(r1, r2))

        else:
            OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax error"]
            break

    elif ins[0]=="cmp":
        if len(ins)==3:
           
            if (ins[1] not in all_registers) or (ins[2] not in all_registers):
                OutputFile = ["Error in line number: " + str(instr+1) + "; Syntax Error, Valid Register not found"]
                break

            else:
                #1st register detection
                if ins[1]=="R0":
                    r1 = R0
                elif ins[1]=="R1":
                    r1 = R1
                elif ins[1]=="R2":
                    r1 = R2
                elif ins[1]=="R3":
                    r1 = R3
                elif ins[1]=="R4":
                    r1 = R4
                elif ins[1]=="R5":
                    r1 = R5
                elif ins[1]=="R6":
                    r1 = R6

                #2nd register detection
                if ins[2]=="R0":
                    r2 = R0
                elif ins[2]=="R1":
                    r2 = R1
                elif ins[2]=="R2":
                    r2 = R2
                elif ins[2]=="R3":
                    r2 = R3
                elif ins[2]=="R4":
                    r2 = R4
                elif ins[2]=="R5":
                    r2 = R5
                elif ins[2]=="R6":
                    r2 = R6

            OutputFile.append(Compare(r1, r2))

        else:
            OutputFile = ["Error in line number: " + str(instr+1) + "Syntax error"]
            break

    elif ins[0]=="jmp":
        jj = ins[1]

        if jj not in label_dict.keys():
            OutputFile = ["Error in line number: " + str(instr+1) + "; Use of Undefined Labels"]
            break
        else:
            x = label_dict[jj]
            OutputFile.append(Unconditional_Jump(x))
    
    elif ins[0]=="jlt":
        jj = ins[1]

        if jj not in label_dict.keys():
            OutputFile = ["Error in line number: " + str(instr+1) + "; Use of Undefined Labels"]
            break
        else:
            x = label_dict[jj]
            OutputFile.append(Jump_if_Less_Than(x))

    elif ins[0]=="jgt":
        jj = ins[1]

        if jj not in label_dict.keys():
            OutputFile = ["Error in line number: " + str(instr+1) + "; Use of Undefined Labels"]
            break
        else:
            x = label_dict[jj]
            OutputFile.append(Jump_if_Greater_Than(x))

    elif ins[0]=="je":
        jj = ins[1]

        if jj not in label_dict.keys():
            OutputFile = ["Error in line number: " + str(instr+1) + "; Use of Undefined Labels"]
            break
        else:
            x = label_dict[jj]
            OutputFile.append(Jump_if_Equal(x))

    else:
        OutputFile = ["Error in line number: " + str(instr+1) + "; Undefined Instruction"]
        break
     
if len(OutputFile)==1:
    chk = OutputFile[0].split()
    if "Error" in chk:
        print(OutputFile[0])
    elif OutputFile[0]=="1001100000000000":
        print("1001100000000000")
    else:
        print("Error: hlt not present")

elif "1001100000000000" not in OutputFile:
     OutputFile = ["Error: hlt not present"]
     print("Error: hlt not present")

else:
    for bb in OutputFile:     # for printing the Output
        print(bb)
        
