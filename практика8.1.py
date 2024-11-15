a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

def NOD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def NOK(a, b):
    return (a * b)/NOD(a, b)

print("НОД равен:", NOD(a, b))
print("НОК равен: ", NOK(a, b))