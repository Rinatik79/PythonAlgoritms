n = int(input("Enter number of sequence members please: "))
sum = 1
current_member = 1
for i in range(n-1):
    current_member *= -.5
    sum += current_member

print(sum)
