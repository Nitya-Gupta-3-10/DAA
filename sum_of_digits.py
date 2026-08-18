no=int(input("Enter number :"))
sum=0
while no>0:
    n=no%10
    sum=sum+n
    no=no//10
print(sum)
