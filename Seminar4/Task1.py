# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию

def get_processed_strig(in_string):
    result_string = ''
    dict_of_repeat = {}
    for i in in_string:
        if dict_of_repeat.get(i) == None:
            result_string += i + " "
            dict_of_repeat[i] = 0
        else:
            dict_of_repeat[i] += 1
            result_string += i + "_" + str(dict_of_repeat.get(i)) + ' '
    return result_string

my_string = 'aabamnv;sdafabb'
print(my_string)
print(get_processed_strig(my_string))

