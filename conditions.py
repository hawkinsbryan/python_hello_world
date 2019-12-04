# if its hot
#     its a hot day
#     drink plenty of water
# otherwise if its cold
#     its a cold day
#     wear warm clothes
# otherwise
#     its a lovely day

is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("wear warm clothes")
else:
    print("It's a lovely day")

# price of house is 1million dollars
# if buyer has good credit they need to put down 10%
# if buyer has bad credit they need to put down 30%

price = 1000000
good_credit = False
bad_credit = True

if good_credit:
    down_payment = .1 * price
elif bad_credit:
    down_payment = .3 * price
else:
    print("Please fill out a credit application")
print(f'Down Payment is ${down_payment}')

#if applicant has high income AND good credit they are eligible for a loan

high_income = True
good_credit = True

if high_income and good_credit:
    print('Eligible for loan')

#if applicant has high income OR good credit they are eligible for a loan

high_income = True
good_credit = True

if high_income or good_credit:
    print('Eligible for loan')

#if applicant has high income AND DOES NOT HAVE criminal record they are eligible for a loan

high_income = True
criminal_record = False

if high_income and not criminal_record:
    print("Eligible for loan")

# if temp is greater than 30
#     print its a hot day
# if temp is less than 30
#     print its a cold day
# otherwise its neither hot nor cold

temperature = 35

if temperature > 30:
    print("It's a hot day")
elif temperature < 30:
    print("It's a cold day")
else:
    print("It's neither hot nor cold")

# if name is less than 3 characters
#     name needs to be more than 3 characters
# if name is more than 50 characters
#     name needs to be less than 50 characters
# else
#     name looks good

# name = "Bryan Hawkins"
# if len(name) <3:
#     print('Name needs to be more than 3 characters')
# elif len(name) >50:
#     print('Name needs to be less than 50 characters')
# else:
#     print('Name looks good')



weight = int(input('What is your weight? '))
unit = input('Please input k for kg or l for lbs ')

if unit.lower() == 'k':
    converted_weight = weight / .45
    print(f'Your weight in lbs is {converted_weight}')
elif unit.lower() == 'l':
    converted_weight = weight * .45
    print(f'Your weight in kgs is {converted_weight}')
else:
    print('Please try again and input k or l')
