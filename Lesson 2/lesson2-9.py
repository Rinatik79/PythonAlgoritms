num_qty = int(input("Enter qty of numbers you want to parse for specific digit: "))

biggest = ""
record = 0

for i in range(num_qty):
    current = input("Enter number please: ")
    count = 0
    for j in current:
        count += int(j)

    if count > record:
        record = count
        biggest = current

print("Number with the greatest sum of digits is " + biggest + ", the sum of digits is " + str(record))