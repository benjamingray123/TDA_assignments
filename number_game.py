from random import randint

target = randint(0,100)

while True:
    guess = int(input('guess an integer between 0 and 100: '))
    if guess == target:
        print(f'correct! you guessed {guess}!')
        break 
    elif guess > target:
        print('too high! try again')
    else: 
        print('too low! try again')
