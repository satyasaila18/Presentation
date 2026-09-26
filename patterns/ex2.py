print("T1 ======================================")
#triangle
for i in range(n+1):
    for j in range(i+1):
        print("*",end='')
    print()

#T2
print("T2++++++++++++++++++++++++++++++++")
for i in range(n+1,0,-1):
    for j in range(i,0,-1):
        print("*",end='')
    print()

#T3
print("T3========================================")
for i in range(n+1):
    for j in range(1,n-i+1,1):
        print(" ",end='')
    for k in range(1,i+1):
        print("*",end='')
    print()
