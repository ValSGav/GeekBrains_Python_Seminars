# Задача 32: Определить индексы элементов массива (списка), значения которых 
# принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

def get_random_list(count_of_elements) -> list:
    return_list = []
    for i in range(count_of_elements):
        return_list.append(random.randint(-50, 51))
    return return_list


def get_list_of_index_of_elements_in_range(min_value: int, max_value: int, list_of_values: list) -> list:
    return_list = []
    for i in range(len(list_of_values)):
        if list_of_values[i] in range(min_value, max_value + 1):
            return_list.append(i)
    return return_list


count_of_values = int(input("Введите количество элементов в масcиве со случайными значениями: "))
min_value = int(input("Введите минимальное значение диапазона: "))
max_value = int(input("Введите максимальное значение диапазона: "))

print(list_of_values := get_random_list(count_of_values))
print(get_list_of_index_of_elements_in_range(min_value, max_value, list_of_values))



