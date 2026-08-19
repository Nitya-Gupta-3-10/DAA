arr=list(map(int,input().split()))
min=arr[0]
for i in range(1,len(arr)):
    if min>arr[i]:
        min=arr[i]
print(min)
