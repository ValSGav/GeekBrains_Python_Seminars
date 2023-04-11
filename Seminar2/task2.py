# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

def findFibo(a):

    if a <=1:
        return -1
    
    counter = 4
    fibNumb = 2
    prevfibNumb = 1

    while fibNumb < a:
        fibNumb = fibNumb + prevfibNumb
        prevfibNumb = fibNumb - prevfibNumb
        counter +=1

    if fibNumb == a:   
        return counter
    else:
        return -1
    
print(findFibo(int(input('imput number: '))))
