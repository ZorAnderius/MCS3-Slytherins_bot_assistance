from .Field import Field


class Phone(Field):
    def __init__(self, phone: str):
        if self.is_valid(phone):
            self.__phone = phone
        else:
            self.__phone = None
            raise ValueError(f"{phone} is invalid phone number. Length must be 10 numbers")
        super().__init__(self.phone)

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

    def serialize(self):
        return self.phone

    def is_valid(self, phone: str) -> bool:
        return True if len(phone) == 10 and phone.isdigit() else False

    def __eq__(self, other) -> bool:
        return self.phone == other

    def __repr__(self) -> str:
        if self.__phone:
            return f"{self.__phone}"

    def __str__(self) -> str:
        if self.__phone:
            return f"{self.__phone}"