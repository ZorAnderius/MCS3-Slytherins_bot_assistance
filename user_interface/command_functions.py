from colorama import Fore

from address_book_classes.Record import Record
from notes_classes.Note import Note


def added_contact(args, book):
    try:
        name, phone = args
        record = Record(name, phone)
        book.add_record(record)
    except ValueError as e:
        return Fore.RED + str(e)
    return Fore.GREEN + "Contact added."


def change_contact(args, book):
    if len(args) == 3:
        name, old_phone, new_phone = args
        try:
            contact = book.find(name)
            contact.edit_phone(old_phone, new_phone)
        except ValueError as e:
            return Fore.RED + str(e)
    else:
        return (
            Fore.RED
            + "Invalid format. To change phone use next command - [change name old_phone new_phone]"
        )
    return Fore.GREEN + "Contact changed."


def find_phone(args, book):
    try:
        name = args[0]
        return book.find(name)
    except ValueError as e:
        return Fore.RED + str(e)


def show_all(book):
    general_str = ""
    for key, value in book.items():
        if type(value) == list:
            author_title = Fore.CYAN + f"\nAuthor:"
            author_name = Fore.YELLOW + f"{key}"
            author_notes = "".join([str(note) for note in value])
            general_str += "{:}{:>10}{:^100}".format(
                author_title, author_name, author_notes
            )
        else:
            general_str += str(value)
    if general_str == "":
        return Fore.YELLOW + "Book is empty"
    return general_str[:-1:]


def add_birthday(args, book):
    if len(args) == 4:
        name, day, month, year = args
        try:
            contact = book.find(name)

            contact.add_birthday(int(year), int(month), int(day))
        except ValueError as e:
            return Fore.RED + str(e)
        return Fore.GREEN + "Birthday was added."


def show_birthday(args, book):
    name = args[0]
    try:
        contact = book.find(name)
        return contact.birthday
    except ValueError as e:
        return Fore.RED + str(e)


def show_all_birthdays(args, book):
    try:
        time = args[0]
        birth_str = ""
        birthday_dict = book.get_birthdays_per_time(int(time))
        if type(birthday_dict) is not dict:
            raise ValueError(birthday_dict)
    except ValueError as e:
        return Fore.YELLOW + str(e)
    except IndexError:
        return Fore.RED + "Missing arguments"
    for _, value in birthday_dict.items():
        for weekday, names in value.items():
            weekdey_str = Fore.BLUE + "{: >10}".format(weekday)
            names_str = Fore.YELLOW + "{: <10}".format(", ".join(names))
            birth_str += f"{weekdey_str} : {names_str}\n"
    return birth_str[:-1:]


def add_note(args, book):
    try:
        author = args[0]
        note = Note(author)
        note.input_title()
        book.check_title(note)
        note.input_body()
        note.input_tag()
        book.add_note(note)
    except ValueError as e:
        return Fore.RED + str(e)
    return Fore.GREEN + "Note added."


def change_note_title(args, book):
    if len(args) == 3:
        name, old_phone, new_phone = args
        try:
            contact = book.find(name)
            contact.edit_phone(old_phone, new_phone)
        except ValueError as e:
            return Fore.RED + str(e)
    else:
        return (
            Fore.RED
            + "Invalid format. To change phone use next command - [change name old_phone new_phone]"
        )
    return Fore.GREEN + "Contact changed."


def change_note_body(args, book):
    pass


def change_note_tag(args, book):
    if len(args) == 3:
        name, old_phone, new_phone = args
        try:
            contact = book.find(name)
            contact.edit_phone(old_phone, new_phone)
        except ValueError as e:
            return Fore.RED + str(e)
    else:
        return (
            Fore.RED
            + "Invalid format. To change phone use next command - [change name old_phone new_phone]"
        )
    return Fore.GREEN + "Contact changed."
