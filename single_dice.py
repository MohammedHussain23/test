import random
play = True
count = 0
old_number = 1

def roll_dice():
    global old_number
    number = random.randint(1,6)
    if number == old_number:
        number = random.randint(1,6)
        print(f'The number is {number}')
        old_number = number
    else:
        print(f'The number is {number}')
        old_number = number

while play:
    user_input = input('Do you want to roll the dice? (y/n): ').lower()
    if user_input == 'y':
        roll_dice()
        count += 1
    else:
        if count == 0:
            print('You did not roll the dice even once. Hope to roll with you next time!')
        elif count == 1:
            print(f'Thanks for rolling the dice {count} time with us. Bye!')            
        else:
            print(f'Thanks for rolling the dice {count} times with us. Bye!')
        play = False

