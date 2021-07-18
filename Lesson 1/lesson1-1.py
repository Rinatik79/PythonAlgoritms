ui = ""
while ui.isdigit() is False or len(ui) != 3 :
    ui = input("Enter 3 digits number please: ")

sum = 0
prod = 1

for i in ui:
    sum += int(i)
    prod *= int(i)

print("Sum of all 3 digits in you number is: " + str(sum))
print("Product of all 3 digits in you number is: " + str(prod))
