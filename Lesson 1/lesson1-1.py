ui = ""
while ui.isdigit() is False or len(ui) != 3 :
    ui = input("Введите пожалуйста 3-х значное число: ")

sum = 0
prod = 1

for i in ui:
    sum += int(i)
    prod *= int(i)

print("Сумма всех цифер равна: " + str(sum))
print("Произведение всех трех цифер равно: " + str(prod))
