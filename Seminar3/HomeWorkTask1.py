# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

def get_numb_occur_digit_in_array(number, arrray_of_numbs):
    numb_of_occur = 0
    for i in arrray_of_numbs:
        if i == number:
            numb_of_occur += 1
    return numb_of_occur

numb_of_elements = int(input("Введите количество элементов в массиве: "))

array_of_numbers = []

for i in range(numb_of_elements):
    array_of_numbers.append(int(input(f"Введите число для {i} элемента массива: ")))

number = int(input("Введите число, количество вхождений которого мы будем искать в массиве: "))

print(f"Количество вхождений числа {number} в массив {array_of_numbers} - " 
      f"{get_numb_occur_digit_in_array(number, array_of_numbers)} раз")