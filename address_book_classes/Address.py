class Address:
    def __init__(self, address=""):
        self.set_address(address)
    @property
    def address(self):
        return self.__address
    
    
    def set_address(self,address):
        if address is None:
            raise ValueError("Address cannot be empty")
        if not any(char.isalpha() for char in address):
            raise ValueError("Address must contain at least one alphabet character")
        self.__address = address

    def get_address(self):
        return self.__address

    def serialize(self):
        return self.__address

    def __str__(self):
        return self.__address
