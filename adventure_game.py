def gameover(reason):
    print(f'\n game over! you were {reason}')

def room1():
    door_choice = int(input('\n you are escaping a labyrinth and you reach a junction room. there are 3 identical doors before you... \n behind door 0 is a raging inferno. \n behind door 1 is a deadly assassin. \n behind door 2 is a lion which hasn\'t eaten for three months. \n which door do you pick? (0/1/2) '))

    if door_choice == 2:
        print('\ngood choice. lions can only survive ~14 days without food. you walk past the lion\'s rotten carcass and continue your escape')
        room2()
    elif door_choice == 1:
        gameover('killed by the assassin')
    elif door_choice == 0:
        gameover('burnt to a crisp')

def room2():
    ans, counter = None, 3
    print(f'\n you emerge into a school classroom. written on the blackboard is the following question: \n there is a patch of lilypads on a lake. the patch doubles in size every day. if it takes 24 days for the patch to cover the entire lake, how many days would it take to cover half the lake?\n')
    
    while counter >= 1:
        ans = int(input(f'\n {counter} attempts remaining. enter your answer (in days) here: '))
        if ans == 23:
            print('\n correct. you may progress to the next room')
            room3()
            break
        else:
            counter -= 1

    gameover(f'exterminated because you could not provide a solution.')

def room3():
    print('\nthis room will test your python string handling knowledge. \n given that string1 = "hello world", select the correct output of the following operation. \n print(string1[5::-1] \n 0. "hello" \n 1. "world" \n 2. "olleh" \n 3. "worl"')
    counter, ans = 2, None
    while counter >= 1:
        ans = int(input(f'\n {counter} attempts remaining. enter your answer here (0/1/2/3):  '))
        if ans == 2:
            print('\n correct. you may continue...')
            room4()
            break
        else:
            counter -= 1

def room4():
    print('welcome to the final room. to complete the game and escape the labrynth you must identify the TRUE statement among the following. \n 0. correlation == causation \n 1. type 1 errors are also known as false negatives \n 2. the null hypothesis is that there is no significant difference between specified populations \n 3. a correlation value of -1.00 means there is no correlation between two variables')
    ans = int(input('enter your answere here (0/1/2/3): ')) 
    if ans == 2:
        print('correct! you have completed the game')
        
room1()

    
