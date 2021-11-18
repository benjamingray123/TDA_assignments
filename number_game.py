from random import randint

target = randint(0,100)

play = True
while play:
    guess = int(input('guess a number between 0 and 100: '))
    if guess == target:
        print(f'correct! you guessed {guess}!')
        break 
    elif guess > target:
        print('too high! try again')
    else: 
        print('too low! try again')
