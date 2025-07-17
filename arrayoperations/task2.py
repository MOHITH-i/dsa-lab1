arr=[5,3,8,1,9]
element=7
index=2
arr=arr[:index]+[element]+arr[index:]
print(arr)