import datetime

from Note import Note
from NoteManager import NoteManager


def main():
    note_manager = NoteManager("notes.json")
    note_manager.load_notes()

    while True:
        print("1. Добавить заметку")
        print("2. Получить заметку")
        print("3. Удалить заметку")
        print("4. Вывести список заметок")
        print("5. Обновить заметку")
        print("6. Вывести заметки с конкретной датой")
        print("6. Выход")

        choice = input("Введите ваш выбор: ")

        if choice == "1":
            title = input("Введите заголовок: ")
            body = input("Введите текст заметки: ")
            note = Note(len(note_manager.notes) + 1, title, body, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            note_manager.add_note(note)
            print("Заметка добавлена")

        elif choice == "2":
            id = int(input("Введите идентификатор заметки: "))
            note = note_manager.get_note(id)
            if note:
                print("Заголовок:", note.title)
                print("Текст заметки:", note.body)
                print("Дата создания:", note.date)
            else:
                print("Заметка не найдена")

        elif choice == "3":
            id = int(input("Введите идентификатор заметки: "))
            note_manager.delete_note(id)
            print("Заметка удалена")

        elif choice == "4":
            notes = note_manager.get_all_notes()
            if len(notes) != 0:
                for note in notes:
                    print("Заголовок:", note.title)
                    print("Текст заметки:", note.body)
                    print("Дата создания:", note.date)
                    print()
            else:
                print("Заметок нет")

        elif choice == "5":
            id = int(input("Введите идентификатор заметки: "))
            note = note_manager.get_note(id)
            if note:
                title = input("Введите новый заголовок (или оставьте пустым): ")
                if title:
                    note.title = title
                body = input("Введите новый текст заметки (или оставьте пустым): ")
                if body:
                    note.body = body
                note_manager.update_note(note)
                print("Заметка обновлена")
            else:
                print("Заметка не найдена")

        elif choice == "6":
            notes = note_manager.get_all_notes()
            year = input("Введите год поика: ")
            month = input("Введите месяц поика: ")
            day = input("Введите день поика: ")
            date = year + '-' + month + '-' + day

            if len(notes) != 0:

                for note in notes:
                    notedate = note.date.split(' ')[0]
                    if notedate == date:
                        print("Заголовок:", note.title)
                        print("Текст заметки:", note.body)
                        print("Дата создания:", note.date)
                        print()
            else:
                print("Заметок нет")

        elif choice == "7":
            break

        else:
            print("Неправильный выбор")


if __name__ == "__main__":
    main()
