#random number guessing game
#import the random module
import random
#create a variable with boolean value True.
flag =  True
#Start a while loop till the flag is not True.
while flag :
    #Take a number for upper bound
    num =input("Type a number for the upper bound : ")
    #check if the input was in digit
    if num.isdigit():
        #if yes 
        print("Let's Play !")
        #convert the num variable into an integer.
        num = int(num)
        #flag false so we can get out of the loop
        flag = False
    else:
        #if the input is not a digit  
        print("Invalid input! Try Again !")
#create a variable that will be the secret number
secret = random.randint(1,num)
#create another variable for taking the guessed input from the user 
guess = None
#check number of counts
count = 1
#while guess is not equal to the secret value
while guess!=secret:
    #input can not have commas(,) so we use (+) to concatenate.
    guess = input ("Please type a number between 1 and " + str(num) + ": ")
    #check if the user input is a digit.
    if guess.isdigit():
        #convert the guess into an integer
        guess = int(guess)
    #if guess is equal to secret 
    if guess == secret:
        print("Wow, you got it!")

    # if guess is not equal to secret or guess is not a digit
    else:
        print("Please try again!")
        #add counts
        count = count +1 
#final statement.
print("It took you", count, "guesses")