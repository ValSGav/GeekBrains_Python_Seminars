# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

# r - read
# w - write(перезаписываем файл)
# a - append(дописываем в файл)
#

# with open("file.txt", "w", encoding="utf-8") as file_w: # в рамках with работаем с файлом,
#                                                         # по окончании закрывать его не нужно
#     file_w.write('первая строка')

# with open("file.txt", "a", encoding="utf-8") as file_a:
#     file_a.write('\nвторая строка')

# with open("file.txt", "r", encoding="utf-8") as file_r:
#     #text_from_file = file_r.read()

#     #text_from_file = file_r.readline()
#     text_from_file = file_r.readlines()

#     print(text_from_file)

def add_contact(file_name):
    with open(file_name, 'a', encoding='utf-8') as ad_book:
        adress_name = input('Введите имя: ')
        adress_second_name = input('Введите отчество: ')
        adress_last_name = input('Введите фамилию: ')
        adress_phone = input('Введите номер телефона: ')
        ad_book.write(
            f'{adress_name};{adress_second_name};{adress_last_name};{adress_phone}\n')


def read_all(file_name):
    enumerate_list_of_found_ares = find_contact_lines(file_name)
    print_enumerate_list(enumerate_list_of_found_ares, 'Адресная книга')


def find_contact(file_name):
    text_for_search = input('Введите текст для поиска контактов: ')
    enumerate_list_of_found_ares = find_contact_lines(
        file_name, text_for_search)
    print_enumerate_list(enumerate_list_of_found_ares, 'Найденные контакты:')


def find_contact_lines(file_name, text_filter='', make_enum=True) -> list:
    with open(file_name, 'r', encoding='utf-8') as file_for_read:
        if make_enum == True:
            file_lines = enumerate(file_for_read.readlines(), start=1)
        else:
            file_lines = file_for_read.readlines()

    list_return = list(filter(
        lambda x: text_filter in x[1] or text_filter == '' and x[1] != '', file_lines))
    return list_return


def print_enumerate_list(enum_list, title=''):
    print(title)
    for i in enum_list:
        splitted_str = i[1].replace('\n', '').split(';')
        print(
            f'{i[0]} - {splitted_str[0]} {splitted_str[1]} {splitted_str[2]} {splitted_str[3]}')


def delete_contact(file_name):

    text_for_search = input('Введите текст для поиска контактов которые нужно удалить,\
                            \nили Enter, чтобы просмотреть все контакты: ')

    enumerate_list_of_found_ares = find_contact_lines(
        file_name, text_for_search)
    print_enumerate_list(enumerate_list_of_found_ares,
                         'Контакты для удаления:')
    index = int(
        input('Введите номер контакта, который собираетесь удалить: '))

    list_of_founded_lines = find_contact_lines(file_name, make_enum=False)

   
    print(f'Удален элемент: {list_of_founded_lines.pop(index - 1)}')

    with open(file_name, 'w', encoding='utf-8') as file_w:
        file_w.writelines(list_of_founded_lines)


def edit_contact(file_name):

    text_for_search = input('Введите текст для поиска контактов которые нужно редактировать,\
                            \nили Enter, чтобы просмотреть все контакты: ')

    enumerate_list_of_found_ares = find_contact_lines(
        file_name, text_for_search)
    print_enumerate_list(enumerate_list_of_found_ares,
                         'Контакты для редактирования:')
    index = int(
        input('Введите номер контакта, который собираетесь редактировать: '))

    list_of_founded_lines = find_contact_lines(file_name, make_enum=False)

    edit_name, edit_second_name, edit_last_name, edit_phone = \
        list_of_founded_lines[index - 1].replace('\n', '').split(';')
    new_name = input(
        f'Введите новое значение "Имя", или Enter, чтобы не менять(сейчас- {edit_name}): ')
    new_second_name = input(
        f'Введите новое значение "Отчество", или Enter, чтобы не менять(сейчас- {edit_second_name}): ')
    new_last_name = input(
        f'Введите новое значение "Фамилия", или Enter, чтобы не менять(сейчас- {edit_last_name}): ')
    new_phone = input(
        f'Введите новое значение "Телефон", или Enter, чтобы не менять(сейчас- {edit_phone}): ')
    if new_name != '':
        edit_name = new_name
    if new_last_name != '':
        edit_last_name = new_last_name
    if new_second_name != '':
        edit_second_name = new_second_name
    if new_phone != '':
        edit_phone = new_phone
    list_of_founded_lines[index -
                          1] = f'{edit_name};{edit_second_name};{edit_last_name};{edit_phone}\n'
    with open(file_name, 'w', encoding='utf-8') as file_w:
        file_w.writelines(list_of_founded_lines)


def main():
    file_name = './adress_book.txt'
    user_choise = '0'
    while user_choise != 'q':
        user_choise = input('Меню: \
                            \n1 - добавить контакт\
                            \n2 - прочитать всю телефонную книгу\
                            \n3 - найти контакт\
                            \n4 - редактировать контакт\
                            \n5 - удалить контакт\
                            \nq - выход\
                            \n:')
        if user_choise == '1':
            add_contact(file_name)
        elif user_choise == '2':
            read_all(file_name)
        elif user_choise == '3':
            find_contact(file_name)
        elif user_choise == '4':
            edit_contact(file_name)
        elif user_choise == '5':
            delete_contact(file_name)
        elif user_choise == 'q':
            print('Всего хорошего')
        else:
            print('Нет такого варианта действия')


if __name__ == "__main__":
    main()
