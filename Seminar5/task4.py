# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

def check_the_divisibility_of_the_numb_by_all_prev(number: int, number_div: int = 0) -> bool:
    if number_div == 0:
        number_div = number - 1
    if number_div == 1:
        return False
    else: 
        return number%number_div == 0 or check_the_divisibility_of_the_numb_by_all_prev(number, number_div - 1)
    

print(check_the_divisibility_of_the_numb_by_all_prev(int(input("Введите число: "))))
    
