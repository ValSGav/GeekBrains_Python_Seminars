# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

def my_pow(numb: int, pow: int) -> int:
    if pow == 0:
        return 1
    else:
        return numb * my_pow(numb, pow - 1)

numb = int(input("Введите число: "))
pow_of_numb = int(input("Введите значение степени в которую нужно возвести число: "))
print(f"{numb} в степени {pow_of_numb} = {my_pow(numb, pow_of_numb)}") 