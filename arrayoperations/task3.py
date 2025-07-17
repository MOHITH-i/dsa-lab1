arr=[5,3,8,1,9];
index=int(input("enter the index"))
arr=arr[:index]+arr[index+1:]
print(arr)