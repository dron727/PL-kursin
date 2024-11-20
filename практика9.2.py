import numpy as np

n = 5
matrix = np.random.choice(range(1, 100), size = (n, n), replace = False)

print("Исходная матрица: ")
print(matrix)

main_diagonal = [matrix[i][i] for i in range(n)]
secondary_diagonal = [matrix[i][n-i-1] for i in range(n)]

max_element = max(main_diagonal + secondary_diagonal)
max_element_position = None

for i in range(n):
    if matrix[i][i] == max_element or matrix[i][n-i-1] == max_element:
        if matrix[i][i] == max_element:
            max_element_position = (i, i)
        else:
            (i, n-i-1)
        break

intersection_element_position = (n // 2, n // 2)

matrix[max_element_position], matrix[intersection_element_position] = matrix[intersection_element_position], matrix[max_element_position]

print("Матрица после замены: ")
print(matrix)