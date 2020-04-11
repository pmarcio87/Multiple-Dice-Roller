import numpy as np

dice = {'1':4,'2':6,'3':8,'4':10,'5':12,'6':20}                #Using a dictionary to pair each type of die with its number of sid

def menu():
    print('Choose the appropriate die to roll according to the numbers below:')
    print('')
    print('1 - 4-sided die (d4)')
    print('2 - 6-sided die (d6)')
    print('3 - 8-sided die (d8)')
    print('4 - 10-sided die (d10)')
    print('5 - 12-sided die (d12)')
    print('6 - 20-sided die (d20)')
    print('')
    sides = input('Select your die: ')
    print('')
    n_dice = int(input('How many will you roll?: '))
    print('')

    n=1                                                         #Variable for printing the result
    for i in range(n_dice):                                     #Iterating over the number of dice rolled
        print('The result for dice '+str(n)+' is: '+str(roll(sides)))
        print('')
        n+=1
    repeat()

def roll(sides):
    n_sides = dice[sides]                                       #Retrieving the number of sides from the dictionary based on the user's selection
    roll = np.random.randint(1,n_sides)                         #Generating a random number with min=1 and max=number of sides on the chosen die
    return roll

def repeat():
    repeat = input('Roll again? (Y/N): ')
    if repeat.lower() == 'y'or repeat.lower() == 'yes':
        print('_________________________________________________________________________')
        menu()

menu()
    
