from colorama import Fore
import copy

from pathlib import Path


from address_book_classes.Record import Record
from address_book_classes.AddressBook import AddressBook
from notes_classes.Note import Note

book_path = Path("address_book.json")
notebook_path = Path("note_book.json")


def add_contact(args, book):
    if len(args) == 1:
        try:
            name = args[0]
            if name in book:
                return Fore.YELLOW + "Contacts is already exist"
            record = Record(name)
            record.input_phones()
            record.input_email()
            record.input_birthday()
            record.input_address()
            book.add_record(record)
        except ValueError as e:
            return Fore.RED + str(e)
    book.save_to_file(book_path)
    return Fore.GREEN + "Contact added."

def add_phone(args, book):
    if len(args) == 1:
        name = args[0]
        try:
            contact = book.find(name)
            contact.input_phones()
        except ValueError as e:
            return Fore.RED + str(e)
    else:
        return Fore.RED + "Invalid format. To add phone use next spell- [add-phone name]"
    book.save_to_file(notebook_path)
    return Fore.GREEN + "Phone added."


def change_phone(args, book):
    if len(args) == 1:
        name= args[0]
        old_phone = None
        new_phone = None
        try:
            contact = book.find(name)
            while True:
                try:
                    if not old_phone:
                        old_phone = input(Fore.BLUE + "Say old phone (n-close): ")
                    if old_phone == 'n':
                        return Fore.YELLOW + "Phone didn't change"
                    if not list(filter(lambda phone: phone.value == old_phone,contact.phones)):
                        old_phone = None
                        print(Fore.YELLOW + "Phone does not exist")
                        continue
                    new_phone = input(Fore.BLUE + "Say new phone (n-close): ")
                    if new_phone == 'n':
                        return Fore.YELLOW + "Phone didn't change"
                    if new_phone == old_phone or list(filter(lambda phone: phone.value == new_phone, contact.phones)):
                        new_phone = None
                        print(Fore.YELLOW + "Phone already exist")
                        continue
                    if new_phone and old_phone:
                        contact.edit_phone(old_phone, new_phone)
                        break
                except ValueError as e:
                    print(Fore.RED + str(e))
        except ValueError as e:
            return Fore.RED + str(e)
    else:
        return (
            Fore.RED
            + "Invalid format. To change phone use next spell - [change-phone name]"
        )
    book.save_to_file(book_path)
    return Fore.GREEN + "Phone changed."


def find_phone(args, book):
    if len(args) == 1:
        try:
            name = args[0]
            return book.find(name)
        except ValueError as e:
            return Fore.RED + str(e)
    else:
        return (
            Fore.RED
            + "Invalid format. Spell format - [phone phone]"
        )


def show_all(book):
    if book:
        return book.show_book()
    else:
        return "[i]...Book is empty...[/i]"

def delete_record(args, book):
    if len(args) == 1:
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
    else:
        return (
            Fore.RED
            + "Invalid format. Spell format - [delete-contact name]"
        )
    
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
                    new_email = input(Fore.BLUE + "Say new email (n-close): ")
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
            + "Invalid format. Spell format - [add-address name]"
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
                    new_email = input(Fore.BLUE + "Say new email (n-close): ")
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
            + "Invalid format. Spell format - [change-email name]"
        )
    book.save_to_file(book_path)
    return Fore.GREEN + "Email changed."

def add_address(args, book):
    if len(args) == 1:
        name = args[0]
        try:
            contact = book.find(name)
            if contact and contact.address:
                return Fore.YELLOW + "Address already exists. Please use change address spell."
            new_address = ""
            while True:
                try:
                    new_address = input(Fore.BLUE + "Say new address (n-close): ")
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
            + "Invalid format. Spell format - [add-address name]"
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
                    new_address = input(Fore.BLUE + "Say new address (n-close): ")
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
            + "Invalid format. Spell format - [change-address name]"
        )
    book.save_to_file(book_path)
    return Fore.GREEN + "Address changed."

def add_birthday(args, book):
    if len(args) == 1:
        name = args[0]
        try:
            contact = book.find(name)
            contact.input_birthday()
            if not contact.birthday:
                return Fore.YELLOW + "Birthday didn't save. Dark Lord will be unhappy"
        except ValueError as e:
            return Fore.RED + str(e)
        book.save_to_file(book_path)
        return Fore.GREEN + "Birthday was added."
    else:
        return (
            Fore.RED
            + "Invalid format. Spell format - [add-birthday name]"
        )


def show_birthday(args, book):
    if len(args) == 1:
        name = args[0]
        try:
            contact = book.find(name)
            if contact and not contact.birthday:
                return f"{contact.name.value.capitalize()}'s birthday is not available."
            return f"{contact.name.value.capitalize()} birthday is on {contact.birthday}"
        except ValueError as e:
            return Fore.RED + str(e)
    else:
        return (
            Fore.RED
            + "Invalid format. Spell format - [show-birthday name]"
        )


