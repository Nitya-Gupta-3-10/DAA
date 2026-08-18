arr=[11,22,33,44,55,66,77,88]
key=111
loc=3
arr.append(0)
i=len(arr)-1
while i>=loc:
    arr[i]=arr[i-1]
    i=i-1
arr[loc]=key
print(*arr)
