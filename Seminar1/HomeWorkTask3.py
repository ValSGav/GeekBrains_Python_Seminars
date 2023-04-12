# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
#Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
#Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no


def determ_lucky_ticket(number_of_ticket):    
    curr_numb = number_of_ticket
    count_of_digit = 0
    
    while curr_numb > 0:
        curr_numb = curr_numb//10
        count_of_digit += 1

    if count_of_digit % 2  > 0 or count_of_digit <=1:
        return False
    
    curr_numb = number_of_ticket    
    sum_of_digit = 0
    counter = 1

    while curr_numb > 0:        
        if counter <= count_of_digit/2:
            sum_of_digit += curr_numb%10
        else:
            sum_of_digit -= curr_numb%10
        
        curr_numb = curr_numb//10
        counter += 1

    return sum_of_digit == 0
    

numb = int(input('Введите номер билетика: '))

if determ_lucky_ticket(numb):
    print(f'Билетик с номером {numb} счастливый!') 
else:
    print(f'Не повезло, билетик с номером {numb} не счастливый.') 
    
