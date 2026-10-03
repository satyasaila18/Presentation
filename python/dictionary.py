d={'s':'satya','n':'naga','d':'durga','p':'prasad'}
print(d)
print(type(d))
print(d['s'])
print(d.keys())
print(d.values())
print(d.items())


#iterating dictinary

for key in d:
    print(key)  #prints key

for val in d.values():
    print(val)  #Valuess


for k,v in d.items():
    print(f'{k} : {v}')   #Keys and values