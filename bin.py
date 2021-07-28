import random 

a = []
for x in range (0,10):
    a.append(str(x))


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
        xl[i]  = ii 
        i += 1 

    return xl

def makebinV2(bins):
    gb = ''
    for xx in bins :
        gb = gb + xx

    print(gb)

        



        
        







    
