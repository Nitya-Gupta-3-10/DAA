no=int(input())
save=no
while no>0:
    rem=no%10
    rev=rev*10+rem
    no=no//10
if save==rev:
    print("Palindrome")
else:
    print("Not Palindrome")
