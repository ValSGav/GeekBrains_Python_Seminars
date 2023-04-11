# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.


def find_pow_of_2_min_or_equal_numb(numb):
    pow_of_2 = 0
    while numb>1:
        numb = numb//2
        pow_of_2 += 1
        print(f'{2**pow_of_2} ({pow_of_2} степень двойки)')
    return pow_of_2

n  = int(input("Введите число: "))
print(f'Степень двойки, являющаяся числом не превосходящим {n}: {find_pow_of_2_min_or_equal_numb(n)}')
