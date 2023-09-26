import random
kol_kus = int(input("Введите количество кустов черники - "))
mas = [random.randint(1,30) for i in range(kol_kus)]
print(mas)

kus = int(input("Введите с какого куста начать собирать - "))
kus = kus -1
sum_1 = int(mas[kus]+ mas[kus-1] + mas[kus + 1])
print(sum_1)
