import random

x = random.randint(0, 100)
counter = 0
print("We made a random number 0 - 100")

while counter < 10:
    hypothesis = int(input("Try to guess it: "))
    if hypothesis > x:
        print("Our random number is less")

    elif hypothesis < x:
        print("Our random number is greater")

    else:
        print("You guess our number. Felicitation!\nBay!")
        exit(0)

    counter += 1

print("You haven't guess our random number. It was " + str(x) + " indeed.\nBay!")

