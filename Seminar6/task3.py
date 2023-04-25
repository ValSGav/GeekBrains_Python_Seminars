# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: Вывод:
# 1 2 3 2 3 2

import random

def get_random_list(count_of_elements) -> list:
    return_list = []
    for i in range(count_of_elements):
        return_list.append(random.randint(1, 51))
    return return_list

def get_count_of_equal_pairs(in_list: list) -> int:
    counter = 0
    for i in set(in_list):
        counter += in_list.count(i) // 2
    return counter


print(my_list := get_random_list(12))
my_list.sort()
print(my_list)
print(get_count_of_equal_pairs(my_list))


