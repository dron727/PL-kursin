import numpy as np

n = 4
matrix = np.random.randint(1, 100, (n, n))

print("Исходная матрица: ")
print(matrix)

max_in_rows = np.max(matrix,axis = 1)
min_in_columns = np.min(matrix, axis = 0)

print("Наибольщий элемент в каждой строке:")
print(max_in_rows)

print("Наименьший элемент в каждой строке:")
print(min_in_columns)