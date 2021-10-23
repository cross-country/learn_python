try:
    a = 100
    while a >= 0:
        b = int(input("Введите число: "))
        a = a - b
    print("недопустимое число")
    print(a)
except ValueError:
    print("Введите число!")