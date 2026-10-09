arr=[10,20,30,40,50,60,70]
target=60
h=len(arr)-1
l=0
while h>l:
    mid=(h+l)//2
    if target==arr[mid]:
        print(f"Target element found at index {mid}")
        break
    elif target>arr[mid]:
        l=mid+1
    elif target<arr[mid]:
        h=mid-1
else:
    print("404!")

