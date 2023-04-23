# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.


def get_sum_of_two_numbers(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return get_sum_of_two_numbers(a + 1, b - 1)
    

int_a = int(input("Введите первое число: "))
int_b = int(input("Введите второе число: "))

print(f"{int_a} + {int_b} = {get_sum_of_two_numbers(int_a, int_b)}")