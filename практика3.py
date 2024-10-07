print("Вводите данные от 1 до 8!")

a1 = int(input("Введите номер столбца первой клетки: "))
a2 = int(input("Введите номер строки первой клетки: "))

b1 = int(input("Введите номер столбца второй клетки: "))
b2 = int(input("Введите номер строки второй клетки: "))

if a1<1 or a1>8 or b1<1 or b1>8 or a2<1 or a2>8 or b2<1 or b2>8:
    print("Некоректные данные!")
else:
    def get_color(a, b):
        if (a + b) % 2 == 0:
            return "Чёрная"
        else:
            return "Белая"

    color1 = get_color(a1, a2)
    color2 = get_color(b1, b2)

    if color1 == color2:
        print("Да")
    else:
        print("Нет")
