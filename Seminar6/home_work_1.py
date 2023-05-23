
# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def get_list_of_ariеhmetic_progressing(a1: int, n: int, d: int) -> list:
    return_list = []
    for i in range(0, n):
        return_list.append(a1 + i * d)
    return return_list


a1 = int(input("Введите значение первого члена прогрессии: "))
d = int(input("Введите значение зазности между членами прогрессии: "))
n = int(input("Введите количество членов прогрессии: "))
print(get_list_of_ariеhmetic_progressing(a1, n, d))
