# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

def show_count_of_figure_for_each_kid(s):
    # по условию задачи количество жур. сделанных Петей обозначим за х,
    # количество жур. Сержи, тоже x, количество жур. Кати (х+х)*2
    # значит s = x+x+(x+x)*2
    # x = s/6 и s должно быть кратно 6

    if s % 6 != 0:
        print('Для указанног количества фигурок не получится вычислить количество фигурок по условиям задачи!')
    else:
        x = int(s/6)
        print(f'Количество фигурок сделанных Петей {x} , количество фигурок сделанных Сережей {x}, а количество фигурок сделанных Катей {x*4}')


numb_of_figure = int(input('Введите количество фигурок:'))
show_count_of_figure_for_each_kid(numb_of_figure)
