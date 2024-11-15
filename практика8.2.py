import math

def square_quadrangle(a, b, c, d, diagonal):

    p1 = 0.5 * (a + b + diagonal)
    p2 = 0.5 * (c + d + diagonal)

    area1 = math.sqrt(p1 * (p1-a)*(p1-b)*(p1-diagonal))
    area2 = math.sqrt(p2 * (p2-c)*(p2-d)*(p2-diagonal))
    return area1 + area2

a = float(input("Введите длину первой стороны: "))
b = float(input("Введите длину второй стороны: "))
c = float(input("Введите длину третьей стороны: "))
d = float(input("Введите длину четвертой стороны: "))
diagonal = float(input("Введите длину диагонали: "))

area = square_quadrangle(a, b, c, d, diagonal)

print("Площадь четырёхугольника равна: ", area)