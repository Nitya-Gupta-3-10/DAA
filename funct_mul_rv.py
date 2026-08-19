def add(x,y): #function defination
    res1=x+y
    res2=x-y
    res3=x*y
    return res1,res2,res3
if __name__ == '__main__':
    a=int(input("Enter a :"))
    b=int(input("Enter b:"))
    r1,r2,r3=add(a,b)  #Function call
    print("Add = ",r1)
    print("Sub = ",r2)
    print("Mul = ",r3)
