def add(x,y): #function defination
    res=x+y
    return res
if __name__ == '__main__':
    a=int(input("Enter a :"))
    b=int(input("Enter b:"))
    res=add(a,b)  #Function call
    print("Add = ",res)
