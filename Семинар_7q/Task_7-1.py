stix = input().split()
glasnie = {1: "АОУЫЭЕЁИЮЯаоуыэеёиюя"}
summ = 0
for i in range(len(stix)):
    for j in stix[i]:
        for k, v in glasnie.items():
            if j in v:
                summ += k
if summ % len(stix) == 0:
    print("Парам пам-пам")
else:
    print("Пам парам")
