from datetime import datetime
from colorama import Fore

from .Name import Name
from .Phone import Phone
from .Birthday import Birthday


class Record:
    def __init__(self, name: str, phone: str = "", *birthday: (int, int, int)):
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

    def serialize(self):
        return {
            "name": self.name.serialize(),
            "phones": [phone.serialize() for phone in self.phones],
            "birthday": self.birthday.serialize() if self.birthday else None,
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
    def birthday(self) -> datetime:
        return self.__birthday

    def set_bithday(self, birthday: datetime):
        if birthday:
            self.__birthday = birthday
        else:
            self.__birthday = None

    def __str__(self) -> str:
        if self.phones:
            str1 = Fore.YELLOW + "Contact name: "
            str2 = Fore.LIGHTMAGENTA_EX + str(self.name)
            str3 = Fore.YELLOW + "phones: "
            str4 = Fore.WHITE + "; ".join(phone.value for phone in self.phones)
            return "{0}{1: <15} {2}\n".format(str1, str2, (str3 + str4))
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
