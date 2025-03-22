### number guessing game ###
"""
  Author : Abdullah Parvez
  Student Number : 790809
  Revison date : 21 March 2025
  Program : number guessing game
  Description :A game where the user has 6 tries to guess a selected number from 1 to 100 
VARIABLE DICTIONARY
  a = To a random number generated from 1 - 100 
  c(int) = Assigned to 1 
  x(int) = First user input
"""







import random # import random number generator

a = random.randrange(1,100) # Random number generated between 1 and 100 is assigned to a 
print("Hello! Welcome to the number guessing game!") # Output Hello! Welcome to the number guessing game!
print("I am thinking of a number between 1 and 100. It is your turn to guess what it is. You have a maximum of six (6) tries.") #I am thinking of a number between 1 and 100. It is your turn to guess what it is. You have a maximum of six (6) tries.
c = 1 # 1 is assigned to the variable c
x = 0 # 0 is assigned to the variable x 

     
while c < 7 and x != a: # Runs as long as c is less then 7 and x is not equal to a 
    x = int(input("Guess #" + str(c) + ": ")) # Guess input by user
    if x < a: # if x is less than a 
       print("Higher")  # output higher if condition above is true
    if x > a: #if x is greater than a 
       print("Lower") # output Lower if condition above is true
    if x == a: # If x is equal to the randome number
       print("You Guessed right!") # output you guessed right if condition above is true
    if (x > 100) or (x < 1): #if number x is greater than a hundread or less than 1 
       print("The Number is between 1 and 100 your output was not in that range") # output the Number is between 1 and 100 your output was not in that rangeif condition above is true

    c += 1 # Add 1 to the value assigned to c every time the while loop is ran 
    if c >= 7 and x != a: # if c greater than or equal to 7 and X not equal to a 
       print("you are out of guesses! The answer was" , a , ". Better luck next time!") # output  you are out of guesses! The answer was (a) . Better Luck next time!


