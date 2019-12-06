for item in 'Python':
    print(item)

for item in ['eggs', 'bacon', 'milk']:
    print(item)

for item in range(10):
    print(item)

for item in range(3, 10):
    print(item)

for item in range(3, 20, 2):
    print(item)

prices = [10, 20, 30]
total = 0
for item in prices:
    total += item
print(f'Your total is: {total}')


#to produce a list of coordinates like 
# (0,1)
# (0,2)
# (0,3)
# (1,1)
# (1,2)
# (1,3)
# (2,1)
# ...

for x in range(4):
    for y in range(4):
        print(f"({x}, {y})")


numbers = [2, 5, 2, 3, 4, 5]

# for x in coordinates:
#     print('x' * x )

for x_count in numbers:
    output = ''
    for x in range(x_count):
        output += 'x'
    print(output)


