class Body:
    def __init__(self, body):
        if self.__is_valid(body):
            self.__body = body
        else:
            raise ValueError("Invalid data")

    @property
    def body(self):
        return self.__body

    @body.setter
    def set_body(self, body):
        if self.__is_valid(body):
            self.__body = body
        else:
            raise ValueError("Invalid data")

    def __str__(self):
        return f"{self.__body}"

    def __is_valid(self, body):
        return True if type(body) is str else False
