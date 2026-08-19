arr=[111,21,45,76,8]
max=arr[0]
for i in range(1,len(arr)):
    if max<arr[i]:
        max=arr[i]
print(max)
