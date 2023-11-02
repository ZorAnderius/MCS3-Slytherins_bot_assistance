class Title:
    def __init__(self, title=""):
        if self.__is_valid(title):
            self.__title = title
        elif title == "":
            self.__title = None
        else:
            self.__title = None
            raise ValueError(
                "Title must be a more than 2 characters long or it must be a string"
            )

    @property
    def title(self):
        return self.__title

    @title.setter
    def set_title(self, title=""):
        self.__title = title

    def __str__(self):
        if self.__title == None:
            return "Title is empty"
        return f"{self.__title}"

    def __is_valid(self, title):
        return True if type(title) is str and len(title) > 2 else False
