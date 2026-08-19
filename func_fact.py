def fc(no):
    fact=1
    while no>0:
        fact=fact*no
        no=no-1
    return fact

if __name__ == '__main__':
    n=int(input("Enter number :"))
    f=fc(n)
    print(f)
