t=(1,2,3,4,5,6,7,8,8,8 , 8 ,8)
print(t.count(8))

print(len(t))
print(t.index(8))

numbers = (1, 2, 3, 4, 2, 5, 2)

# Find '2', but start searching from index 3
print(numbers.index(2, 3))  # Output: 4 (It skips the '2' at index 1)

# Find '2' between index 2 and index 5
print(numbers.index(2, 2, 5))  # Output: 4

b=[1,2,3,4,5]
c=b.append(6)
print(b)
print(c)