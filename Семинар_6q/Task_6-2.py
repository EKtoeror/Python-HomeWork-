import random

a = int(input("Введите кол-во элементов: "))
r_min = int(input("Введите минимальное значение диапазона: "))
r_max = int(input("Введите максимальное значение диапазона: "))

list_1 = []

for num in range(0, a):
    num = random.randint(-100, 100)
    list_1.append(num)
print(*list_1)

for num in list_1:
    if num >= r_min and num <= r_max:
        print(list_1.index(num), end=" ")
