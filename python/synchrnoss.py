import random
arr=[1,2,3,4,4,51,9,33,0,999]
mx=arr[0]
for i in range(len(arr)):
    if arr[i]>mx:
        mx=arr[i]

print(f'maximum number is {mx}')



s='madam'
rev=''
for i in s:
    rev=rev+i

if rev==s:
    print("Palindrome..")
else:
    print("Not a palindrome")


s='Satya'
s=55
print(s)

digi=random.randint(1,100)
print(digi)