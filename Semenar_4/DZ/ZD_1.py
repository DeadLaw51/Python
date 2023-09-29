import random
kol_1 = int(input("Введите размер 1 множества - "))
kol_2 = int(input("Введите размер 2 множества - "))

my_set_1 = {random.randint(0,20) for i in range(kol_1) }
my_set_2 = {random.randint(0,20) for i in range(kol_2) }

print(my_set_1)
print(my_set_2)

print(my_set_1 & my_set_2)

