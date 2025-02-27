import math

print("I will find the your cubes inner diagonal length")
x = int(input("What is the edge length for your cube: "))
if (x <= 0):
  x = int(input("Your edge length has to be a nonzero and a positive number: "))
   
num = 3
n =  math.sqrt(num)
d = x * n
print("Your inner diagonal is: %.2f" % d)
