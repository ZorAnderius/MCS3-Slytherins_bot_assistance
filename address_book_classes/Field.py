import copy


class Field:
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def set_value(self, value):
        self.__value = value

    def __copy__(self):
        value_copy = copy.copy(self.__value)
        return value_copy

    def __repr__(self):
        return f"value: {self.__value}"
