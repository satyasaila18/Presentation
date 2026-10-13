s=input("Enter a String: ")
freq={}
for i in s:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

print(freq)
for i,j in freq.items():
    if j==1:
        print(i)