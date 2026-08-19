n=int(input())
arr=list(map(int,input().split()))
loc=int(input())
for i in range (loc+1,len(arr)):
    arr[i-1]=arr[i]
arr.pop()
print(*arr)
