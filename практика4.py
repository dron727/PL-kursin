def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
n = int(input("Введите число n: "))

result = factorial(n)

print("Факториал числа n равняется ", result)
