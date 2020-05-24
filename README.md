# Multiple-Dice-Roller

It's necessary to install the numpy package to run the program.

I decided to create this project after failing to find a decent dice roller online for a remote D&D session. Most of the dice rollers that I found
were simple d6 rollers. I tried to create a more complex roller while maintaining the code and the interface simple.
It also allowed me to practice some concepts I've learned, such as generating random numbers.

I'm new to programming, so feedback is much appreciated. All the code has been written by myself from scratch.

CODE UPDATE: 24/05/20

I made the following changes into the code:

- The rolls would never yield the highest number, since the highest number in the range is exclusive. I had two options to correct this problem: I could either add 1 to every single value in my dictionary 'dice' or add 1 when the function was called. I went for the second one since I thought it was less confusing to someone new to coding such as myself.
- I've added a second code, similar to the first one, that yields an array containing all the rolls. This was made by using the optional parameter 'size' in the randint() function. This way, there is no need to use a for loop to iterate repeatedly untill all the rolls are done, but the result display could become more complicated as the number of dice is higher and it isn't as friendly as before. I could have made it so by iterating over the array and displaying every result separately, but the whole point of using this parameter was to eliminate the iteration in the first place. I've renamed the functions 'option1()' and 'option2()' (which now incorporates the for loop), so you can choose whichever display suits you by commenting/uncommenting the proper lines. I've left 'option2()' as standard.

NEXT UPDATE: I will work around the user inputs to avoid exceptions in case something other than the numbers in the menu is typed. I could do it with a simple if/elif/else, but for the sake of practice I will check into exception handling.
