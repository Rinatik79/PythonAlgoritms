c = input("Enter two letters by using ';' as separator, for example g;m :").lower()

c = c.split(";")

print("Entered " + str(ord(c[0]) - 96) + "-th and " + str(ord(c[1]) - 96) + "-th alphabet letters.")
print("There are " + str(abs(ord(c[0]) - ord(c[1])) - 1) + " letters between.")
