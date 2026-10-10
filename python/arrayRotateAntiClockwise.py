
#Anti Clockwise
def RotateAntiClockwise(arr,n):
    l=len(arr)
    for i in range(n):
        first=arr[0]
        for j in range(l-1):
            arr[j]=arr[j+1]
        arr[l-1]=first
    print(arr)

arr=[10,20,30,40,50]

n2=int(input("Enter number of rotates for Anit clock wise..."))
RotateAntiClockwise(arr,n2)
