import numpy as np

n = 4
matrix = np.random.randint(1, 100, (n, n))

print("Исходная матрица: ")
print(matrix)

matrix_str = str(matrix)

with open('КурсинАндрейАнатольевич_У-244_vvod.txt', 'w') as file:
    file.write(matrix_str)