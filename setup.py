import bin
x = input('put your bins here')
n = int(input("number of generated bins"))
sx = bin.input2x(x)
print(sx)
for sp in range(0,n):
    bm = bin.updatedbingen(sx)
    bin.makebinV2(bm)











