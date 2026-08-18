arr=[11,2,3,76,90,80,88]
print(arr)
print(*arr)
for i in range(len(arr)):
    print(arr[i],end=" ")
print()
for i in range(len(arr)-1,-1,-1):
    print(arr[i],end=" ")