def show_all_birthdays(args, book):
    if len(args) == 1:
        try:
            time = args[0]
            birthday_book = book.get_birthdays_per_time(int(time))
            if type(birthday_book) is not AddressBook:
                raise ValueError(birthday_book)
        except ValueError as e:
            return f'[i]{str(e)}[/i]'
        except IndexError:
            return Fore.RED + "Missing arguments. Spell format - [birthday days]"
    else:
        return "[i]Invalid format. Spell format - birthdays day[/i]"
    
    return birthday_book.show_book()


def find_notes(args, book):
    if len(args) == 1:
        try:
            name = args[0]
            return book.find(name)
        except ValueError as e:
            return Fore.RED + str(e)
    else:
        return "[i]Invalid command[/i]"


def find_note(args, book):
    if len(args) == 2:
        try:
            name, title = args[0]
            return book.find(name, title)
        except ValueError as e:
            return Fore.RED + str(e)
    else:
        return (
            Fore.RED
            + "Invalid format. Spell format - [search-tag tag]"
        )
    
def search_by_tag(args, book):
    if len(args) == 1:
        tag = args[0]
        filter_book = book.search_by_tag(tag)
        return filter_book.show_book()
    else:
        return ("[i]Invalid format. Spell format - [search-tag tag][/i]")
    
def search_by_author(args, book):
    if len(args) == 1:
        tag = args[0]
        filter_book = book.search_by_author(tag)
        return filter_book.show_book()
    else:
        return ("[i]Invalid format. Spell format - [search-author author][/i]")
    
def search_by_title(args, book):
    if len(args) == 1:
        tag = args[0]
        filter_book = book.search_by_title(tag)
        return filter_book.show_book()
    else:
        return ("[i]Invalid format. Spell format - [search-title title][/i]")
    
def sort_notes(book):
    return book.sort_notes().show_book()

def add_note(args, book):
    if len(args) == 1:
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
    else:
        return (
            Fore.RED
            + "Invalid format. Spell format - [add-note author]"
        )
    return Fore.GREEN + "Note added."

def add_tag(args, book):
    if len(args) == 1:
        author = args[0]
        try:
            note = book.find_all_notes(author)[0]
            note.input_tag()
        except ValueError as e:
            return Fore.RED + str(e)
    else:
        return Fore.RED + "Invalid format. Spell format - [add-tag author]"
    book.save_to_file(notebook_path)
    return Fore.GREEN + "Tag updated."

def change_note_title(args, book):
    if len(args) == 1:
        author = args[0]
        try:
            note = book.find_all_notes(author)[0]
            while True:
                new_title = input(Fore.BLUE + "Say new title (n-close): ")
                if new_title == "n":
                    return Fore.YELLOW + "No changes saved. Nagini is hungry "
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
            + "Invalid format. Spell format - [change-title author]"
        )
    book.save_to_file(notebook_path)
    return Fore.GREEN + "Title changed."

def change_note_body(args, book):
    if len(args) == 1:
        author = args[0]
        title = None
        body = None
        note = None
        while True:
            try:
                if not title:
                    title = input(Fore.BLUE + "Say title (n-close):")
                if title == "n":
                    return Fore.YELLOW + "No changes saved."
                if title:
                    note = book.find_note(author,title)
                if note is None:
                    raise ValueError(Fore.RED + "Invalid title")
                body = input(Fore.BLUE + "Say note (n-close): ")
                if body == "n":
                    return Fore.YELLOW + "No changes saved."
                if body and type(body) is str and note:
                    note.edit_body(body)
                    break
                else:
                    print(Fore.RED + "Invalid text")
            except ValueError as e:
                print(Fore.RED + str(e))
                title = None
                continue
    else:
        return Fore.RED + "Invalid format. To change note body use next spell - [change-body name]"
    book.save_to_file(notebook_path)
    return Fore.GREEN + "Note changed."

def change_note_tag(args, book):
    if len(args) == 1:
        author= args[0]
        title = None
        old_tag = None
        new_tag = None
        while True:
            try:
                if not title:
                    title = input(Fore.BLUE + "Say title (n-close):")
                if title == "n":
                        return Fore.YELLOW + "No changes saved."
                if title:
                    note = book.find_note(author,title)
                if note is None:
                    raise ValueError(Fore.RED + "Invalid title")
                if not old_tag:
                    old_tag = input(Fore.BLUE + "Say old tag (n-close):")
                if old_tag == "n":
                        return Fore.YELLOW + "No changes saved."
                if not (list(filter(lambda x: x.tag == old_tag, note.tags))):
                    old_tag = None
                    print(Fore.RED + "Wrong tag. Try again")
                    continue
            
                new_tag = input(Fore.BLUE + "Say new tag (n-close): ")
                if new_tag == "n":
                    return Fore.YELLOW + "No changes saved."
                if old_tag and new_tag and type(new_tag) == str and note:
                    try:
                        note.edit_tag(old_tag, new_tag)
                        break
                    except ValueError as e:
                        print(Fore.RED + f"{e}")
                else:
                    print(Fore.RED + "Invalid text")
            except ValueError as e:
                title = None
                print(Fore.RED + str(e))
    else:
        return (
            Fore.RED
            + "Invalid format. To change tag use next spell - [change-tag name]"
        )
    book.save_to_file(notebook_path)
    return Fore.GREEN + "Tag changed."

