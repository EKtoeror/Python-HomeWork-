# Петя и Катя – брат и сестра. Петя – студент,
# а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

# s, p = map(int, input().split())
# if s**2 - 4 * p > 0:
#     x = (s-int((s**2-4*p)**0.5))//2
#     y = (s+int((s**2-4*p)**0.5))//2
#     print(x, y)
# else:
#     print("Такое не возможно")

s = int(input("Введите сумму чисел: "))
p = int(input("Введите произведение чисел: "))
d = int(s*s - 4 * p)

if d < 0:
    print("Такое не возможно")

else:
    y = int((s + d)/2)
    x = int(s - y)
    if 0 < x <= 1000 and 0 < y <= 1000:
        print(x, y)
    else:
        print("Загадали не натуральные числа")
