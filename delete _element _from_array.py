arr=[12,21,13,45,51,16,27]
loc=3
for i in range (loc+1,len(arr)):
    arr[i-1]=arr[i]
arr.pop()
print(*arr)
