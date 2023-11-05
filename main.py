from colorama import Fore
from pathlib import Path
import os.path
import sys
from rich.console import Console
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

from address_book_classes.AddressBook import AddressBook
from notes_classes.NoteBook import NoteBook
from user_interface.command_functions import *
from user_interface.parse_input import parse_input

book_path = Path("address_book.json")
notebook_path = Path("note_book.json")


def main():
    book = AddressBook()
    notebook = NoteBook()
    console = Console()

    if os.path.exists(book_path):
        new_book = book.read_from_file(book_path)
        if new_book and type(new_book) is dict:
            book = book.add_book(new_book)

    if os.path.exists(notebook_path ):
        new_notebook = notebook.read_from_file(notebook_path )
        if new_notebook and type(new_notebook) is dict:
            notebook = notebook.add_book(new_notebook)

    while True:
        user_input = prompt("Say the spell: ", completer=command_completer(),)
        if user_input:
            command, *args = parse_input(user_input)

            handle_command(command, args, book, notebook, console, book_path, notebook_path)

def command_completer():
    book_commands = [
    "add-contact",
    "add-phone",
    "change-phone",
    "add-email",
    "change-email",
    "add-address",
    "change-address",
    "phone",
    "all-contacts",
    "delete-contact",
    "search-name",
    "search-phone",
    "search-email",
    "remove-phone",
    "add-birthday",
    "show-birthday",
    "birthdays",
    'close',
    'exit'
    ]
    notebook_commands = [
    "add-note",
    "add-tag",
    "change-title",
    "change-body",
    "change-tag",
    "delete-notes",
    "remove-note",
    "remove-body",
    "remove-tag",
    "search-tag",
    "search-author",
    "search-title",
    "sort-notes",
    "all-notes",
    ]
    commands = book_commands + notebook_commands
    return WordCompleter(commands)

def handle_command(command, args, book, notebook, console, book_path, notebook_path):
    if command in ["close", "exit"]:
        print(Fore.BLUE + "Good bye!")
        book.save_to_file(book_path)
        notebook.save_to_file(notebook_path)
        sys.exit(0)
    elif command == "hello":
        print(Fore.BLUE + "Hi! I am Voldebot! What kind of magic shall we do today?")
    elif command == "add-contact":
        print(add_contact(args, book))
    elif command == "add-phone":
        print(add_phone(args, book))
    elif command == "change-phone":
        print(change_phone(args, book))
    elif command == "add-email":
        print(add_email(args, book))
    elif command == "change-email":
        print(change_email(args, book))
    elif command == "add-address":
        print(add_address(args, book))
    elif command == "change-address": 
        print(change_address(args, book))
    elif command == "phone":
        print(find_phone(args, book)[:-1:])
    elif command == "all-contacts": 
        console.print(show_all(book))
    elif command == 'delete-contact': 
        print (delete_record(args, book))
    elif command == "search-name": 
        console.print(search_by_name(args, book))
    elif command == "search-phone": 
        console.print(search_by_phone(args, book))
    elif command == "search-email": 
        console.print(search_by_email(args, book))
    elif command == "remove-phone": 
        print(remove_phone(args, book))
    elif command == "add-birthday": 
        print(add_birthday(args, book))
    elif command == "show-birthday": 
        print(show_birthday(args, book))
    elif command == "birthdays": 
        console.print(show_all_birthdays(args, book))
    elif command == "add-note": 
        print(add_note(args, notebook))
    elif command == "add-tag": 
        print(add_tag(args, notebook))
    elif command == "change-title": 
        print(change_note_title(args, notebook))
    elif command == "change-body": 
        print(change_note_body(args, notebook))
    elif command == "change-tag": 
        print(change_note_tag(args, notebook))
    elif command == "delete-notes": 
        print(delete_notes(args, notebook))
    elif command == "remove-note":  
        print(remove_note(args, notebook))
    elif command == "remove-body": 
        print(remove_note_body(args, notebook))
    elif command == "remove-tag": 
        print(remove_note_tag(args, notebook))
    elif command == "search-tag": 
        console.print(search_by_tag(args, notebook))
    elif command == "search-author":
        console.print(search_by_author(args, notebook))
    elif command == "search-title": 
        console.print(search_by_title(args, notebook))
    elif command == "sort-notes":
        console.print(sort_notes(notebook))
    elif command == "all-notes": 
        console.print(show_all(notebook))
    else:
        print(Fore.YELLOW + "Invalid spall")

    book.save_to_file(book_path)
    notebook.save_to_file(notebook_path)


if __name__ == "__main__":
    main()
