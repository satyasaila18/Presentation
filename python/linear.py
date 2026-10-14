arr=[10,20,30,40,50,99]
target=50
for i in range(len(arr)):
    if arr[i]==target:
        print(f'target element {target} found at index {i}')
        break
else:
    print("404!..")