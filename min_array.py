arr=[111,21,45,76,8]
min=arr[0]
for i in range(1,len(arr)):
    if min>arr[i]:
        min=arr[i]
print(min)
