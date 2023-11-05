from colorama import Fore
import copy

from pathlib import Path
from rich.table import Table
from rich.console import Console

from address_book_classes.Record import Record
from notes_classes.Note import Note

book_path = Path("address_book.json")
notebook_path = Path("note_book.json")


def added_contact(args, book):
    if len(args) == 1:
        name = args[0]
        try:
            phone = ""
            while True:
                try:
                    phone = input(Fore.BLUE + "Enter phone (n-close): ")
                    if phone == "n":
                        return Fore.YELLOW + "No changes saved."
                    if phone and type(phone) is str:
                        record = Record(name, phone)
                        book.add_record(record)
                        break
                    else:
                        print(Fore.RED + "Invalid text")
                except ValueError as e:
                    print(Fore.RED + str(e))
        except ValueError as e:
            return Fore.RED + str(e)
    else:
        return (
            Fore.RED
            + "Invalid format. Missing one of the arguments - name"
        )
    book.save_to_file(book_path)
    return Fore.GREEN + "Phone added."


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
    book.save_to_file(book_path)
    return Fore.GREEN + "Contact changed."


def find_phone(args, book):
    try:
        name = args[0]
        return book.find(name)
    except ValueError as e:
        return Fore.RED + str(e)


def show_all(book):
    if book:
        return book.show_book()
    else:
        return "[i]...Book is empty...[/i]"

def delete_record(args, book):
    name = args[0]
    try:
        contact = book.find(name)
        if contact:
            book.delete(name)  
            book.save_to_file(book_path)
            return Fore.GREEN + 'Record deleted.'
        else:
            return Fore.RED + 'Contact not found.'
    except ValueError as e:
        return Fore.RED + str(e)
    
def add_email(args, book):
    if len(args) == 1:
        name = args[0]
        try:
            contact = book.find(name)
            if contact and contact.email:
                return Fore.YELLOW + "Email already exists. Please use change email."
            new_email = ""
            while True:
                try:
                    new_email = input(Fore.BLUE + "Enter new email (n-close): ")
                    if new_email == "n":
                        return Fore.YELLOW + "No changes saved."
                    if new_email and type(new_email) is str:
                        contact.add_email(new_email)
                        break
                    else:
                        print(Fore.RED + "Invalid text")
                except ValueError as e:
                    print(Fore.RED + str(e))
        except ValueError as e:
            return Fore.RED + str(e)
    else:
        return (
            Fore.RED
            + "Invalid format. Missing one of the arguments - name"
        )
    book.save_to_file(book_path)
    return Fore.GREEN + "Email added."

def change_email(args,book):
    if len(args) == 1:
        name = args[0]
        try:
            contact = book.find(name)
            new_email = ""
            while True:
                try:
                    new_email = input(Fore.BLUE + "Enter new email (n-close): ")
                    if new_email == "n":
                        return Fore.YELLOW + "No changes saved."
                    if new_email and type(new_email) is str:
                        contact.change_email(new_email)
                        break
                    else:
                        print(Fore.RED + "Invalid text")
                except ValueError as e:
                    print(Fore.RED + str(e))
        except ValueError as e:
            return Fore.RED + str(e)
    else:
        return (
            Fore.RED
            + "Invalid format. Missing one of the arguments - name"
        )
    book.save_to_file(book_path)
    return Fore.GREEN + "Email changed."

def add_address(args, book):
    if len(args) == 1:
        name = args[0]
        try:
            contact = book.find(name)
            if contact and contact.address:
                return Fore.YELLOW + "Address already exists. Please use change address."
            new_address = ""
            while True:
                try:
                    new_address = input(Fore.BLUE + "Enter new address (n-close): ")
                    if new_address == "n":
                        return Fore.YELLOW + "No changes saved."
                    if new_address and type(new_address) is str:
                        contact.add_address(new_address)
                        break
                    else:
                        print(Fore.RED + "Invalid text")
                except ValueError as e:
                    print(Fore.RED + str(e))
        except ValueError as e:
            return Fore.RED + str(e)
    else:
        return (
            Fore.RED
            + "Invalid format. Missing one of the arguments - name"
        )
    book.save_to_file(book_path)
    return Fore.GREEN + "Address added."

