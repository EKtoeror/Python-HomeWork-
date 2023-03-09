a = int(input("Введите число А: "))
b = int(input("Введите число B: "))


def exp(a, b):
    e = a
    if b == 0:
        return 1
    return e * exp(a, b - 1)


print(exp(a, b))
