import random

def play():
    user_point = 0
    compute_point = 0
    exit = False
    while exit == False:
        options = ['r', 'p', 's']
        user_input = input('Enter R: Rock, P: Paper, S: Scissor  R/P/S only : ')
        computer_input = random.choice(options)

        if user_input == "":
            exit = True

        if user_input.lower() not in options:
            print('enter a valid alphabet')

        if user_input.lower() == 'r':
            if computer_input == 'r':
                print('its tie')
            elif computer_input.lower() == 'p':
                print('computer got the point')
                compute_point += 1
            elif computer_input.lower() == 's':
                print('you got the point')
                user_point += 1
        elif user_input.lower() == 'p':
            if computer_input == 'p':
                print('its tie')
            elif computer_input.lower() == 's':
                print('computer got the point')
                compute_point += 1
            elif computer_input.lower() == 'r':
                print('you got the point')
                user_point += 1
        elif user_input.lower() == 's':
            if computer_input == 's':
                print('its tie')
            elif computer_input.lower() == 'r':
                print('computer got the point')
                compute_point += 1
            elif computer_input.lower() == 'p':
                print('you got the point')
                user_point += 1
    if user_point > compute_point:
        print("You won")
        print('you point is : ', user_point)
    elif compute_point > user_point:
        print('computer won')
        print('an got ', compute_point)
    else:
        print('its tie ')

play()