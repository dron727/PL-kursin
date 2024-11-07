import random
massiv = [random.randint(-100,100) for _ in range(10)]
print("Массив: ",massiv)
srednee = sum(massiv)/len(massiv)
print("Среднее арифметическое: ", srednee)
maksimalnoe = max(massiv)
menshe_maksimalnogo = 0
for element in massiv:
    if element < maksimalnoe:
        menshe_maksimalnogo += 1

print("Колличество элементов, меньших максимального: ", menshe_maksimalnogo)

bolshe_srednego = 0
for element in massiv:
    if element > srednee:
        bolshe_srednego += 1

print("Количество эдементов, больших среднего арифметического: ", bolshe_srednego)
