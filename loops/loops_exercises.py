
# Question 1

number = input("Type a number ")
result = 0

while len(number) > 0:
    num = int(number)
    result = result + num
    number = input("Type a number ")

print(result)



# Question 2

mailing_list = [["Roary", "roary@moth.catchers"],["Remus", "remus@kapers.dog"],["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],["Biscuit", "biscuit@whippies.park"],["Rory", "rory@whippies.park"],]

for pet in mailing_list:
    print(f"{pet[0]}: {pet[1]}")



# Question 3

names = []

while len(names) < 3:
    name = input("Type a name.. ")
    names.append(name)

for name in names:
    print(name)



# Question 4

groceries = [["Baby Spinach", 2.78],["Hot Chocolate", 3.70],["Crackers", 2.10],["Bacon", 9.00],["Carrots", 0.56],["Oranges", 3.08]]

grocery_quantities = []

total = 0.0

for item in groceries:
    qty = input(f"How many {item[0]} did you buy? ")
    grocery_quantities.append(int(qty))

print()

print("====Izzy's Food Emporium====")
for index, item in enumerate(groceries):
    cost = item[1]*grocery_quantities[index]
    total += cost
    print(f"{item[0]:<20} ${cost:.2f}")
print("============================")
print(f"{'':<21}${total:.2f}")


