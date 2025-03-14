print("Make a choice from the following menu: ")
print("A: apples")
print("B: bananas")
print("C: cherries")

ch = input(str("your choice: "))

if (ch == "A") or (ch == "a") or (ch == "apples") or (ch == "Apples"):
    print("I prefer apples")
elif (ch == "B") or (ch == "b") or (ch == "Bananas") or (ch == "bananas"):
    print("I prefer bananas")
elif (ch == "C") or (ch == "c") or (ch == "Cherries") or (ch == "cherries"):
    print("I prefer cherries")
while ch != (ch == "A") or (ch == "a") or (ch == "apples") or (ch == "Apples") or (ch == "B") or (ch == "b") or (ch == "Bananas") or (ch == "bananas") or (ch == "C") or (ch == "c") or (ch == "Cherries") or (ch == "cherries"):
  print("This choice is not apart of the following menue")
  print("A: apples")
  print("B: bananas")
  print("C: cherries")
  ch = input(str("your choice: "))
