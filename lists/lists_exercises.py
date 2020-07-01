# Question 1

foods = ["orange","apple","banana","strawberry","grape","blueberry",["carrot", "cauliflower", "pumpkin"],"passionfruit","mango","kiwifruit"]

print(foods[0])
print(foods[2])

print(foods[-1])

print(foods[0:3])

print(foods[-3:])

print(foods[6][-1])




# Question 2

mailing_list = [["Roary", "roary@moth.catchers"],["Remus", "remus@kapers.dog"],["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],["Biscuit", "biscuit@whippies.park"],["Rory", "rory@whippies.park"]]

print(f"{mailing_list[0][0]}: {mailing_list[0][1]}")
print(f"{mailing_list[1][0]}: {mailing_list[1][1]}")
print(f"{mailing_list[2][0]}: {mailing_list[2][1]}")
print(f"{mailing_list[3][0]}: {mailing_list[3][1]}")
print(f"{mailing_list[4][0]}: {mailing_list[4][1]}")


# Question 3

names = []

while len(names) < 3:
    name = input("Type a name.. ")
    names.append(name)

print(names)


# Question 4

string = input("Type a sentence.. ")

words = string.split(" ")
letters = list(string)

print(f"{len(words)} {words}")
print(f"{len(letters)} {letters}")

