from collections import UserDict, defaultdict
from datetime import datetime

from .Note import Note


class NoteBook(UserDict):
    def __init__(self):
        super().__init__()

    @property
    def notebook(self):
        return self.data

    @notebook.setter
    def set_notebook(self, data):
        if data is not None:
            self.data = data
        else:
            raise ValueError("Data is empty")

    def add_book(self, data):
        pass

    def add_note(self, note):
        if note:
            if not note.created_at in self.data:
                self.data[note.id] = note
            else:
                return "Note is already done"

    def __repr__(self):
        string = ""
        for note in self.data.values():
            string += str(note) + "\n"
        return string[:-1:]


def show_all(book):
    general_str = ""
    for val, record in book.items():
        general_str += str(record)
    if general_str == "":
        return "Book is empty"
    return general_str[:-1:]


if __name__ == "__main__":
    notebook = NoteBook()
    note = Note()
    note.add_title("")
    note.add_body("It's my first program")
    notebook.add_note(note)
    # print(show_all(notebook))
    # time.sleep(30)
    note2 = Note()
    note2.add_title("my first program")
    note2.add_body("It's my first program")
    # print(note2.created_at == note.created_at)
    notebook.add_note(note2)
    print(show_all(notebook))
