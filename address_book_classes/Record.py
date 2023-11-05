from datetime import datetime
from colorama import Fore
from rich.table import Table

from .Name import Name
from .Phone import Phone
from .Birthday import Birthday
from .Email import Email
from .Address import Address
from .Email import Email

class Record:
    def __init__(self, name: str, phone: str = "", *birthday: (int, int, int), email: str="", address: str = ""):
        self.__name = Name(name)

        if phone:
            phone = Phone(phone)
            self.__phones = [phone]
        else:
            self.__phones = []

        if birthday and len(birthday) == 3:
            year, month, day = birthday
            self.__birthday = Birthday(year, month, day)
        else:
            self.__birthday = None
            
        if email and type(email) is str:
            self.__email = Email(email)
        else: 
            self.__email = None
            
        if address and type(address) is str:
            self.__address = Address(address)
        else: 
            self.__address = None


    def serialize(self):
        return {
            "name": self.name.serialize(),
            "phones": [phone.serialize() for phone in self.phones],
            "birthday": self.birthday.serialize() if self.birthday else None,
            "email": self.email.serialize() if self.email else None,
            'address': self.address.serialize() if self.address else None
        }

    @property
    def name(self) -> Name:
        return self.__name

    @name.setter
    def set_name(self, name: str):
        self.__name = Name(name)

    @property
    def phones(self) -> list[Phone]:
        return self.__phones

    @phones.setter
    def set_phones(self, phones: list[Phone]):
        if phones:
            self.__phones = phones
        else:
            self.__phones = []
    
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def set_email(self, email):
        if email and type(email) is str:
            temp_email = Email(email)
            self.__email = temp_email

    @property
    def birthday(self) -> datetime:
        return self.__birthday

    def set_birthday(self, birthday: datetime):
        if birthday:
            self.__birthday = birthday
        else:
            self.__birthday = None

    @property
    def address(self) -> Address:
        return self.__address

    @address.setter
    def set_address(self, address: str):
        self.__address = Address(address)


    @property
    def emails(self) -> Email:
        return self.__emails
        
    def set_emails(self, emails: str):
        self.__emails = Email(emails)

    def __str__(self) -> str:
        if self.phones:  
            str1 = Fore.YELLOW + "Contact name: "
            str2 = Fore.LIGHTMAGENTA_EX + str(self.name)
            str3 = Fore.YELLOW + "phones: "
            str4 = Fore.WHITE + '; '.join(phone.value for phone in self.phones)
            return "{0}{1: <15} {2}\n".format(str1,  str2, (str3 + str4))
        if not self.phones and self.name.name is None:   
            return 'None'
        return "{0}{1: <15}: Phonebook is empty\n".format(str1,  str2)

    def search_contacts(self, keyword: str):
        keyword = keyword.lower()
        results = []

        for contact in self.contacts:
            contact_name = contact.name.name.lower()
            for phone in contact.phones:
                phone_number = phone.value.lower()
            for email in contact.emails:
                email_address = email.address.lower()
            birthday_date = str(contact.birthday.birthday) if contact.birthday else ""

            if (self.check_prefix(contact_name, keyword) or
                self.check_prefix(phone_number, keyword) or
                self.check_prefix(email_address, keyword) or
                self.check_prefix(birthday_date, keyword)):
                results.append(contact)

        return results
    
    def check_prefix(self, text, prefix):
        if len(prefix) >= 2 and text.startswith(prefix):
            return True
        return False
    
    def search(self, keyword: str):
        search_results = self.search_contacts(keyword)
        if search_results:
            print(f"Search results for '{keyword}':")
            for result in search_results:
                print(result)
        else:
            print(f"No results found for '{keyword}'.")

    def __str__(self) -> str:    
        if self.phones:
            str1 = Fore.YELLOW + "Contact name: "
            str2 = Fore.LIGHTMAGENTA_EX + str(self.name)
            str3 = Fore.YELLOW + "phones: "
            str4 = Fore.WHITE + "; ".join(phone.value for phone in self.phones)
            str5 = Fore.YELLOW + "address: "
            str6 = Fore.WHITE + str(self.address)
            return "{0}{1: <15} {2}\n{3}{4: <15} {5}{6}n".format(str1, str2, str3, str4, str5, str6)
        if not self.phones and self.name.name is None:
            return "None"
        return "{0}{1: <15}: Phonebook is empty\n".format(str1, str2)


    def add_phones(self, phones):
        self.__phones = [Phone(phone) for phone in phones]

    def add_phone(self, phone: str):
        new_phone = Phone(phone)
        if new_phone.phone in self.phones:
            raise ValueError(
                Fore.YELLOW
                + f"Phone {phone} is already in your phonebook. If you want to change phone use 'change' operation"
            )
        elif new_phone.phone:
            self.__phones.append(new_phone)

    def find_phone(self, phone: str) -> str or None:
        if list(filter(lambda p: p.value == phone, self.phones)):
            return phone

    def remove_phone(self, phone: str) -> int or None:
        if self.find_phone(phone):
            index = list(map(str, self.phones)).index(phone)
            del self.phones[index]
            return index
        
    def delete_record(self, phone: str) -> str:
            index = self.find_phone(phone)

            if index is not None:
                del self.phones[index]
                
                # Check if there are no more phone numbers for this record
                if not self.phones:
                    # If there are no more phone numbers, also remove the name and birthday
                    self.__name = Name("")  
                    self.__birthday = None  

                return f"Record for {self.name} with phone {phone} deleted."

            return f"No record found for phone {phone}."
       

    def edit_phone(self, old_phone: str, new_phone: str):
        new_phone = Phone(new_phone)
        if new_phone.phone:
            if self.find_phone(old_phone):
                index = self.remove_phone(old_phone)
                if index >= 0:
                    self.phones.insert(index, new_phone)
            else:
                raise ValueError(
                    f"Phone number {old_phone} is not in the {self.name} record list"
                )

    def add_birthday(self, *birthday: (int, int, int)):
        if birthday and len(birthday) == 3:
            year, month, day = birthday
            if self.__birthday:
                raise ValueError("You cannot change existing birthday")
            self.__birthday = Birthday(year, month, day)
            if self.__birthday is None:
                raise ValueError("Invalid date format")
        else:
            raise ValueError("Invalid date format")

    def add_address(self, address: str):
        if address and type(address) is str:
            temp_address = Address(address)
            if temp_address:
                print(temp_address)
                if self.__address :
                    raise ValueError(Fore.YELLOW + "Address already exists. Please use change email.")
                self.__address = temp_address
                return f"Address added: {address}"

    def change_address(self, address: str):
        if address and type(address) is str:
            if self.__address and self.__address.get_address() == address:
                raise ValueError(Fore.YELLOW + "The new address is the same as the old one")
            self.add_address(address)
    
    def add_email(self, email: str):
        if email and type(email) is str:
            temp_email = Email(email)
            if temp_email:
                if self.__email and self.__email.get_email():
                    raise ValueError(Fore.YELLOW + "Email already exists. Please use change email.")
                self.__email = temp_email
                return f"Email added: {email}"

    def change_email(self, email: str):
        if email and type(email) is str:
            if self.__email and self.__email.get_email() == email:
                raise ValueError(Fore.YELLOW + "The new email is the same as the old one")
        temp_email = Email(email)
        if temp_email:
            if not self.__email:
                raise ValueError(Fore.YELLOW + "Email does not exist. Please use add-email command.")
            if self.__email and self.__email.email == email:
                raise ValueError(Fore.YELLOW + "New email is the same as the existing one.")
            self.__email = temp_email
            return f"Email changed: {email}"

