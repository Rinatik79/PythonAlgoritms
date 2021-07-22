num_qty = int(input("Enter qty of numbers you want to parse for specific digit: "))
digit = input("Enter needed digit for it appearance calculation: ")

count = 0

for i in range(num_qty):
    current = input("Enter number please: ")
    count += current.count(digit)

print("In entered sequence we found " + str(count) + " appearances of digit " + digit)