import random

game = 0
numguessed = int(random.randrange(1,9,1))

while (game < 5): 
        usernumber = int(input("Please guess a number from 1 to 9 = "))
        print (usernumber)
        if  numguessed == usernumber:
                print('The number you guessed is PERFECT')
                game = 5
        elif  numguessed > usernumber:
                print('The number you guessed was LOW')
                game = game+1
        elif  numguessed < usernumber:
                print('The number you guessed is HIGH')
                game = game+1