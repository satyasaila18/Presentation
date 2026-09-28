def happy(n):
    if n==1:
        return True
    elif n==4:
        return False
    sum=0
    while n>0:
        dig=n%10
        sum+=(dig*dig)
        n//=10
    return happy(sum)
    

n=int(input("Enter a number "))
res=happy(n)
if res:
    print(f'{n} is a happy number')
else:
    print(f'{n} not a happy number')


#first n happy numbers

m=int(input("Enter rangee : "))
for i in range(1,m+1):
    if happy(i)==True:
        print(i)