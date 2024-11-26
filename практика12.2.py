def second_largest():
    largest = None
    second_largest = None

    while True:
        number = int(input("Введите натуральное число (0 для завершения): "))
        if number == 0:
            break

        if largest is None or number > largest:
            second_largest = largest
            largest = number
        elif number != largest and (second_largest is None or number > second_largest):
            second_largest = number

    if second_largest is not None:
        print("Второй по величине элемент:", second_largest)
    else:
        print("Нет второго по величине элемента.")

second_largest()