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
            if note.author.value in self.data:
                self.data[note.author.value].append(note)
            else:
                self.data[note.author.value] = [note]
        else:
            raise ValueError("Invalid record")

    def __repr__(self):
        string = ""
        for note in self.data.values():
            string += str(note) + "\n"
        return string[:-1:]
