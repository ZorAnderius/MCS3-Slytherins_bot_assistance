import copy


class Body:
    def __init__(self, body):
        if self.__is_valid(body):
            self.__body = body
        else:
            self.__body = None
            raise ValueError("Invalid data")

    @property
    def body(self):
        return self.__body

    @body.setter
    def set_body(self, body):
        if self.__is_valid(body):
            self.__body = body
        else:
            self.__body = None
            raise ValueError("Invalid data")
        
    def serialize(self):
        return self.body

    def __copy__(self):
        body_copy = Body(
            copy.copy(self.body),
        )
        return body_copy

    def __is_valid(self, body):
        return True if type(body) is str else False
    
    def __str__(self):
        return f"{self.__body}"
