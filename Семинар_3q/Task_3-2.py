# Требуется найти в массиве A[1..N]
# самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число
# N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5
n = int(input("Введите кол-во элементов в массиве: "))

list_1 = []

for num in range(1, n + 1):
    list_1.append(num)
    print(num, end=" ")
print(" ")

m = int(input("Введите число: "))

n1 = list_1[0]
for num in list_1:
    if abs(n1 - m) > abs(num - m):
        n1 = num

print(f"Ближайшим элементом к числу {m} является {n1}")
