a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))


def summNumbers(a, b):
    if b == 0:
        return a
    return summNumbers(a, b - 1) + 1


print(summNumbers(a, b))
