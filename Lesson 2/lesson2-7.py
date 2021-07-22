# есть вот такое доказательство: https://otvet.mail.ru/question/45249046
# но мне хочется сгенерить два случайных числа и проверить для них истинность равенства

import random

for i in range(2):
    x = random.randint(0, 1000)
    sum = 0

    for j in range(x + 1):
        sum += j

    if x * (x + 1) / 2 == sum:
        print("Try number " + str(i + 1) + " proved equation: 1+2+...+n = n(n+1)/2 for natural number " + str(x))
