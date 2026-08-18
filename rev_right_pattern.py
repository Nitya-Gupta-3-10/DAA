sp=0
for i in range(4,0,-1):
    for k in range(sp):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()
    sp=sp-1
        
