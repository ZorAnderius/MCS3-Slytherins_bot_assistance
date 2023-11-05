from colorama import Fore
from pathlib import Path
import os.path
from rich.console import Console

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
        user_input = input(Fore.CYAN + "Enter a command: ")
        if user_input:
            command, *args = parse_input(user_input)
            if command in ["close", "exit"]:
                print(Fore.BLUE + "Good bye!")
                break
            elif command == "hello":
                print(Fore.BLUE + "How can I help you?")
            elif command == "add-contact": #1
                print(add_contact(args, book))
            elif command == "add-phone": #1
                print(add_phone(args, book))
            elif command == "change-phone":#1
                print(change_phone(args, book))
            elif command == "add-email":#1
                print(add_email(args, book))
            elif command == "change-email":#1
                print(change_email(args, book))
            elif command == "add-address":#1
                print(add_address(args, book))
            elif command == "change-address": #1
                print(change_address(args, book))
            elif command == "phone":#1
                print(find_phone(args, book)[:-1:])
            elif command == "all-contacts": #1
                console.print(show_all(book))
            elif command == 'delete-contact': #1
                print (delete_record(args, book))
            elif command == "search-name": #1
                console.print(search_by_name(args, book))
            elif command == "search-phone": #1
                console.print(search_by_phone(args, book))
            elif command == "search-email": #1
                console.print(search_by_email(args, book))
            elif command == "remove-phone": #1
                print(remove_phone(args, book))
            elif command == "add-birthday": #1
                print(add_birthday(args, book))
            elif command == "show-birthday": #1
                print(show_birthday(args, book))
            elif command == "birthdays": #1
                console.print(show_all_birthdays(args, book))
            elif command == "add-note": #1
                print(add_note(args, notebook))
            elif command == "add-tag": #1
                print(add_tag(args, notebook))
            elif command == "change-title": #1
                print(change_note_title(args, notebook))
            elif command == "change-body":#1 
                print(change_note_body(args, notebook))
            elif command == "change-tag": #1
                print(change_note_tag(args, notebook))
            elif command == "delete-notes": #1
                print(delete_notes(args, notebook))
            elif command == "remove-note":  #1
                print(remove_note(args, notebook))
            elif command == "remove-body": #1
                print(remove_note_body(args, notebook))
            elif command == "remove-tag": #1
                print(remove_note_tag(args, notebook))
            elif command == "search-tag": #1
                console.print(search_by_tag(args, notebook))
            elif command == "search-author":#1
                console.print(search_by_author(args, notebook))
            elif command == "search-title": #1
                console.print(search_by_title(args, notebook))
            elif command == "sort-notes":#1
                console.print(sort_notes(notebook))
            elif command == "all-notes": #1
                console.print(show_all(notebook))
            else:
                print(Fore.YELLOW + "Invalid command")

    book.save_to_file(book_path)
    notebook.save_to_file(notebook_path)


if __name__ == "__main__":
    main()
