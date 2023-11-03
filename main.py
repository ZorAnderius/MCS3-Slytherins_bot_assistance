from colorama import Fore
from pathlib import Path
import os.path

from address_book_classes.AddressBook import AddressBook
from notes_classes.NoteBook import NoteBook
from user_interface.command_functions import *
from user_interface.parse_input import parse_input

path = Path("data.json")


def main():
    book = AddressBook()
    notebook = NoteBook()
    if os.path.exists(path):
        new_book = book.read_from_file(path)
        if new_book and type(new_book) is dict:
            book = book.add_book(new_book)
    while True:
        user_input = input(Fore.CYAN + "Enter a command: ")
        if user_input:
            command, *args = parse_input(user_input)
            if command in ["close", "exit"]:
                print(Fore.BLUE + "Good bye!")
                break
            elif command == "hello":
                print(Fore.BLUE + "How can I help you?")
            elif command == "add":
                print(added_contact(args, book))
            elif command == "change":
                print(change_contact(args, book))
            elif command == "phone":
                print(find_phone(args, book)[:-1:])
            elif command == "all-contacts":
                print(show_all(book))
            elif command == "add-birthday":
                print(add_birthday(args, book))
            elif command == "show-birthday":
                print(show_birthday(args, book))
            elif command == "birthdays":
                print(show_all_birthdays(args, book))
            elif command == "add-note":
                print(add_note(args, notebook))
            elif command == "change-title":
                print(change_note_title(args, notebook))
            elif command == "change-body":
                print(change_note_body(args, notebook))
            elif command == "change-tag":
                print(change_note_tag(args, notebook))
            elif command == "remove-note":
                print(remove_note(args, notebook))
            elif command == "remove-body":
                print(remove_note_body(args, notebook))
            elif command == "remove-tag":
                print(remove_note_tag(args, notebook))
            elif command == "all-notes":
                print(show_all(notebook))
            else:
                print(Fore.YELLOW + "Invalid command")

    book.save_to_file(path)


if __name__ == "__main__":
    main()
