customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer['name'])
print(customer.get('name'))
print(customer.get('birthdate', 'jan 1 2019'))

user_input = input('Phone: ')

numbers = {
    '1': "one",
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}

output = ''
for number in user_input:
    output += numbers.get(number) + ' '
print(output)


message = input('>')
words = message.split()
smile = {
    ':)': '😀',
    '):': '☹️'
}
output = ''
for word in words:
   output += smile.get(word, word) + ' '
print(output)



