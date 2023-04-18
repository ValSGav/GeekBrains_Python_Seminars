# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

import random

n = int(input("Введите количество элементов в первом множестве: "))
m = int(input("Введите количество элементов во втором множестве: "))

list_n = list()
list_m = list()


for i in range(n):
    list_n.append(random.randint(1, 11))  

for i in range(m):
    list_m.append(random.randint(1, 11))

print(list_n)
print(list_m)

set_n = set(list_n)
set_m = set(list_m)

set_final = set_n.intersection(set_m)
final_list = list(set_final)
final_list.sort()

print(final_list)