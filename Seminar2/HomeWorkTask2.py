# Задача 10: На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть


import random

def find_min_flip(list_of_flip):
    heads = 0
    tails = 0
    for i in list_of_flip:
        if i: 
            heads += 1
        else:
            tails += 1
    if heads > tails and tails != 0:
        return tails
    else:
        return heads

numb_of_coins = int(input("Введите количество монеток: "))
list_of_coins = list()
for i in range(numb_of_coins):
    list_of_coins.append(random.randint(0,1))

print(list_of_coins)
print(f'Минимальное количество переворотов монеток: {find_min_flip(list_of_coins)}')