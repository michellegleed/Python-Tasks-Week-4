first_number = input("Type a number: ")
second_number = input("Type another number: ")

if "." in first_number:
    first_number = float(first_number)
else:
    first_number = int(first_number)
    
if "." in second_number:
    second_number = float(second_number)
else:
    second_number = int(second_number)

result = first_number + second_number

print(result)