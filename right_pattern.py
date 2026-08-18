sp=5
for i in range(1,5):
    for k in range(sp):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()
    sp=sp-1
