from collections import UserDict
from colorama import Fore
import json
from rich.table import Table

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
        for author, notes in data.items():  
            for note in notes:
                author = note['author'] if "author" in note else None
                title = note['title'] if "title" in note else None
                tags = note['tags'] if "tags" in note else None
                body = note['body'] if "body" in note else None
                created_at = note['created_at'] if "created_at" in note else None
                new_note = Note(author)
                if new_note:
                    if title:
                        new_note.add_title(title)
                    if tags and len(tags):
                        new_note.add_tags(tags)
                    if body :       
                        new_note.add_body(body)
                    if created_at:
                        new_note.add_created_at(created_at)    
                if not self.data:                    
                    self.data[author] = [new_note]
                else:
                    self.data[author].append(new_note)
        return self
    
    def serialize(self):
        nested_dict = dict()
        if len(self.data):
            for key, notes in self.data.items():
                nested_dict[key] = [note.serialize() for note in notes]

        return {'data': nested_dict}

    def de_serialize(self, data):
        new_book = data['data']
        return new_book

    def save_to_file(self, filename=''):
        if filename:
            with open(filename, 'w') as f_write:
                json.dump(self.serialize(), f_write)

    def read_from_file(self, filename):
        if filename:
            with open(filename, 'r') as f_read:
                try:
                    res = json.load(f_read)
                except ValueError as e:
                    return str(e)
                except:
                    return None
                if len(res):
                    res = self.de_serialize(res)
                return res
            
    def show_book(self):
        table = Table(title="NoteBook",style="blue", show_lines=True)

        table.add_column("Author", justify="center", style="green",min_width=20, no_wrap=True)
        table.add_column("Title", style="yellow", justify="center", max_width=35, no_wrap=False)
        table.add_column("Note", justify="center",min_width=20, style="yellow")
        table.add_column("Tags", justify="center",min_width=20, style="yellow")
        table.add_column("Created at", justify="center",min_width=20, style="grey0")
        
        for key, notes in self.data.items():  
            for note in notes:
                tags_txt = "----" if note.tags is None else "; ".join(tag.tag for tag in note.tags)
                title_txt = "----" if note.title is None else note.title.title
                body_txt = "----" if note.body is None else note.body.body
                created_at_txt = "----" if note.created_at is None else note.created_at
                table.add_row(key.capitalize(),  title_txt, body_txt, tags_txt, created_at_txt)
        return table

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
        return list(filter(lambda note: note.title.title.lower() == title.lower(), notes))[0]
    
    def remove_note(self, author, title):
        if author in self.data:
            notes = self.find_all_notes(author)
            note = self.find_note(author, title)
            index = notes.index(note)
            if index >= 0:
                notes.pop(index)

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
                            and new_note.title.title.lower() == note.title.title.lower()
                        ):
                            raise ValueError(
                                Fore.YELLOW
                                + f"Note with {new_note.title.title.upper()} title is already exist"
                            )

                    elif type(new_note.title) == str:
                        if (
                            new_note.author.value.lower() == author.lower()
                            and new_note.title.lower() == note.title.title.lower()
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
