def read_txt(my_filename):
    new_phone_book = list()
    list_of_fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(my_filename, 'r', encoding='utf-8') as phone_book_in:
        for line in phone_book_in:
            record = dict(tuple(zip(list_of_fields, line[:-1].split(','))))
            new_phone_book.append(record)
    return new_phone_book


def print_result(my_list):
    for i in range(len(my_list)):
        print(f"{i + 1}.")
        for k, v in my_list[i].items():
            print(k + ": " + v)
        print()


def find_by_lastname(my_list, my_last_name):
    result = list()
    for i in range(len(my_list)):
        s = my_list[i]['Фамилия']
        if s.lower().find(my_last_name.lower()) != -1:
            result.append(my_list[i])
    return result


def find_by_phonenumber(my_list, my_phone_number):
    result = list()
    for i in range(len(my_list)):
        s = my_list[i]['Телефон']
        if s.lower().find(my_phone_number.lower()) != -1:
            result.append(my_list[i])
    return result


def add_record(my_list, my_last_name, my_first_name, my_phone_number, my_note):
    list_of_fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    l = [my_last_name.capitalize(), my_first_name.capitalize(), my_phone_number, my_note]
    record = dict(tuple(zip(list_of_fields, l)))
    my_list.append(record)
    return my_list


def edit_record(my_list, my_number):
    print("\nВыберите необходимое действие:\n"
          "1. Изменить фамилию\n"
          "2. Изменить имя\n"
          "3. Изменить телефонный номер\n"
          "4. Изменить описание\n")
    choice = int(input("Введите номер пункта меню: "))
    if choice == 1:
        last_name = input("Введите новую фамилию: ")
        my_list[my_number - 1]['Фамилия'] = last_name.capitalize()
    if choice == 2:
        first_name = input("Введите новое имя: ")
        my_list[my_number - 1]['Имя'] = first_name.capitalize()
    if choice == 3:
        phone_number = input("Введите новый телефон: ")
        my_list[my_number - 1]['Телефон'] = phone_number
    if choice == 4:
        note = input("Введите новое описание: ")
        my_list[my_number - 1]['Описание'] = note
    return my_list


def write_txt(my_filename, my_list):
    with open(my_filename, 'w', encoding='utf-8') as phone_book_out:
        for i in range(len(my_list)):
            s = ''
            for v in my_list[i].values():
                s = s + v + ','
            phone_book_out.write(f'{s[:-1]}\n')


def copy_record(my_list, my_number, my_filename):
    with open(my_filename, 'w', encoding='utf-8') as copy_out:
        s = ''
        for v in my_list[my_number - 1].values():
            s = s + v + ','
        copy_out.write(f'{s[:-1]}\n')

def work_with_phonebook():
    phone_book = read_txt('phone.txt')

    choice = show_menu()

    while choice != 9:
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input("Введите фамилию полностью или частично: ")
            list_found_items = find_by_lastname(phone_book, last_name)
            if list_found_items == []:
                print("Абонент с такой фамилией не найден")
            else:
                print_result(list_found_items)
        elif choice == 3:
            phone_number = input("Введите телефонный номер полностью или частично: ")
            # print(change_number(phone_book, last_name, new_number))
            list_found_items = find_by_phonenumber(phone_book, phone_number)
            if list_found_items == []:
                print("Абонент с таким телефонным номером не найден")
            else:
                print_result(list_found_items)
        elif choice == 4:
            number = int(input("Введите номер записи которую хотите изменить: "))
            phone_book = edit_record(phone_book, number)
        elif choice == 5:
            last_name = input("Введите фамилию полностью: ")
            first_name = input("Введите имя полностью: ")
            phone_number = input("Введите телефонный номер: ")
            note = input("Введите описание: ")
            phone_book = add_record(phone_book, last_name, first_name, phone_number, note)
            print(phone_book)
        elif choice == 6:
            number = int(input("Введите номер записи которую хотите удалит: "))
            phone_book.pop(number - 1)
        elif choice == 7:
            write_txt('phone.txt', phone_book)
        elif choice == 8:
            number = int(input("Введите номер записи которую хотите скопировать: "))
            filename = input("Введите имя нового файла: ")
            copy_record(phone_book, number, filename)

        choice = show_menu()


def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Изменить данные абонента\n"
          "5. Добавить абонента в справочник\n"
          "6. Удалить абонента из справочника\n" 
          "7. Сохранить справочник в текстовом формате\n"
          "8. Копировать данные абонента в другой файл\n"
          "9. Выход из программы\n")
    choice = int(input("Введите номер пункта меню: "))
    return choice


work_with_phonebook()
