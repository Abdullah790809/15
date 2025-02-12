import math

x = input("Please input a whole number: ")
x = int(x)
y = input("Please input another nonzero whole number")
y = int(y)
if y == 0:
  y = int(input("Please input a nonzero whole : "))
  print("Now deciding if", y, "is a factor of", x, "...")

rem = x % y
if rem == 0:
    print("Yes!", y, "is a factor of", x)
else:
  print("No", y, "is not of factor of", x)







import math

x = input("Please input a whole number between 1 and 20: ")
x = int(x)
y = input("Please input another nonzero whole number between 1 and 20")
y = int(y)
if (y <= 0) and (y >= 20):
  y = int(input("Please input a nonzero whole between 1 and 20: "))
else: print( y, "is out of range")
if (x <= 0) and (x >= 20):
  x = int(input("Please input a nonzero whole between 1 and 20: "))
  print("Now deciding if", y, "is a factor of", x, "...")
else:
  print( x, "is out of range")
rem = x % y
if rem == 0:
    print("Yes!", y, "is a factor of", x)
else:
  print("No", y, "is not of factor of", x)
