def LinearSearch(arr,target):
    for i in range (len(arr)):
        if arr[i]==target:
            return i
    
    return -1
    



arr=[2,4,1,7,5]
target=7
result=LinearSearch(arr,target)
if result != -1:
    print("Found at index",result)
else:
    print("Not Found")
