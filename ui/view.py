# 1. Добавить заметку
# 2. Отобразить все заметки
# 3. Поиск заметок по дате
# 4. Удалить заметку
# 5. Сохранить заметки в .json
# 6. Сохранить заметки в .csv

MENU_ADD_NOTE = 1
MENU_VIEW_ALL_NOTES = 2
MENU_FIND_NOTES_ON_DATE = 3
MENU_REMOVE_NOTE = 4
MENU_PUSH_NOTES = 5
MENU_PULL_NOTES = 6
MENU_EXIT = 0

MENU_ITEMS = [
    f'{MENU_ADD_NOTE}. Добавить заметку',
    f'{MENU_VIEW_ALL_NOTES}. Показать все заметки',
    f'{MENU_FIND_NOTES_ON_DATE}. Найти заметки по дате',
    f'{MENU_REMOVE_NOTE}. Удалить заметку',
    f'{MENU_PUSH_NOTES}. Сохранить заметки в файл .json',
    f'{MENU_PULL_NOTES}. Загрузить заметки из файла .json',
    f'{MENU_EXIT}. Выход'
]


def print_line():
    print("-" * 30)


def show_menu():
    print_line()
    for item in MENU_ITEMS:
        print(item)
    print_line()


def show_list(lst):
    print_line()
    print(lst)


def print_dict(d):
    print_line()
    print(d)


def show_notes(notes):
    print_dict(notes)
