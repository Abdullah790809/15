### PART 1: Even or Odd ###
"""
  Author : Abdullah Parvez
  Student Number : 790809
  Revison date : 2 March 2025
  Program : Even or Odd
  Description : A program that determines whether the product of number is even or odd
VARIABLE DICTIONARY
  num1(int) = the first number inputted by the user
  num2(int) = the second number inputted by the user
  num3(int) = The product (multiplication) of the first number and the second number.
"""


print("Welcome to the even and odd detector") 
num1 = int(input("please input a Number other than 0")) #Gets user input and converts it into and integer
if num1 == 0: # if Variable num1 is equal to 0 
  num1 = int(input("Please input a nonzero number : ")) # Gets correct user input and converts it into and integer
  
num2 = int(input("please input a second number other than 0")) # Gets user input and coverts it into and integer

  
if num2 == 0: # if Variable num2 is equal to 0 
  num2 = int(input("Please input a nonzero number : ")) # Gets correct user input and converts it into and integer

num3 = num1 * num2 # Gets the product of of the two numbers assigned to num1 and num2 and assignes it variable num3 
rem = num3 % 2 # Finds out any remainder and assignes it to rem
if rem == 0: #if variable rem is equal 
   print("the product of your 2 Numbers is even") # Its will give output the product of your 2 Numbers is even
else: #if variable rem is something else 
  print("The product of your 2 Numbers is odd") # Its will give an output the product of your 2 Number is odd 

### PART 2: inner diagonal lenght calculator###
"""
  Author : Abdullah Parvez
  Student Number : 790809
  Revison date : 2 March 2025
  Program : Inner diagnal leanght calculator
  Description : A program that determines the inner diagonal lenght
VARIABLE DICTIONARY
  x(int) = the first number inputted by the user
  num(int) = holds the number 3 
  n(int) = sqaure root of the varibale num
  d(int) = The product (multiplication) of the variable x and n.
"""
  
"""
import math # Allows you to use math methods 
print("I will find the your cubes inner diagonal length")
x = int(input("What is the edge length for your cube: ")) # Gets user input of the edge length of their cube and and assigns it to variable x
if (x <= 0): # if 0 is equal or greater than variable x
  x = int(input("Your edge length has to be a nonzero and a positive number: ")) # Gets correct input and stores it to x 
   
num = 3 # States that the value 3 is and assigns it to variable num
n =  math.sqrt(num) # Sqaure roots value assigned to the variable nume 
d = x * n # Gets the product of value assigned to x and the value assigned to n 
print("Your inner diagonal is: %.2f" % d) # Returns the the rounded lenght of their inner diagonal 


### PART 3:## Change returner ###

"""
 Author : Abdullah Parvez
  Student Number : 790809
  Revison date : 2 March 2025
  Program : money change
  Description : A program that determines amount of change
"""




x = int(input("How much cents do you have: ")) # gets user input and turns in into an integer
money = x//100 # Calculates whole dollars and assigns it to variable money
cents = x % 100 # finds any remainder and stores it in cents variable and assigns it to variable cents
q = cents//25 # finds how many qaurters can fit in to the amount of cents and assigns it to variable q
cents = cents%25 # finds out any remaider and assigns it to variable cents 
d = cents//10 # finds out how many dimes can fit in to the cents left and assigns it to variable d
cents = cents%10 # find out  any remainder and assigns it to variable cents
n = cents//5 # find out how many nickles can fit in to the amount of cents left and assigns it to variable n
cents = cents%5 # finds out any remainder and assigns it to variable cents 
p = cents # any remaning cents left will be stored in the variable p which is short form for pennies 
if x == 0:     # states if user inputs 0
   print("no change") # It will returnan output sating no change 
if money  == 1: # if  the number  assigned variable money is equal to a dollar
   print(money , "Dollar") # It will return the number assigned to the variable and then it will say dollar
elif money > 1: # if the number  assigned to the variable money is greater than 1
   print(money , "Dollars") # It will return the number assigned to the variable and then it will say Dollar's

if q  == 1:  #if the number  assigned to the variable q is eqaul than 1
   print(q ,  "Quarter") # It will return the number assigned to the variable and then it will say Quarter's
elif q > 1:  #if a number  assigned to the variable q is greater than 1
   print(q , "Quarters") # It will return the number assigned to the variable and then it will say Quarters's

if d == 1:  #if the number assigned to the variable d is equal than 1
   print(d , "Dime") # It will return the number assigned to the variable and then it will say Dime
elif d >  1:  #if a number  assigned to the variable d is greater than 1
   print(d , "Dimes") # It will return the number assigned to the variable and then it will say Dime's
if n == 1:  #If a number  assigned to the variable n is equal than 1
   print(n , "Nickle") # It will return the number assigned to the variable and then it will say Nickle
elif n  > 1: #  if a number  assigned to the variable n is greater than 1
   Print(n , "Nickles") # It will return the number assigned to the variable and then it will say Nickle's
if p == 1:  #if a number  assigned to the variable p is equal than 1
   print(p , "Pennie") # It will return the number assigned to the variable and then it will say Pennie
elif p > 1:  #if a number  assigned to the variable p is greater than 1
   print(p , "Pennies") # It will return the number assigned to the variable and then it will say Pennies







   
