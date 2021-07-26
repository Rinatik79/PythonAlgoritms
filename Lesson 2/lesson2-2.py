num = input("Enter natural number please: ")

evens = "02468"
even = 0
odd = 0
for d in num:
    if evens.find(d) != -1:
        even += 1
    else:
        odd += 1

print(num + " contains " + str(even) + " even and " + str(odd) + " odd digits.")
