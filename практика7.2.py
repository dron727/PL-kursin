summa = 0
massiv = []
for i in range(10):
    element = int(input(f"Введите {i+1}-й элемент массива: "))
    massiv.append(element)
print("Массив: ", massiv)
for element in massiv:
    if element > 5:
        summa += element

print("Сумма элементов, больших 5: ", summa)