def delete_notes(args, book):
    if len(args) == 1:
        author = args[0]
        try:
            note = book.find_all_notes(author)
            if note:
                book.delete(author)  
                book.save_to_file(notebook_path)
                return Fore.GREEN + 'Notes deleted. Harry Potter is happy'
            else:
                return Fore.RED + 'Notes not found.'
        except ValueError as e:
            return Fore.RED + str(e)
    return (
            Fore.RED
            + "Invalid format. To delete note use next spell - [delete-note author]"
        )

def remove_note(args, book):
    if len(args) == 1:
        author = args[0]
        while True:
            try:
                title = input(Fore.BLUE + "Say title (n-close):")
                if title == "n":
                        return Fore.YELLOW + "No changes saved."
                if title:
                    book.remove_note(author, title)
                    break
            except ValueError as e:
                print(Fore.RED + str(e))
    else:
        return Fore.RED + "Invalid format. Spell format - [remove-note author]"
    book.save_to_file(notebook_path)
    return Fore.GREEN + "Note deleted."


def remove_note_body(args, book):
    if len(args) == 1:
        author = args[0]
        while True:
            try:
                title = input(Fore.BLUE + "Say title (n-close):")
                if title == "n":
                        return Fore.YELLOW + "No changes saved."
                if title:
                    note = book.find_note(author, title)
                    if note:
                        note.remove_body()
                        break
                    print(Fore.RED + "Wrong title.Haven't received Crucio in a long time?")
            except ValueError as e:
                return Fore.RED + str(e)
    else:
        return Fore.RED + "Invalid format. Spell format - [remove-body author]"
    book.save_to_file(notebook_path)
    return Fore.GREEN + "Note body deleted."


def remove_note_tag(args, book):
    if len(args) == 1:
        author= args[0]
        title = None
        tag = None
        note = None
        
        while True:
            try:
                if not title:
                    title = input(Fore.BLUE + "Say title (n-close):")
                if title == "n":
                        return Fore.YELLOW + "No changes saved."
                if title:
                    note = book.find_note(author,title)
                if not note:
                    raise ValueError("Wrong title")
                    
                if not tag:
                    tag = input(Fore.BLUE + "Say old tag (n-close):")
                if tag == "n":
                        return Fore.YELLOW + "No changes saved."
                
                if not (list(filter(lambda x: x.tag == tag, note.tags))):
                    tag = None
                    print(Fore.RED + "Wrong tag. Try again muggle!")
                    continue
                
                if note and tag:
                    note.remove_tag(tag)
                    break
            except ValueError as e:
                title = None
                print(Fore.RED + str(e))
    else:
        return Fore.RED + "Invalid format. Spell format - [remove-tag author]"
    book.save_to_file(notebook_path)
    return Fore.GREEN + f"Tag deleted."

def search_by_name(args, book):
    if len(args) == 1:
        name_prefix = args[0]
        filter_book = book.search_contacts_by_name(name_prefix)
        if filter_book and type(filter_book) is AddressBook:
            return filter_book.show_book()
        else:
            return "[i]No contact found with this name[/i]"
    else:
        return "[i]Invalid format. Please provide a single argument for the name search.[/i]"  
        
def search_by_phone(args, book):
    if len(args) == 1:
        phone_prefix = args[0]
        filter_book = book.search_contacts_by_phone(phone_prefix)
        return filter_book.show_book()
    else:
        return "[i]Invalid format. Please provide a single argument for the phone search.[/i]"    
        
def search_by_email(args, book):
    if len(args) == 1:
        email = args[0]
        filter_book = book.search_contacts_by_email(email)
        if filter_book and type(filter_book) is AddressBook:
            return filter_book.show_book()
        else:
            return "[i]No contact found with this email[/i]"
    else:
        return "[i]Invalid format. Please provide a single argument for the email search.[/i]"    


def remove_phone(args, book):
    if len(args) == 1:
        name = args[0]
        try:
            contact = book.find(name)
            if contact:
                while True:
                    phone_to_remove = input("Say phone number (n-close): ")
                    if phone_to_remove == "n":
                        return Fore.YELLOW + "No changes made."
                    
                    if phone_to_remove:
                        phone_numbers = [phone.value for phone in contact.phones]
                        if phone_to_remove in phone_numbers:
                            contact.remove_phone(phone_to_remove)
                            return Fore.GREEN + 'Phone number removed.'
                        else:
                            print(Fore.RED + 'Such phone number wasn\'t found.')
                    else:
                        print(Fore.YELLOW + 'Invalid phone.')
            else:
                return Fore.RED + 'Contact not found.'
        except ValueError as e:
            return Fore.RED + str(e)
    else:
        return Fore.RED + "Invalid format. Spell format: [remove-phone name]"
        