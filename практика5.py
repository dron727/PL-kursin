summa = 0
quantity = 0
n = int(input("Введите число: ")
if n == 0:
    print("Вы ввели 0!")
else:
    while n != 0:
        if n > 0:
            summa += n
            quantity += 1
            n -= 1
        elif n < 0:
            summa += n
            quantity += 1
            n += 1
    print(summa/quantity)