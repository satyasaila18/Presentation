arr=[10,20,30,40,50]
l=len(arr)
n=int(input("Enter number of rotates..."))
for i in range(n):
    last=arr[l-1]
    for j in range(l-1,0,-1):
        arr[j]=arr[j-1]
    arr[0]=last
print(arr)