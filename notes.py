import json
from pprint import pprint
from time import localtime, strftime

from ui.inputs import input_note
from ui.view import print_line

notes_list = [
    {
        'id': 1,
        'title': 'Note 1',
        'body': 'blah-blah',
        'updated_at': '04.04.2022'  # strftime('%d.%m.%Y', localtime())
    }

]


def add_note(note):
    """
    Добавляет заметку
    """
    if notes_list:
        note['id'] = notes_list[-1]['id'] + 1
    else:
        note['id'] = 1

    note['updated_at'] = strftime('%d.%m.%Y', localtime())
    notes_list.append(note)

    print_line()
    print('Ваша заметка добавлена')


def remove_note(note_id):
    """
    Удаляет заметку по ее id"
    """
    idx = 0
    for note in notes_list:
        if note['id'] == note_id:
            idx = notes_list.index(note)
            break

    notes_list.remove(notes_list[idx])

    print_line()
    print(f'Заметка №{note_id} удалена')


def find_notes_on_date(date):
    """
    Ищет заметку по дате ее обновления
    """
    notes_on_date = []
    for note in notes_list:
        if note['updated_at'] == date:
            notes_on_date.append(note)

    if not notes_on_date:
        return f'Нет заметок с такой датой'

    print_line()
    print(f'Заметки по дате {date}:')

    return notes_on_date


def change_note(note_id):
    for note in notes_list:
        if note['id'] == note_id:
            new_note = input_note()
            note['title'] = new_note['title']
            note['body'] = new_note['body']
            note['updated_at'] = strftime('%d.%m.%Y', localtime())

    print_line()
    print(f'Заметка №{note_id} обновлена')


def push_notes_db():
    """
    Записывает все заметки в файл формата .json
    """
    with open('notes_db.json', 'w') as file_db:
        json.dump(notes_list, file_db)

    print_line()
    print('Заметки записаны в файл notes_db.json')


def pull_notes_db():
    """
    Извлекает все заметки в файла формата .json
    """
    with open('notes_db.json', 'r') as file_db:
        notes_db = json.load(file_db)
        print('Заметки из файла:')
        pprint(notes_db)
