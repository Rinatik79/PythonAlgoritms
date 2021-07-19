import random


def return_arranged_array(array):
    if array[0] > array[1]:
        aux = array[0]
        array[0] = array[1]
        array[1] = aux

    return array

i = input("Enter integer boundaries by using ';' as separator, for example -100;77 :")
f = input("Enter float boundaries by using ';' as separator, for example -100.89;77.77 :")
c = input("Enter letters boundaries by using ';' as separator, for example g;m :")

i = i.split(";")
i[0] = int(i[0])
i[1] = int(i[1])
i = return_arranged_array(i)

f = f.split(";")
f[0] = float(f[0])
f[1] = float(f[1])
f = return_arranged_array(f)

c = c.split(";")
c[0] = ord(c[0])
c[1] = ord(c[1])
c = return_arranged_array(c)

print("Random integer: " + str(random.randint(i[0], i[1])))
print("Random float: " + str(f[0] + ((f[1] - f[0]) * random.random())))
print("Random symbol: " + chr(random.randint(c[0], c[1])))