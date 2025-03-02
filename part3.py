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
   print(p , "Pennies") # It will return the number assigned to the variable and then it will say Pennie's







   
