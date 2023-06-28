# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных

path = str('phones.txt')
phone_book = {}


def open_file(path: str = 'phones.txt'):
    file = open(path, 'r', encoding='UTF-8')
    data = file.readlines()
    file.close()
    for contact in data:
        nc = contact.strip().split(':')
        phone_book[int(nc[0])] = {'name': nc[1], 'phone': nc[2], 'comment': nc[3]}
    print('\nТелефонная книга успешно загружена')

def save_file():
    data = []
    for i, contact in phone_book.items():
        new = ':'.join([str(i), contact.get("name"), contact.get("phone"), contact.get("comment")])
        data.append(new)
    data= '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)
    print('Файл сохранен')

def show_info(book: dict[int, dict]):
    print('=' * 200)
    for i, cnt in book.items():
        print(f'{i:>3}.{cnt.get("name"):<35}{cnt.get("phone"):<25}{cnt.get("comment"):<20}')
    print('=' * 200)

def add_contact():
    current_id = max(list(phone_book.keys())) + 1
    name = input('Введите имя контакта: ')
    phone = input('Введите телефон контакта: ')
    comment = input('Введите комментарий к контакту: ')
    phone_book[current_id] = {'name': name, 'phone': phone, 'comment': comment}
    print('Контакт добавлен')
def search():
    result = {}
    word = input('Введите поисковый запрос: ')
    for i, contact in phone_book.items():
        if word.lower() in ''.join(list(contact.values())).lower():
            result[i] = contact
    return result

def change_contact():
    result = search()
    show_info(result)
    index = int(input('Введите ID контакта для изменения'))
    delete_cnt = phone_book.pop(index)
    name = input('Введите новое имя контакта: ')
    phone = input('Введите новый телефон контакта: ')
    comment = input('Введите новый комментарий к контакту: ')
    phone_book[index] = {'name': name, 'phone': phone, 'comment': comment}
    print('Контакт изменен')
def remove ():
    result = search()
    show_info(result)
    index = int(input('Введите ID контакта для удаления'))
    del_cnt = phone_book.pop(index)
    print(f'\nКонтакт {del_cnt.get("name")} удален')





def start() -> int:
    main_menu = '''Главное меню:
    1. Открыть файл
    2. Сохранить файл
    3. Показать все контакты
    4. Создать контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    Выход'''
    print(main_menu)

    while True:
        select = input("Выберите пункт меню: ")
        if select.isdigit() and 0 < int(select) < 9:
            return int(select)


while True:
    select = start()
    match select:
        case 1:
            open_file('phones.txt')
        case 2:
            save_file()
        case 3:
            show_info(phone_book)
        case 4:
            add_contact()
        case 5:
            result = search()
            show_info(result)
        case 6:
            change_contact()
        case 7:
            remove()
        case 8:
            print('Завершение программы')
            break
