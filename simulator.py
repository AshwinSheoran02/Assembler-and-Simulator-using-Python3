import sys
import numpy as np
import matplotlib.pyplot as plt

class Register:
    # address is a 3 bit string
    def __init__(self, address):
        self.value = 0;
        self.address = address

    def addr(self):
        return self.address

    def val(self):
        return self.value

class Flag_Register:
    # v, l, g, e are always 0 or 1
    def __init__(self) -> None:
        self.v = 0
        self.l = 0
        self.g = 0
        self.e = 0

    def val(self):
        return "0"*12 + str(self.v) + str(self.l) + str(self.g) + str(self.e)

    def addr(self):
        return "111"

    def reset(self):
        self.v = 0
        self.l = 0
        self.g = 0
        self.e = 0



def convert_int_to_bin(n, ln):
    # n is an integer, length of the binary 
    bnr = bin(n)
    bnr = bnr.replace('0b','')
    while len(bnr)<ln:
        bnr = "0" + bnr

    return bnr 

def convert_bin_to_int(s):
    # s is always 8 bit binary
    return int(s, 2)



global R0;
global R1;
global R2;
global R3;
global R4;
global R5;
global R6;
global FLAGS;
global Variable_dict;

R0 = Register("000")
R1 = Register("001")
R2 = Register("010")
R3 = Register("011")
R4 = Register("100")
R5 = Register("101")
R6 = Register("110")
FLAGS = Flag_Register()
Variable_dict = {}

def printer(prog_count):
    # prog_count is a integer that is the line number;

    prg = convert_int_to_bin(prog_count, 8)

    r0 = convert_int_to_bin(R0.val(), 16)
    r1 = convert_int_to_bin(R1.val(), 16)
    r2 = convert_int_to_bin(R2.val(), 16)
    r3 = convert_int_to_bin(R3.val(), 16)
    r4 = convert_int_to_bin(R4.val(), 16)
    r5 = convert_int_to_bin(R5.val(), 16)
    r6 = convert_int_to_bin(R6.val(), 16)
    flg = FLAGS.val()

    return [prg, r0, r1, r2, r3, r4, r5, r6, flg]

def Addition(r1, r2, r3):
    FLAGS.reset()
    x = r2.val() + r3.val()

    if x>65535:
        FLAGS.v = 1
        binx = convert_int_to_bin(x, 17)
        binx = binx[1:17]
        nx = convert_bin_to_int(binx)
        r1.value = nx
    
    else:
        #FLAGS.reset()
        r1.value = x
    

def Subtraction(r1, r2, r3):
    FLAGS.reset()
    x = r2.val() - r3.val()

    if x<0:
        r1.value = 0
        FLAGS.v = 1

    else:
        FLAGS.reset()
        r1.value = x

def Move_Immidiate(r1, imm):
    # imm is 8 bit value binary
    x = convert_bin_to_int(imm)
    r1.value = x
    FLAGS.reset()

def Move_Register(r1, r2):
    if r2==FLAGS:
        r1.value = convert_bin_to_int(FLAGS.val())
    else:
        r1.value = r2.val()

    FLAGS.reset()

def Load(r1, mem):
    # mem is 8 bit string
    if mem in Variable_dict.keys():
        xn = Variable_dict[mem]
    else:
        Variable_dict[mem] = 0
        xn = Variable_dict[mem]

    r1.value = xn 
    FLAGS.reset()

def Store(r1, mem):
    # mem is 8 bit value binary
    if mem in Variable_dict.keys():
        Variable_dict[mem] = r1.val()
    else:
        Variable_dict[mem] = r1.val()
    
    FLAGS.reset()

def Multiply(r1, r2, r3):
    FLAGS.reset()
    x = (r2.val())*(r3.val())

    if x>65535:
        FLAGS.v = 1
        binx = convert_int_to_bin(x, 32)
        binx = binx[16:32]
        nx = convert_bin_to_int(binx)
        r1.value = nx
    
    else:
        #FLAGS.reset()
        r1.value = x

