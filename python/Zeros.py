arr=[0,3,5,1,0,0,3,0]
res=[]
# res2=[]
# for i in range(len(arr)):
#     if arr[i]==0:
#         res.append(arr[i])
#     else:
#         res2.append(arr[i])

# print(res+res2)


# for i in arr:
#     if i ==0:
#         res.insert(0,i)
#     else:
#         res.append(i)
# print(res)

n=len(arr)
j=0
for i in range(n):
    if arr[i]!=0:
        arr[i],arr[j]=arr[j],arr[i]
        j+=1

print(arr)