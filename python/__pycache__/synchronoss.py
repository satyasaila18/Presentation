arr1=[1,2,3,4,]
arr2=[3,5,2]
res=[x for x in arr1 if x not in arr2]
print(res)

print(set(arr1)-set(arr2))

