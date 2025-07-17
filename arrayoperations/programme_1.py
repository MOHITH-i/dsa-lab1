#printing all the elements (traverse)
arr=[5,3,8,1,9]
for x in arr:
    print(x,end=" ")
#insering at the index by slicing 
element=7
index=2
arr=arr[:index]+[element]+arr[index:]
print("\n")
print(arr)
#deleting
index=1
arr=arr[:index]+arr[index+1:]
print(arr)
#searching
target=8;
for i in range(5):
    if (arr[i]==target):
        print(i)
    else:
        print(-1)
#update
arr=[5,3,8,1,9]
arr[3]=4
print(arr)        