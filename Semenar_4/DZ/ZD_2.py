import random
kol_kus = int(input("Введите количество кустов черники - "))
mas = [random.randint(1,30) for i in range(kol_kus)]
print(mas)
sum_1 = 0
max_m = 0
i = 0
for i in range(len(mas)):
    sum_1 = (mas[i] + mas[i-1] + mas[i-2])
    if sum_1 > max_m:
        max_m = sum_1
    i += 1
print(max_m)

