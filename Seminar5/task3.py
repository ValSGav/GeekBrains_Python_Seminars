# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

def print_reverse(numb_of_digits: int) -> str:

    curr_number = input("Введите цифру: ")
    if numb_of_digits == 1:
        return curr_number
    else:
        return print_reverse(numb_of_digits - 1)+ " " + curr_number
          
print(print_reverse(int(input("Введите количество цифр в числе: "))))