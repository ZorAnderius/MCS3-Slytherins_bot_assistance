from collections import UserDict, defaultdict
from datetime import datetime
import json

from .Record import Record


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    @property
    def book(self):
        return self.data

    @book.setter
    def set_book(self, data):
        self.data = data
        
    def add_book(self, data):
        for key, record in data.items():
            name = record['name']
            phones = record['phones']
            birthday = record['birthday']
            new_record = Record(name)
            if phones and len(phones):
                new_record.add_phones(phones)
            if birthday:
                day, month, year = [int(day) for day in birthday.split('.')]
                current_date = datetime.now()
                if year < current_date.year:
                    new_record.add_birthday(year, month, day)
                    self.data[key] = new_record
                if year == current_date.year and month < current_date.month:
                    new_record.add_birthday(year, month, day)
                    self.data[key] = new_record
                if year == current_date.year and month == current_date.month and day < current_date.day:
                    new_record.add_birthday(year, month, day)
                    self.data[key] = new_record
                        
            self.data[key] = new_record
        return self

    def add_record(self, record):
        if record:
            if record.name.value in self.data:
                self.data[record.name.value].add_phone(record.phones[0].value)
            else:
                self.data[record.name.value] = record
        else:
            raise ValueError("Invalid record")

    def find(self, name):
        if not len(self.data):
            raise ValueError("Phonebook is empty")
        if name in self.data:
            return self.data[name]
        else:
            raise ValueError("Contact not found")

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def serialize(self):
        if len(self.data):
            nested_dict = dict()
            for key, record in self.data.items():
                nested_dict[key] = record.serialize()

        return {'data': nested_dict}

    def de_serialize(self, data):
        new_book = data['data']
        return new_book

    def save_to_file(self, filename=''):
        if filename and len(self.data):
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


    def __repr__(self):
        string = ''
        for record in self.data.values():
            string += str(record) + '\n'
        return string[:-1:]

    def get_birthdays_per_time(self, time):
        if not len(self.data.values()):
            raise ValueError("Your phonebook is empty")
        users_birthdays_dict = defaultdict(list)
        dict_of_users = dict()
        
        current_date = datetime.today().date()
        next_year = self.__days_per_next_year(current_date)

        if time > next_year:
            return (
                f"The date value is not within a year. Choose a value from 1 to {next_year}"
            )
        for record in self.data.values():
            name = record.name.value
            if record.birthday:
                birthday = record.birthday
            else:
                birthday = None

            if name and birthday is not None:
                birthday_this_year = birthday.replace_year(year=current_date.year)
                if birthday_this_year is None:
                    continue

                if birthday_this_year < current_date:
                    birthday_this_year = birthday_this_year.replace(year=(current_date.year + 1))

                days_from_current = (birthday_this_year - current_date).days
                birthday_day = birthday_this_year.strftime("%d.%m.%Y")

                if birthday_day in dict_of_users:
                    dict_of_users[days_from_current][birthday_day].append(name)
                else:
                    users_birthdays_dict[birthday_day].append(name)
                    if len(users_birthdays_dict) > 1:
                        key = list(users_birthdays_dict.keys())[0]
                        del users_birthdays_dict[key]
                        
                    dict_of_users[days_from_current] = dict(users_birthdays_dict)
        dict_of_users = self.__sorted_users_notes((dict_of_users))
        if not dict_of_users:
            raise ValueError("Your calendar is empty")
        return dict_of_users
    
    def __days_per_next_year(self, date):
        next_year = date.replace(year=date.year + 5).year
        is_leap_year = False
        if next_year % 4 == 0:
            is_leap_year = True
            if next_year % 100 == 0 and next_year % 400 != 0:
                is_leap_year = False

        return 366 if is_leap_year else 365

    def __sorted_users_notes(self, users_birthdays_dict):
        temp_dict = dict()
        keys = sorted(users_birthdays_dict.keys())
        for key in keys:
            temp_dict[key] = users_birthdays_dict[key]
        return temp_dict

