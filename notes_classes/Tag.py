import copy


class Tag:
    def __init__(self, tag):
        if self.__is_valid(tag):
            self.__tag = tag
        else:
            self.__tag = None
            raise ValueError("Invalid tag. Please use letters only")

    @property
    def tag(self):
        return self.__tag

    @tag.setter
    def set_tag(self, tag):
        if self.__is_valid(tag):
            self.__tag = tag
        else:
            self.__tag = None
            raise ValueError("Invalid tag. Please use letters only")

    def __copy__(self):
        print(type(self.tag))
        tag_copy = Tag(copy.copy(self.tag))
        return tag_copy

    def __str__(self):
        return f"{self.__tag}"

    def __is_valid(self, tag):
        if type(tag) is Tag:
            print(tag)
            print(type(tag))
            return (
                True
                if tag.tag
                and type(tag.tag) is str
                and len(tag.tag) > 2
                and tag.tag.isalpha()
                else False
            )
        return (
            True
            if tag and type(tag) is str and len(tag) > 2 and tag.isalpha()
            else False
        )
