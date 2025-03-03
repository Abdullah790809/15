
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
