# Требуется вычислить,
# сколько раз встречается некоторое число X
# в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число
# N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1
n = int(input("Введите кол-во элементов в массиве: "))

list_1 = []

for num in range(1, n + 1):
    list_1.append(num)
    # Хотел сделать чтобы числа выходили рандомно,
    # # но не могу понять как это записать
    print(num, end=" ")
print(" ")  # не занл как ввести новый запрос с новой строки

m = int(input("Введите искомое число: "))

count = 0
for num in list_1:
    if num == m:
        count += 1
print(f"Число {m} встречается {count} раз")
