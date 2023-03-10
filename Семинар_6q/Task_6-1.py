a = int(input("Введите первый элемент: "))
b = int(input("Введите разность: "))
c = int(input("Введите кол-во элементов: "))

list_1 = []
for num in range(0, c):
    num = a + (c - 1) * b
    list_1.append(num)
    c = c - 1
list_1.sort()
print(*list_1)
