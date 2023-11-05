from collections import UserDict
from colorama import Fore
import json
from rich.table import Table
import re

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
                if not self.data or not author in self.data:                    
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
        table.add_column("Created at", justify="center", style="grey0", width=30)
        
        for key, notes in self.data.items():  
            for note in notes:
                tags_txt = "----" if note.tags is None or len(note.tags) == 0 else "; ".join(tag.tag for tag in note.tags)
                title_txt = "----" if note.title is None else note.title.title
                body_txt = "----" if note.body is None else note.body.body
                created_at_txt = "----" if note.created_at is None else note.created_at
                table.add_row(note.author.value.capitalize(),  title_txt, body_txt, tags_txt, created_at_txt)
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
        if notes and type(notes) is list:
            res = list(filter(lambda note: note.title.title.lower() == title.lower(), notes))
            if res:
                return res[0]
    
    def search_by_title(self, title):
        if title and type(title) is str:
            if len(title) <= 2:
                return "[i]At least two characters are required for search[/i]"
            filter_book = NoteBook()
            for _, notes in self.data.items():
                for note in notes:
                    if re.findall(title, note.title.title, re.IGNORECASE):
                        filter_book.add_note(note)
            return filter_book
    
    def search_by_author(self, author):
        filter_book = NoteBook()
        for _, notes in self.data.items():
            for note in notes:
                if re.findall(author, note.author.value, re.IGNORECASE):
                    filter_book.add_note(note)
        return filter_book
    
    def search_by_tag(self, tag):
        filter_book = NoteBook()
        for _, notes in self.data.items():
            for note in notes:
                if list(filter(lambda note_tag: re.findall(tag, note_tag.tag, re.IGNORECASE), note.tags)):
                    filter_book.add_note(note)
        return filter_book
    
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
                            
    def sort_notes(self):
        temp_dict = NoteBook()
        if len(self.data):
            for key, notes in self.data.items():
                for note in notes:
                    str_syb_tags = "".join(tag.tag for tag in note.tags)
                        
                    if len(str_syb_tags) in temp_dict:
                        temp_dict[len(str_syb_tags)].append(note)
                    else: 
                        temp_dict[len(str_syb_tags)] = [note]
        if  temp_dict:
            sort_key = sorted(temp_dict.keys())
            sorted_dict = NoteBook()
            for key in sort_key:
                sorted_dict[key] = temp_dict[key]
            return sorted_dict
        else:
            return "[i]...NoteNook is empty...[/i]"

    def __repr__(self):
        string = ""
        for note in self.data.values():
            string += str(note) + "\n"
        return string[:-1:]
