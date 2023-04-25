# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)

def get_numbs_in_first_list_that_not_occur_in_second_list(list1: list, list2: list) -> list:
    result_list = []
    for i in range(len(list1)):
        if list1[i] not in list2:
            result_list.append(list1[i])
    return result_list


def get_array_of_numbs(message: str) -> list:
    result_list = []
    # count_of_elements = int(input("Введите количество элементов в списке: "))
    # for i in range(count_of_elements):
    #     result_list.append(
    #         int(input(f"Введите значение для {i} элемента списка: ")))
    # return result_list

    list_of_str_number = input(message).split()
    for i in range(len(list_of_str_number)):
        result_list.append(int(list_of_str_number[i]))
    return result_list


list1 = get_array_of_numbs("Введите все числа первого списка через пробел: ")
list2 = get_array_of_numbs("Введите все числа второго списка через пробел: ")

print(list1)
print(list2)
print(get_numbs_in_first_list_that_not_occur_in_second_list(list1, list2))
