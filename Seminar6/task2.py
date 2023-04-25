# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: Ввод:
# 5 5
# 1 2 3 4 5 1 5 1 5 1
# Вывод: Вывод:
# 0 2

import random

def get_count_of_both_less_neigborhood_for_elements_of_list(in_list: list) -> int:
    counter = 0
    for i in range(1, len(in_list)-1):
        if in_list[i-1] < in_list[i] > in_list[i+1]:
            counter += 1
    return counter



def get_random_list(count_of_elements) -> list:
    return_list = []
    for i in range(count_of_elements):
        return_list.append(random.randint(1, 51))
    return return_list


print(new_list := get_random_list(11))
print(get_count_of_both_less_neigborhood_for_elements_of_list(new_list))