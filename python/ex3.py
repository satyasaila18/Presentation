def Count_nums(n):
    count=0
    while n:
        count+=1
        n//=10
    return count

def ArmStrong(n,m):
    sum=0
    temp=n
    while n:
        dig=n%10
        sum+=dig**m
        n//=10
    return temp==sum

n=int(input("Enter a Number>.."))
count=Count_nums(n)
res=ArmStrong(n,count)

if res:
    print(f'{n} is an ArmStrong Number')
else:
    print(f'{n} is not an ArmStrong Number')