# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5


def print_the_number_closest_in_value_in_the_array(number, arrray_of_numbs):
    # Алгоритм для не упорядоченного массива, с учетом того, чтоб могут быть два 
    # числа(меньше и больше) одинаково близких к "загаданному"

    curr_min_diff = 0
    curr_min_negative_diff = 0

    for i in array_of_numbers:

        difference = i - number

        if difference == 0:
            print(
                f"в массиве {array_of_numbers} ближайшим к нашему числу {number} являются оно само: {number}")
            return
        elif difference > 0:
            if curr_min_diff == 0:
                curr_min_diff = difference
            else:
                curr_min_diff = min(curr_min_diff, difference)
        else:
            if curr_min_negative_diff == 0:
                curr_min_negative_diff = difference
            else:
                curr_min_negative_diff = max(
                    curr_min_negative_diff, difference)

    print(f'{curr_min_diff} и {curr_min_negative_diff}')

    if curr_min_diff == -curr_min_negative_diff:
        print(
            f"в массиве {array_of_numbers} ближайшими к нашему числу {number} являются {number + curr_min_negative_diff} и {number + curr_min_diff}")
    elif curr_min_diff == 0 or curr_min_negative_diff == 0:
        print(
            f"в массиве {array_of_numbers} ближайшим к нашему числу {number} являются {0}")
    elif curr_min_diff < - curr_min_negative_diff:
        print(
            f"в массиве {array_of_numbers} ближайшим к нашему числу {number} являются {number + curr_min_diff}")
    else:
        print(
            f"в массиве {array_of_numbers} ближайшим к нашему числу {number} являются {number + curr_min_negative_diff}")


numb_of_elements = int(input("Введите количество элементов в массиве: "))

array_of_numbers = []

for i in range(numb_of_elements):
    array_of_numbers.append(
        int(input(f"Введите число для {i} элемента массива: ")))

number = int(
    input("Введите число, для которого мы будем искать самое близкое в массиве: "))

print_the_number_closest_in_value_in_the_array(number, array_of_numbers)
