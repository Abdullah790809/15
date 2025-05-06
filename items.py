x = int(input("How many items are you entering: "))
items = []
print("Please enter your items now")
for i in range(x):
  h = str(input("Next item: "))
  items.append(h)
print("You have entered" , x , "items")
for p in items:
  print(p)
