# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

def get_fibb(numb_fibb: int) -> int:
    if numb_fibb > 1:
        return get_fibb(numb_fibb - 1) + get_fibb(numb_fibb - 2)
    else:
        return 1
    
print(get_fibb(9))
    
