ls=[1,2,3,4,5,6]
#map()
doubled=map(lambda x:x*2,ls)
print(list(doubled))

#filter
even=filter(lambda x:x%2==0,ls )
print(list(even))


#same without map and filter
d2=[x*2 for x in ls]
print(d2)

e2=[x for x in ls if x%2==0]
print(e2)

#combination
ed=[x*2 for x in ls if x%2==0]
print(ed)