from random import randint

while True:
    sides = int(input('how many sides should the die have? '))
    print(randint(1,sides))
    play = input('roll again? (y/n) ')
    if play == 'n':
        break 
    else:
        continue 
        
