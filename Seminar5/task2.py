# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

def change_maximal_numb_to_minimal(list_of_numb: list) -> list:
    max_num = max(list_of_numb)
    min_num = min(list_of_numb)
    for i in range(len(list_of_numb)):
        if list_of_numb[i] == max_num:
            list_of_numb[i] = min_num
    return list_of_numb


list_of_numbs = [1, 3, 3, 6, 7, 4]
print(change_maximal_numb_to_minimal(list_of_numbs))
