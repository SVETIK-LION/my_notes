import pickle
from pprint import pprint
from time import localtime, strftime

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

    print(f'Заметка с id = {note_id} удалена')


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

    return notes_on_date


def push_notes_db():
    """
    Записывает все заметки в файл формата .json
    """
    with open('notes_db.json', 'wb') as file_db:
        for note in notes_list:
            pickle.dump(note, file_db)

    print('Заметки записаны в файл notes_db.json')


def pull_notes_db():
    """
    Извлекает все заметки в файла формата .json
    """
    with open('notes_db.json', 'rb') as file_db:
        notes_db = pickle.load(file_db)

    pprint(notes_db)