def change_address(args, book):
    if len(args) == 1:
        name = args[0]
        try:
            contact = book.find(name)
            new_address = ""
            while True:
                try:
                    new_address = input(Fore.BLUE + "Enter new address (n-close): ")
                    if new_address == "n":
                        return Fore.YELLOW + "No changes saved."
                    if new_address and type(new_address) is str:
                        contact.change_address(new_address)
                        break
                    else:
                        print(Fore.RED + "Invalid text")
                except ValueError as e:
                    print(Fore.RED + str(e))
        except ValueError as e:
            return Fore.RED + str(e)
    else:
        return (
            Fore.RED
            + "Invalid format. Missing one of the arguments - name"
        )
    book.save_to_file(book_path)
    return Fore.GREEN + "Address changed."

def add_birthday(args, book):
    if len(args) == 4:
        name, day, month, year = args
        try:
            contact = book.find(name)

            contact.add_birthday(int(year), int(month), int(day))
        except ValueError as e:
            return Fore.RED + str(e)
        book.save_to_file(book_path)
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


def find_notes(args, book):
    try:
        name = args[0]
        return book.find(name)
    except ValueError as e:
        return Fore.RED + str(e)


def find_note(args, book):
    try:
        name, title = args[0]
        return book.find(name, title)
    except ValueError as e:
        return Fore.RED + str(e)
    
def search_by_tag(args, book):
    if len(args) == 1:
        tag = args[0]
        filter_book = book.search_by_tag(tag)
        return filter_book.show_book()
    else:
        return "[i]Invalid command[/i]"
    
def search_by_author(args, book):
    if len(args) == 1:
        tag = args[0]
        filter_book = book.search_by_author(tag)
        return filter_book.show_book()
    else:
        return "[i]Invalid command[/i]"
    
def search_by_title(args, book):
    if len(args) == 1:
        tag = args[0]
        filter_book = book.search_by_title(tag)
        return filter_book.show_book()
    else:
        return "[i]Invalid command[/i]"
    
def sort_notes(book):
    return book.sort_notes().show_book()


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
    book.save_to_file(notebook_path)
    return Fore.GREEN + "Note added."


def add_tag(args, book):
    if len(args) == 3:
        author, title, tag = args
        try:
            note = book.find_note(author, title)
            if tag and type(tag) is str:
                for note_tag in note.tags:
                    pass
                note.add_tag(tag)
        except ValueError as e:
            return Fore.RED + str(e)
    else:
        return Fore.RED + "Invalid format. Must be 3 arguments: name, title, new_tag"
    book.save_to_file(notebook_path)
    return Fore.GREEN + "Tag updated."


def change_note_title(args, book):
    if len(args) == 2:
        author, old_title = args
        try:
            note = book.find_note(author, old_title)
            new_title = ""
            while True:
                new_title = input(Fore.BLUE + "Enter new title (n-close): ")
                if new_title == "n":
                    return Fore.YELLOW + "No changes saved."
                if new_title and type(new_title) is str:
                    break
                else:
                    print(Fore.RED + "Invalid text")
            copy_note = copy.deepcopy(note)
            if new_title and type(new_title) is str:
                copy_note.edit_title(new_title)
                book.check_title(copy_note)
                note.edit_title(new_title)
            else:
                return Fore.YELLOW + "No changes saved."
        except ValueError as e:
            return Fore.RED + str(e)
    else:
        return (
            Fore.RED
            + "Invalid format. Missing one of the arguments: name, old_title or new_title"
        )
    book.save_to_file(notebook_path)
    return Fore.GREEN + "Title changed."


def change_note_body(args, book):
    if len(args) == 2:
        author, title = args
        try:
            note = book.find_note(author, title)
            while True:
                body = input(Fore.BLUE + "Enter note (n-close): ")
                if body == "n":
                    return Fore.YELLOW + "No changes saved."
                if body and type(body) is str:
                    note.edit_body(body)
                    break
                else:
                    print(Fore.RED + "Invalid text")
        except ValueError as e:
            return Fore.RED + str(e)
    else:
        return Fore.RED + "Invalid format. To change note body use next command - [change-body name]"
    book.save_to_file(notebook_path)
    return Fore.GREEN + "Note changed."


def change_note_tag(args, book):
    if len(args) == 3:
        author, title, old_tag = args
        try:
            note = book.find_note(author, title)
            while True:
                new_tag = input(Fore.BLUE + "Enter new tag (n-close): ")
                if new_tag == "n":
                    return Fore.YELLOW + "No changes saved."
                if new_tag and type(new_tag) == str:
                    try:
                        note.edit_tag(old_tag, new_tag)
                        break
                    except ValueError as e:
                        print(Fore.RED + f"{e}")
                else:
                    print(Fore.RED + "Invalid text")
        except ValueError as e:
            return Fore.RED + str(e)
    else:
        return (
            Fore.RED
            + "Invalid format. To change tag use next command - [change-tag name]"
        )
    book.save_to_file(notebook_path)
    return Fore.GREEN + "Tag changed."

