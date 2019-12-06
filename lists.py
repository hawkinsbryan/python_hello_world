names = ['Bryan', 'Mary', 'Devon', 'Yoshi', 'George']
names[0] = 'bhawk'
print(names[3])
print(names)

numbers = [3, 4, 8, 6, 3, 1, 3, 900, 4]
maximum = numbers[0]

for x in numbers:
    if x > maximum:
        maximum = x
print(maximum)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][2])

for row in matrix:
    for item in row:
        print(item)


numbers = [3, 4, 8, 6, 3, 1, 3, 900, 4]
numbers_copy = numbers.copy()
numbers.insert(4, 50)
numbers.append(1000)
numbers.remove(8)
print(numbers)
print(900 in numbers)
print(numbers.count(3))
numbers.sort()
print(numbers)
print(numbers_copy)



#create a new array with no duplicates
number_array = [2, 3, 5, 8, 4, 3, 1, 2, 3, 2, 2]
uniques = []
for x in number_array:
    if x not in uniques:
        uniques.append(x)


print(number_array)
print(uniques)

