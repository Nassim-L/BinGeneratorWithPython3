import random 

a = []
for x in range (0,10):
    a.append(str(x))

def generatebin(bins):
    b = []
    aa = 0
    gen_len = len(bins)
    
    while aa < (16-gen_len) :
        c = random.choice(a)
        b.append(c)
        aa += 1

    return b

def makebin(bins, b):
    gb = bins
    for xx in b :
        gb = gb + xx


    print(gb)

def updatedbingen(bins):
    binx = []
    i = 0
    for x in bins:
        if x =='x' or x=='X': 
            x = random.choice(a)
            binx.append(x)

        else:
            binx.append(x)


    return binx


def input2x(bins):
    xl = ['x' for x in range(0,16) ]
    i = 0 
    for ii in bins:
        print(ii)
        xl[i]  = ii 
        i += 1 

    return xl

def makebinV2(bins):
    gb = ''
    for xx in bins :
        gb = gb + xx

    print(gb)

        



        
        







    
