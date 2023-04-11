# Задача №15. Общее обсуждение
# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

def select_arbuz(list_weight_of_arbuz):
    max_weight = list_weight_of_arbuz[0]
    min_weight = max_weight
    for i in list_weight_of_arbuz:
        if i < min_weight:
            min_weight = i
        elif i > max_weight:
            max_weight = i
    print(f'Теще {min_weight} кг, а мне, конечно, {max_weight} кг')

import random

numb_of_arbuz = int(input("Введите количество арбузов: "))
list_of_arbuz = list()
for i in range(numb_of_arbuz):
    list_of_arbuz.append(random.randint(1, 51))

print(list_of_arbuz)

select_arbuz(list_of_arbuz)
        
