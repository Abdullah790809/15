import math
length = input("Please input a length: ")
radius = int(input("Please input a radius: "))
length = float(length)
area = math.pow(length, 2)
area2 = 3.14 * radius
area3 = math.pow(area2, 2)
area4 = 0.5 * area3
area5 = area4 + area
print("The area of the object is: ", area5)
