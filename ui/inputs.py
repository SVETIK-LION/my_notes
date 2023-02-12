from ui.view import MENU_ITEMS


def read_menu_number() -> int:
    """
    Запрашивает у пользователя пункт меню
    """
    menu_number_check = False
    menu_number = None
    while not menu_number_check:
        menu_number = input('Введите номер пункта меню: ')
        if not menu_number.isdigit():
            print('Введите число - номер пункта меню: ')
            continue
        menu_number = int(menu_number)
        if -1 < menu_number <= len(MENU_ITEMS):
            menu_number_check = True
        else:
            print('Такого пункта нет. Введите номер пункта меню из списка: ')
    return menu_number


def input_note() -> dict[str, str]:
    """
    Запрашивает заголовок и текст заметки
    """
    title = input('Заголовок заметки: ')
    body = input('Введите текст заметки: ')

    return {'id': '', 'title': title, 'body': body, 'updated_at': ''}


def input_date() -> str:
    date = input('Введите дату заметки (дд.мм.гггг): ')

    return date


def input_id() -> int:
    note_id = int(input('Введите id заметки: '))

    return note_id
