from .Field import Field
import re


class Phone(Field):
    def __init__(self, phone: str):
        if self.is_valid(phone):
            self.__phone = phone
        else:
            self.__phone = None
            raise ValueError(f"{phone} is invalid phone number. Length must more than 10 but less than 15 values")
        super().__init__(self.phone)

    def ph_length(self, phone: str) -> int:
        regex = r"([^\d]?)"
        replace = ""
        length = len(re.sub(regex,replace,phone, 0))
        return length
        
    def serialize(self):
        return self.phone

    def is_valid(self, phone: str) -> bool:
        if phone.startswith("+"):
            phone_len = self.ph_length(phone)
            if phone_len > 15 or phone_len < 10:
                return False
        else:
            if self.ph_length(phone) > 10:
                return False
            
        regex = r"\+?[\d\s\-\(\)]+"
        match = re.search(regex, phone)
        return match is not None
    
    @property
    def phone(self) -> str:
        return self.__phone

    @phone.setter
    def set_phone(self, phone: str):
        if self.is_valid(phone):
            self.__phone = phone
        else:
            self.__phone = None
            raise ValueError(f"{phone} is invalid phone number. Length must be 10 numbers")

    def __eq__(self, other) -> bool:
        return self.phone == other

    def __repr__(self) -> str:
        if self.__phone:
            return f"{self.__phone}"

    def __str__(self) -> str:
        if self.__phone:
            return f"{self.__phone}"