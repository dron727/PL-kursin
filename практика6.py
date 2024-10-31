string = input(str("Введите любое предложение: "))
count_a = string.count("а")
result = string.replace("а", "")

print("Получилась строка: ", result)
print("Удалено: ", count_a, " букв")