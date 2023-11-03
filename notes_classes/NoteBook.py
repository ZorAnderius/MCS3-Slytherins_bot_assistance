from collections import UserDict
from colorama import Fore

from .Title import Title
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
                self.data[note.author.value.lower()].append(note)
            else:
                self.data[note.author.value.lower()] = [note]
        else:
            raise ValueError("Invalid record")

    def find_all_notes(self, name):
        if not len(self.data):
            raise ValueError("Notebook is empty")
        if name in self.data:
            return self.data[name]
        else:
            raise ValueError("Note is not found")

    def find_note(self, name, title):
        notes = self.find_all_notes(name)
        return list(filter(lambda note: note.title.lower() == title.lower(), notes))[0]

    def remove_note(self, author, title):
        for _, notes in self.data.items():
            index = list(map(lambda x: str(x).lower(), notes)).index(title.lower())
            print(index)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def check_title(self, new_note):
        if (
            new_note
            and new_note.title
            and type(new_note.title) == str
            or type(new_note.title) == Title
        ):
            for author, notes in self.data.items():
                for note in notes:
                    if type(new_note.title) == Title:
                        if (
                            new_note.author.value.lower() == author.lower()
                            and new_note.title.title.lower() == note.title.lower()
                        ):
                            raise ValueError(
                                Fore.YELLOW
                                + f"Note with {new_note.title.title.upper()} title is already exist"
                            )

                    elif type(new_note.title) == str:
                        if (
                            new_note.author.value.lower() == author.lower()
                            and new_note.title.lower() == note.title.lower()
                        ):
                            raise ValueError(
                                Fore.YELLOW
                                + f"Note with {new_note.title.upper()} title is already exist"
                            )

    def __repr__(self):
        string = ""
        for note in self.data.values():
            string += str(note) + "\n"
        return string[:-1:]