def delete_notes(args, book):
    author = args[0]
    try:
        note = book.find_all_notes(author)
        if note:
            book.delete(author)  
            book.save_to_file(notebook_path)
            return Fore.GREEN + 'Notes deleted.'
        else:
            return Fore.RED + 'Notes not found.'
    except ValueError as e:
        return Fore.RED + str(e)


def remove_note(args, book):
    if len(args) == 2:
        author, title = args
        try:
            book.remove_note(author, title)
        except ValueError as e:
            return Fore.RED + str(e)
    else:
        return Fore.RED + "Invalid format. Missing one of the parameters: name, title"
    book.save_to_file(notebook_path)
    return Fore.GREEN + "Note deleted."


def remove_note_body(args, book):
    if len(args) == 2:
        author, title = args
        try:
            note = book.find_note(author, title)
            note.remove_body()
        except ValueError as e:
            return Fore.RED + str(e)
    else:
        return Fore.RED + "Invalid format. Missing one of the parameters: name, title"
    book.save_to_file(notebook_path)
    return Fore.GREEN + "Note body deleted."


def remove_note_tag(args, book):
    if len(args) == 3:
        author, title, tag = args
        try:
            note = book.find_note(author, title)
            note.remove_tag(tag)
        except ValueError as e:
            return Fore.RED + str(e)
    else:
        return Fore.RED + "Invalid format. Missing one of the parameters: name, title"
    book.save_to_file(notebook_path)
    return Fore.GREEN + "Note body deleted."

def search_by_name(args, book):
    if len(args) == 1:
        name_prefix = args[0]
        result = book.search_contacts_by_name(name_prefix)
        return display_search_results(result)
    else:
        return "Invalid format. Please provide a single argument for the name search."
        
def search_by_phone(args, book):
    if len(args) == 1:
        phone_prefix = args[0]
        result = book.search_contacts_by_phone(phone_prefix)
        return display_search_results(result)
    else:
        return "Invalid format. Please provide a single argument for the phone search."    
        
def search_by_email(args, book):
    if len(args) == 1:
        email = args[0]
        result = book.search_contacts_by_email(email)
        return display_search_results(result)
    else:
        return "Invalid format. Please provide a single argument for the email search."    


def remove_phone(args, book):
    if len(args) == 1:
        name = args[0]
        try:
            contact = book.find(name)
            if contact:
                print(Fore.CYAN + f"Contact information for {contact.name}:")
                search_results = {contact.name: contact}
                result = display_search_results(search_results)
    
                print(result)
                
                phone_to_remove = input("Please enter the phone number to be removed (n-close): ")
                if phone_to_remove == "n":
                    return Fore.YELLOW + "No changes made."
                if phone_to_remove:
                    phone_numbers = [phone.value for phone in contact.phones]
                    if phone_to_remove in phone_numbers:
                        contact.remove_phone(phone_to_remove)
                        print(Fore.GREEN + 'Phone number removed.')
                    else:
                        print(Fore.RED + 'Such phone number wasn\'t found.')
                else:
                    print(Fore.YELLOW + 'No changes made.')
            else:
                print(Fore.RED + 'Contact not found.')
        except ValueError as e:
            print(Fore.RED + str(e))
    else:
        print(
            Fore.RED
            + "Invalid format. The 'remove-phone' command should be in the format: remove-phone [name]"
        )




def display_search_results(results):
    if isinstance(results, str):
        return results
    else:
        table = Table(title="Search Results", style="blue", show_lines=True)
        table.add_column("Contact name", justify="center", style="green", min_width=20, no_wrap=True)
        table.add_column("Phones", style="yellow", justify="center", max_width=35, no_wrap=False)
        table.add_column("Email", justify="center", min_width=20, style="yellow")
        table.add_column("Birthday", justify="center", min_width=20, style="yellow")
        table.add_column("Address", justify="center", min_width=20, style="green")

        for key, record in results.items():
            phone_txt = "----" if record.phones is None else "; ".join(phone.value for phone in record.phones)
            email_txt = "----" if record.email is None else record.email.email
            birthday_txt = "----" if record.birthday is None else str(record.birthday)
            address_txt = "----" if record.address is None else record.address.address
            table.add_row(record.name.value.capitalize(), phone_txt, email_txt, birthday_txt, address_txt)
            
        console = Console()
        console.print(table)
        return ""