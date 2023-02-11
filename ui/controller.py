from notes import add_note, remove_note, find_notes_on_date, push_notes_db, pull_notes_db, notes_list
from ui.inputs import input_id, input_date, input_notes
from ui.inputs import read_menu_number
from ui.view import (
    MENU_EXIT,
    MENU_PULL_NOTES,
    MENU_PUSH_NOTES,
    MENU_VIEW_ALL_NOTES,
    MENU_REMOVE_NOTE,
    MENU_ADD_NOTE,
    MENU_FIND_NOTES_ON_DATE,
    show_notes,
    show_menu, show_list)


def run():
    """
    Открывает меню заметок
    """
    menu_number = 1
    while menu_number != MENU_EXIT:
        show_menu()
        menu_number = read_menu_number()

        if menu_number == MENU_ADD_NOTE:
            note = input_notes()
            add_note(note)

        elif menu_number == MENU_VIEW_ALL_NOTES:
            show_notes(notes_list)

        elif menu_number == MENU_FIND_NOTES_ON_DATE:
            date = input_date()
            show_list(find_notes_on_date(date))

        elif menu_number == MENU_REMOVE_NOTE:
            note_id = input_id()
            remove_note(note_id)

        elif menu_number == MENU_PUSH_NOTES:
            push_notes_db()

        elif menu_number == MENU_PULL_NOTES:
            pull_notes_db()
