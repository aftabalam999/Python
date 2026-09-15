import random

guess_num = random.randint(1, 100)
tries = 0

while(True):
    tries += 1
    user_input = int(input('Guess the number between 1 to 100 : '))
    if user_input == guess_num :
        print(f'you guess the right number {guess_num} in {tries} tries \n')
        break
    elif user_input < guess_num :
        print(f'wrong guess, try to guess higher value and {tries} time tried \n')
    else :
        print(f'wrong guess, try to guess lower value and {tries} time tried \n')
        