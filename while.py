# index =1
# while index <= 5:
#     print(index)
#     index = index + 1
# print("done")
#
# index =1
# while index <= 5:
#     print('*' * index)
#     index = index + 1
# print("done")


#guessing game

# secret_number = 9
# guess_count = 0
# guess_limit = 3
#
# while guess_count < guess_limit:
#     guess = int(user_input('Guess: '))
#     guess_count += 1
#     if guess == secret_number:
#         print('You guessed correctly')
#         break
# else:
#     print('You guessed incorrectly 3 times')


#
command = ''
started = False
stopped = False

while True:
    command = input("> ").lower()
    if command == 'start':
        if started:
            print('engine is already started')
        else:
            started = True
            print('engine is started')

    elif command == 'stop':
        if stopped:
            print('engine is already stopped')
        else:
            stopped = True
            print('engine is stopped')

    elif command == 'help':
        print('''
        type start - to start the car
        type stop - to stop the car
        type quit - to quit the game
        ''')
    elif command == 'quit':
        break
    else:
        print('I dont understand that user_input')