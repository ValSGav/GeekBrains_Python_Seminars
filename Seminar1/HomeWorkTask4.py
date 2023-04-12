# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
#(то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

def determ_possibility_splitting(m, n, pieces):

    for i in range(m):
        if i * n == pieces:
            return True

    for j in range(n):
        if i * m == pieces:
            return True
        
    return False

n_size = int(input('Введите количество плиток шоколадки по стороне "n": '))
m_size = int(input('Введите количество плиток шоколадки по стороне "m": '))
count_of_pieces = int(input('Введите количество кусочков которые вы хотите отломить от шоколадки: '))

if determ_possibility_splitting(n_size, m_size, count_of_pieces):
    print('Можно отломить такое количество плиток от шоколадки!')
else:
    print('Нельзя отломить такое количество плиток от шоколадки!')