def Divide(r3, r4):
    R0.value, R1.value = (r3.val()//r4.val()), (r3.val()%r4.val()) 
    FLAGS.reset()

def Right_Shift(r1, imm):
    # imm is a 8 bit string
    xn = convert_bin_to_int(imm)
    x = convert_int_to_bin(r1.val(), 16)
    x = "0"*xn + x
    x = x[0:16]
    r1.value = convert_bin_to_int(x)
    FLAGS.reset()

def Left_Shift(r1, imm):
    # imm is a 8 bit string
    xn = convert_bin_to_int(imm)
    x = convert_int_to_bin(r1.val(), 16)
    x = x + "0"*xn
    x = x[len(x)-16:len(x)]
    r1.value = convert_bin_to_int(x)
    FLAGS.reset()

def XOR(r1, r2, r3):
    r1.value = (r2.val())^(r3.val())
    FLAGS.reset()

def OR(r1, r2, r3):
    r1.value = (r2.val())|(r3.val())
    FLAGS.reset()

def AND(r1, r2, r3):
    r1.value = (r2.val())&(r3.val())
    FLAGS.reset()

def Invert(r1, r2):
    xs = convert_int_to_bin(r2.val(), 16)
    xso = ""

    for i in range(16):
        if xs[i]=="0":
            xso = xso + "1"
        else:
            xso = xso + "0"
    
    r1.value = convert_bin_to_int(xso)

    FLAGS.reset()

def Compare(r1, r2):
    FLAGS.reset()
    if r1.val()<r2.val():
        FLAGS.l = 1
    elif r1.val()>r2.val():
        FLAGS.g = 1
    else:
        FLAGS.e = 1

# def Unconditional_Jump(mem):
#     pass

# def Jump_if_less_than(mem):
#     pass

# def Jump_if_greater_than(mem):
#     pass

# def Jump_if_equal(mem):
#     pass


# main function starts here
global plot_points_x;
global plot_points_y;

plot_points_x = [];
plot_points_y = [];

prg_count = 0

instructions = sys.stdin.readlines();

halted = False

cycle_no = 0

while (not halted):
    plot_points_x.append(cycle_no)
    plot_points_y.append(prg_count)
    cycle_no += 1
    instr = instructions[prg_count]
    if (instr=="1001100000000000"):
        FLAGS.reset();
        crnt_prnt = printer(prg_count)
        print(*crnt_prnt)
        #FLAGS.reset()
        halted = True
        break 

    elif (instr[0:5] == "00000"):
        rg1 = instr[7:10]
        rg2 = instr[10:13]
        rg3 = instr[13:16]

        # detecting rg1
        if rg1==R0.addr():
            r1 = R0
        elif rg1==R1.addr():
            r1 = R1
        elif rg1==R2.addr():
            r1 = R2
        elif rg1==R3.addr():
            r1 = R3
        elif rg1==R4.addr():
            r1 = R4
        elif rg1==R5.addr():
            r1 = R5
        elif rg1==R6.addr():
            r1 = R6

        # detecting rg2
        if rg2==R0.addr():
            r2 = R0
        elif rg2==R1.addr():
            r2 = R1
        elif rg2==R2.addr():
            r2 = R2
        elif rg2==R3.addr():
            r2 = R3
        elif rg2==R4.addr():
            r2 = R4
        elif rg2==R5.addr():
            r2 = R5
        elif rg2==R6.addr():
            r2 = R6

        # detecting rg3
        if rg3==R0.addr():
            r3 = R0
        elif rg3==R1.addr():
            r3 = R1
        elif rg3==R2.addr():
            r3 = R2
        elif rg3==R3.addr():
            r3 = R3
        elif rg3==R4.addr():
            r3 = R4
        elif rg3==R5.addr():
            r3 = R5
        elif rg3==R6.addr():
            r3 = R6

        Addition(r1, r2, r3)

        crnt_prnt = printer(prg_count)
        print(*crnt_prnt)
    
    elif (instr[0:5] == "00001"):
        rg1 = instr[7:10]
        rg2 = instr[10:13]
        rg3 = instr[13:16]

        # detecting rg1
        if rg1==R0.addr():
            r1 = R0
        elif rg1==R1.addr():
            r1 = R1
        elif rg1==R2.addr():
            r1 = R2
        elif rg1==R3.addr():
            r1 = R3
        elif rg1==R4.addr():
            r1 = R4
        elif rg1==R5.addr():
            r1 = R5
        elif rg1==R6.addr():
            r1 = R6

        # detecting rg2
        if rg2==R0.addr():
            r2 = R0
        elif rg2==R1.addr():
            r2 = R1
        elif rg2==R2.addr():
            r2 = R2
        elif rg2==R3.addr():
            r2 = R3
        elif rg2==R4.addr():
            r2 = R4
        elif rg2==R5.addr():
            r2 = R5
        elif rg2==R6.addr():
            r2 = R6

        # detecting rg3
        if rg3==R0.addr():
            r3 = R0
        elif rg3==R1.addr():
            r3 = R1
        elif rg3==R2.addr():
            r3 = R2
        elif rg3==R3.addr():
            r3 = R3
        elif rg3==R4.addr():
            r3 = R4
        elif rg3==R5.addr():
            r3 = R5
        elif rg3==R6.addr():
            r3 = R6

        Subtraction(r1, r2, r3)

        crnt_prnt = printer(prg_count)
        print(*crnt_prnt)
    
    elif (instr[0:5]=="00010"):
        rg1 = instr[5:8]

        # detecting rg1
        if rg1==R0.addr():
            r1 = R0
        elif rg1==R1.addr():
            r1 = R1
        elif rg1==R2.addr():
            r1 = R2
        elif rg1==R3.addr():
            r1 = R3
        elif rg1==R4.addr():
            r1 = R4
        elif rg1==R5.addr():
            r1 = R5
        elif rg1==R6.addr():
            r1 = R6

        Move_Immidiate(r1, instr[8:16])

        crnt_prnt = printer(prg_count)
        print(*crnt_prnt)

    elif (instr[0:5]=="00011"):
        rg1 = instr[10:13]
        rg2 = instr[13:16]

        # detecting rg1
        if rg1==R0.addr():
            r1 = R0
        elif rg1==R1.addr():
            r1 = R1
        elif rg1==R2.addr():
            r1 = R2
        elif rg1==R3.addr():
            r1 = R3
        elif rg1==R4.addr():
            r1 = R4
        elif rg1==R5.addr():
            r1 = R5
        elif rg1==R6.addr():
            r1 = R6

        # detecting rg2
        if rg2==R0.addr():
            r2 = R0
        elif rg2==R1.addr():
            r2 = R1
        elif rg2==R2.addr():
            r2 = R2
        elif rg2==R3.addr():
            r2 = R3
        elif rg2==R4.addr():
            r2 = R4
        elif rg2==R5.addr():
            r2 = R5
        elif rg2==R6.addr():
            r2 = R6
        elif rg2==FLAGS.addr():
            r2 = FLAGS

        Move_Register(r1, r2)

        crnt_prnt = printer(prg_count)
        print(*crnt_prnt)

    elif (instr[0:5]=="00100"):
        rg1 = instr[5:8]

        # detecting rg1
        if rg1==R0.addr():
            r1 = R0
        elif rg1==R1.addr():
            r1 = R1
        elif rg1==R2.addr():
            r1 = R2
        elif rg1==R3.addr():
            r1 = R3
        elif rg1==R4.addr():
            r1 = R4
        elif rg1==R5.addr():
            r1 = R5
        elif rg1==R6.addr():
            r1 = R6

        Load(r1, instr[8:16])

        crnt_prnt = printer(prg_count)
        print(*crnt_prnt)

    elif (instr[0:5]=="00101"):
        rg1 = instr[5:8]

        # detecting rg1
        if rg1==R0.addr():
            r1 = R0
        elif rg1==R1.addr():
            r1 = R1
        elif rg1==R2.addr():
            r1 = R2
        elif rg1==R3.addr():
            r1 = R3
        elif rg1==R4.addr():
            r1 = R4
        elif rg1==R5.addr():
            r1 = R5
        elif rg1==R6.addr():
            r1 = R6

        Store(r1, instr[8:16])

        crnt_prnt = printer(prg_count)
        print(*crnt_prnt)

    elif (instr[0:5] == "00110"):
        rg1 = instr[7:10]
        rg2 = instr[10:13]
        rg3 = instr[13:16]

        # detecting rg1
        if rg1==R0.addr():
            r1 = R0
        elif rg1==R1.addr():
            r1 = R1
        elif rg1==R2.addr():
            r1 = R2
        elif rg1==R3.addr():
            r1 = R3
        elif rg1==R4.addr():
            r1 = R4
        elif rg1==R5.addr():
            r1 = R5
        elif rg1==R6.addr():
            r1 = R6

        # detecting rg2
        if rg2==R0.addr():
            r2 = R0
        elif rg2==R1.addr():
            r2 = R1
        elif rg2==R2.addr():
            r2 = R2
        elif rg2==R3.addr():
            r2 = R3
        elif rg2==R4.addr():
            r2 = R4
        elif rg2==R5.addr():
            r2 = R5
        elif rg2==R6.addr():
            r2 = R6

        # detecting rg3
        if rg3==R0.addr():
            r3 = R0
        elif rg3==R1.addr():
            r3 = R1
        elif rg3==R2.addr():
            r3 = R2
        elif rg3==R3.addr():
            r3 = R3
        elif rg3==R4.addr():
            r3 = R4
        elif rg3==R5.addr():
            r3 = R5
        elif rg3==R6.addr():
            r3 = R6

        Multiply(r1, r2, r3)

        crnt_prnt = printer(prg_count)
        print(*crnt_prnt)

    elif (instr[0:5]=="00111"):
        rg3 = instr[10:13]
        rg4 = instr[13:16]

        # detecting rg3
        if rg3==R0.addr():
            r3 = R0
        elif rg3==R1.addr():
            r3 = R1
        elif rg3==R2.addr():
            r3 = R2
        elif rg3==R3.addr():
            r3 = R3
        elif rg3==R4.addr():
            r3 = R4
        elif rg3==R5.addr():
            r3 = R5
        elif rg3==R6.addr():
            r3 = R6

        # detecting rg4
        if rg4==R0.addr():
            r4 = R0
        elif rg4==R1.addr():
            r4 = R1
        elif rg4==R2.addr():
            r4 = R2
        elif rg4==R3.addr():
            r4 = R3
        elif rg4==R4.addr():
            r4 = R4
        elif rg4==R5.addr():
            r4 = R5
        elif rg4==R6.addr():
            r4 = R6

        Divide(r3, r4)

        crnt_prnt = printer(prg_count)
        print(*crnt_prnt)

    elif (instr[0:5]=="01000"):
        rg1 = instr[5:8]

        # detecting rg1
        if rg1==R0.addr():
            r1 = R0
        elif rg1==R1.addr():
            r1 = R1
        elif rg1==R2.addr():
            r1 = R2
        elif rg1==R3.addr():
            r1 = R3
        elif rg1==R4.addr():
            r1 = R4
        elif rg1==R5.addr():
            r1 = R5
        elif rg1==R6.addr():
            r1 = R6

        Right_Shift(r1, instr[8:16])

        crnt_prnt = printer(prg_count)
        print(*crnt_prnt)

    elif (instr[0:5]=="01001"):
        rg1 = instr[5:8]

        # detecting rg1
        if rg1==R0.addr():
            r1 = R0
        elif rg1==R1.addr():
            r1 = R1
        elif rg1==R2.addr():
            r1 = R2
        elif rg1==R3.addr():
            r1 = R3
        elif rg1==R4.addr():
            r1 = R4
        elif rg1==R5.addr():
            r1 = R5
        elif rg1==R6.addr():
            r1 = R6

        Left_Shift(r1, instr[8:16])

        crnt_prnt = printer(prg_count)
        print(*crnt_prnt)

    elif (instr[0:5]=="01010"):
        rg1 = instr[7:10]
        rg2 = instr[10:13]
        rg3 = instr[13:16]

        # detecting rg1
        if rg1==R0.addr():
            r1 = R0
        elif rg1==R1.addr():
            r1 = R1
        elif rg1==R2.addr():
            r1 = R2
        elif rg1==R3.addr():
            r1 = R3
        elif rg1==R4.addr():
            r1 = R4
        elif rg1==R5.addr():
            r1 = R5
        elif rg1==R6.addr():
            r1 = R6

        # detecting rg2
        if rg2==R0.addr():
            r2 = R0
        elif rg2==R1.addr():
            r2 = R1
        elif rg2==R2.addr():
            r2 = R2
        elif rg2==R3.addr():
            r2 = R3
        elif rg2==R4.addr():
            r2 = R4
        elif rg2==R5.addr():
            r2 = R5
        elif rg2==R6.addr():
            r2 = R6

        # detecting rg3
        if rg3==R0.addr():
            r3 = R0
        elif rg3==R1.addr():
            r3 = R1
        elif rg3==R2.addr():
            r3 = R2
        elif rg3==R3.addr():
            r3 = R3
        elif rg3==R4.addr():
            r3 = R4
        elif rg3==R5.addr():
            r3 = R5
        elif rg3==R6.addr():
            r3 = R6

        XOR(r1, r2, r3)

        crnt_prnt = printer(prg_count)
        print(*crnt_prnt)

    elif (instr[0:5]=="01011"):
        rg1 = instr[7:10]
        rg2 = instr[10:13]
        rg3 = instr[13:16]

        # detecting rg1
        if rg1==R0.addr():
            r1 = R0
        elif rg1==R1.addr():
            r1 = R1
        elif rg1==R2.addr():
            r1 = R2
        elif rg1==R3.addr():
            r1 = R3
        elif rg1==R4.addr():
            r1 = R4
        elif rg1==R5.addr():
            r1 = R5
        elif rg1==R6.addr():
            r1 = R6

        # detecting rg2
        if rg2==R0.addr():
            r2 = R0
        elif rg2==R1.addr():
            r2 = R1
        elif rg2==R2.addr():
            r2 = R2
        elif rg2==R3.addr():
            r2 = R3
        elif rg2==R4.addr():
            r2 = R4
        elif rg2==R5.addr():
            r2 = R5
        elif rg2==R6.addr():
            r2 = R6

        # detecting rg3
        if rg3==R0.addr():
            r3 = R0
        elif rg3==R1.addr():
            r3 = R1
        elif rg3==R2.addr():
            r3 = R2
        elif rg3==R3.addr():
            r3 = R3
        elif rg3==R4.addr():
            r3 = R4
        elif rg3==R5.addr():
            r3 = R5
        elif rg3==R6.addr():
            r3 = R6

        OR(r1, r2, r3)

        crnt_prnt = printer(prg_count)
        print(*crnt_prnt)

    elif (instr[0:5]=="01100"):
        rg1 = instr[7:10]
        rg2 = instr[10:13]
        rg3 = instr[13:16]

        # detecting rg1
        if rg1==R0.addr():
            r1 = R0
        elif rg1==R1.addr():
            r1 = R1
        elif rg1==R2.addr():
            r1 = R2
        elif rg1==R3.addr():
            r1 = R3
        elif rg1==R4.addr():
            r1 = R4
        elif rg1==R5.addr():
            r1 = R5
        elif rg1==R6.addr():
            r1 = R6

        # detecting rg2
        if rg2==R0.addr():
            r2 = R0
        elif rg2==R1.addr():
            r2 = R1
        elif rg2==R2.addr():
            r2 = R2
        elif rg2==R3.addr():
            r2 = R3
        elif rg2==R4.addr():
            r2 = R4
        elif rg2==R5.addr():
            r2 = R5
        elif rg2==R6.addr():
            r2 = R6

        # detecting rg3
        if rg3==R0.addr():
            r3 = R0
        elif rg3==R1.addr():
            r3 = R1
        elif rg3==R2.addr():
            r3 = R2
        elif rg3==R3.addr():
            r3 = R3
        elif rg3==R4.addr():
            r3 = R4
        elif rg3==R5.addr():
            r3 = R5
        elif rg3==R6.addr():
            r3 = R6

        AND(r1, r2, r3)

        crnt_prnt = printer(prg_count)
        print(*crnt_prnt)

    elif (instr[0:5]=="01101"):
        rg1 = instr[10:13]
        rg2 = instr[13:16]

        # detecting rg1
        if rg1==R0.addr():
            r1 = R0
        elif rg1==R1.addr():
            r1 = R1
        elif rg1==R2.addr():
            r1 = R2
        elif rg1==R3.addr():
            r1 = R3
        elif rg1==R4.addr():
            r1 = R4
        elif rg1==R5.addr():
            r1 = R5
        elif rg1==R6.addr():
            r1 = R6

        # detecting rg2
        if rg2==R0.addr():
            r2 = R0
        elif rg2==R1.addr():
            r2 = R1
        elif rg2==R2.addr():
            r2 = R2
        elif rg2==R3.addr():
            r2 = R3
        elif rg2==R4.addr():
            r2 = R4
        elif rg2==R5.addr():
            r2 = R5
        elif rg2==R6.addr():
            r2 = R6

        Invert(r1, r2)

        crnt_prnt = printer(prg_count)
        print(*crnt_prnt)

    elif (instr[0:5]=="01110"):
        rg1 = instr[10:13]
        rg2 = instr[13:16]

        # detecting rg1
        if rg1==R0.addr():
            r1 = R0
        elif rg1==R1.addr():
            r1 = R1
        elif rg1==R2.addr():
            r1 = R2
        elif rg1==R3.addr():
            r1 = R3
        elif rg1==R4.addr():
            r1 = R4
        elif rg1==R5.addr():
            r1 = R5
        elif rg1==R6.addr():
            r1 = R6

        # detecting rg2
        if rg2==R0.addr():
            r2 = R0
        elif rg2==R1.addr():
            r2 = R1
        elif rg2==R2.addr():
            r2 = R2
        elif rg2==R3.addr():
            r2 = R3
        elif rg2==R4.addr():
            r2 = R4
        elif rg2==R5.addr():
            r2 = R5
        elif rg2==R6.addr():
            r2 = R6
        elif rg2==FLAGS.addr():
            r2 = FLAGS

        Compare(r1, r2)

        crnt_prnt = printer(prg_count)
        print(*crnt_prnt)

    elif (instr[0:5]=="01111"):
        FLAGS.reset()
        crnt_prnt = printer(prg_count)
        print(*crnt_prnt)

        prg_count = convert_bin_to_int(instr[8:16])
        continue

    elif (instr[0:5]=="10000"):
        
        if (FLAGS.l == 1):
            FLAGS.reset()
            crnt_prnt = printer(prg_count)
            print(*crnt_prnt)

            prg_count = convert_bin_to_int(instr[8:16])
            continue

        else:
            FLAGS.reset()
            crnt_prnt = printer(prg_count)
            print(*crnt_prnt)

            prg_count += 1;
            continue

    elif (instr[0:5]=="10001"):

        if (FLAGS.g == 1):
            FLAGS.reset()
            crnt_prnt = printer(prg_count)
            print(*crnt_prnt)

            prg_count = convert_bin_to_int(instr[8:16])
            continue
            
        else:
            FLAGS.reset()
            crnt_prnt = printer(prg_count)
            print(*crnt_prnt)

            prg_count += 1;
            continue

    elif (instr[0:5]=="10010"):

        if (FLAGS.e == 1):
            FLAGS.reset()
            crnt_prnt = printer(prg_count)
            print(*crnt_prnt)

            prg_count = convert_bin_to_int(instr[8:16])
            continue
        else:
            FLAGS.reset()
            crnt_prnt = printer(prg_count)
            print(*crnt_prnt)

            prg_count += 1;
            continue

    prg_count += 1; 

# global remain_lines;
global variable_mem_list;

remain_lines = 256 - len(instructions)

for instr in instructions:
    print(instr[0:16])
    # remain_lines -= 1

variable_mem_list = list(Variable_dict.keys())
variable_mem_list.sort()

for mem_addr in variable_mem_list:
    xn = convert_int_to_bin(Variable_dict[mem_addr], 16)
    print(xn)
    remain_lines -=1

for i in range(remain_lines):
    print("0"*16)


# plotting code
x_points = np.array(plot_points_x)
y_points = np.array(plot_points_y)

plt.scatter(x_points, y_points)

plt.xlabel("Cycle Number")
plt.ylabel("Memory Address")

plt.show()



    

