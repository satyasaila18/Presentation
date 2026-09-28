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