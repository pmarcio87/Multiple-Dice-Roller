import numpy as np

dice = {'1':4,'2':6,'3':8,'4':10,'5':12,'6':20}                        #Using a dictionary to pair each type of die with its number of sides

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
    sides = int(input('Select your die: '))
    print('')
    n_dice = int(input('How many will you roll?: '))
    print('')

    #option1(sides,n_dice)
    option2(sides,n_dice)

    repeat()

#def option1(sides,n_dice):                                             #Generates an array containing all the rolls
#    n_sides = dice[str(sides)] + 1                                     #Retrieving the number of sides from the dictionary based on the user's selection and adding 1 to adjust to the range
#    roll = np.random.randint(1,n_sides,size=n_dice)                    #Generating a random number with low=1, high=number of sides on the chosen die (adjusted since the highest value is exclusive) and size=number of dice rolled
#    print('The result(s) is(are): ' + str(roll))                       #The result will be an array containing the roll of each die

def option2(sides,n_dice):                                              #Original code for dice roll combined with the iteration - used to be separate
    n=1                                                                 #Variable for printing the result
    for i in range(n_dice):                                             #Iterating over the number of dice rolled
        n_sides = dice[str(sides)] + 1                                  #Retrieving the number of sides from the dictionary based on the user's selection and adding 1 to adjust to the range
        roll = np.random.randint(1,n_sides)                             #Generating a random number with low=1 and high=number of sides on the chosen die (adjusted since the highest value is exclusive)
        print('The result for dice '+str(n)+' is: '+str(roll))          #Printing the result of each roll separately before iterating over
        print('')
        n+=1

def repeat():
    repeat = input('Roll again? (Y/N): ')
    if repeat.lower() == 'y' or repeat.lower() == 'yes':
        print('_________________________________________________________________________')
        menu()

menu()
