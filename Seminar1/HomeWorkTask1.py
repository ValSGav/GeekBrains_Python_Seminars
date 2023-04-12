# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

def GetSumOfDgit(numb):
    currNumb = numb
    sum = 0
    while currNumb > 0:
        sum += currNumb%10
        currNumb = currNumb//10
    return sum


numb = int(input("Введите число: "))

print(GetSumOfDgit(numb))
