from datetime import datetime
from colorama import Fore, Back
import sys
import copy

sys.path.append(".")


from .Title import Title
from .Body import Body
from .Tag import Tag
from address_book_classes.Name import Name


class Note:
    def __init__(self, author, title="", body="", *tags):
        self.__author = Name(author)
            
        if title and type(title) is str:
            self.__title = Title(title)
        else: 
            self.__title = None

        if body and type(body) is str:
            self.__body = Body(body)
        else: 
            self.__body = None
            
        if tags and type(tags[0]) == str:
            self.__tags = [Tag(tag) for tag in tags]
        elif tags and type(tags[0]) == Tag:
            self.__tags = tags
        else:
            self.__tags = []
        
        self.__created_at = datetime.today().strftime("%a %d %b %Y, %I:%M%p")

    @property
    def author(self):
        return self.__author

    @property
    def title(self):
        return self.__title

    @title.setter
    def set_title(self, title):
        self.__title = Title(title)

    @property
    def body(self):
        return self.__body

    @body.setter
    def set_body(self, body):
        if body and type(body) is str:
            self.__body = Body(body)
        else:
            self.__body = None

    @property
    def created_at(self):
        return self.__created_at

    @property
    def tags(self):
        return self.__tags

    @tags.setter
    def set_tags(self, tags):
        if tags:
            self.__tags = tags
        else:
            self.__tags = []

    @property
    def id(self):
        return self.__id
    
    def serialize(self):
        return {
            "author": self.author.serialize() if self.author else None,
            "title": self.title.serialize() if self.title else None,
            "tags": [tag.serialize() for tag in self.tags] if self.tags else None,
            "body": self.body.serialize() if self.body else None,
            "created_at": self.created_at if self.created_at else None,
        }

    def add_title(self, title: str):
        new_title = Title(title)
        if new_title and type(new_title) == Title:
            self.__title = new_title

    def add_body(self, body: str):
        if body and type(body) is str:
            self.__body = Body(body)
        else:
            self.__body = None

    def add_tag(self, tag: str):
        if list(filter(lambda x: x.tag == tag, self.__tags)):
            raise ValueError(Fore.YELLOW + f"{tag} is already exist")
        try:
            new_tag = Tag(tag)
        except ValueError as e:
            print(Fore.RED + str(e))
            new_tag = None
        if new_tag and new_tag.tag in self.__tags:
            raise ValueError(Fore.YELLOW + f"Duplicate tag {new_tag}")
        elif new_tag:
            self.__tags.append(new_tag)
            
    def add_tags(self, tags):
        self.__tags = [Tag(tag) for tag in tags]

    def input_title(self):
        title_text = self.__input_note(Fore.BLUE + "Enter title")
        if title_text:
            self.add_title(title_text.strip().lower())

    def input_body(self):
        body_text = self.__input_note(Fore.BLUE + "Enter body")
        if body_text:
            self.add_body(body_text.strip())

    def input_tag(self):
        while True:
            tag_text = self.__input_note(Fore.BLUE + "Enter tag (n-close)")
            if tag_text == "n":
                break
            if list(filter(lambda x: x.tag == tag_text, self.__tags)):
                print(Fore.YELLOW + f"{tag_text} is already exist")
                continue
            self.add_tag(tag_text)

    def edit_title(self, title: str):
        self.add_title(title)

    def edit_body(self, body):
        self.add_body(body)

    def edit_tag(self, old_tag: str, new_tag: str):
        if list(filter(lambda x: x.tag == new_tag, self.__tags)):
            raise ValueError(Fore.YELLOW + f"{new_tag} is already exist")
        new_tag = Tag(new_tag)
        if new_tag.tag:
            if self.find_tag(old_tag):
                index = self.remove_tag(old_tag)
                if index >= 0:
                    self.tags.insert(index, new_tag)
            else:
                raise ValueError(
                    f"Tag {old_tag} is not in the {self.title.upper()} note"
                )
                
    def add_created_at(self, date: str):
        if date and type(date) == str:
            self.__created_at = date

    def find_tag(self, tag: str) -> str or None:
        if list(filter(lambda p: p.tag == tag, self.tags)):
            return tag

    def remove_body(self):
        self.__body = None

    def remove_tag(self, tag: str) -> int or None:
        if self.find_tag(tag):
            index = list(map(str, self.tags)).index(tag)
            del self.tags[index]
            return index

    def __copy__(self):
        note_copy = Note(
            copy.copy(self.author),
            copy.copy(self.title),
            copy.copy(self.body),
            [copy.copy(tag) for tag in self.tags],
        )
        return note_copy

    def __deepcopy__(self, memo):
        copy_obj = Note(
            copy.deepcopy(self.author),
            copy.deepcopy(self.title),
            copy.deepcopy(self.body),
            copy.deepcopy(self.tags),
        )
        memo[id(copy_obj)] = copy_obj
        return copy_obj

    def __str__(self):
        tags_str = None
        title_str = Fore.GREEN + "\nTitle:"
        body_str = Fore.GREEN + "Note:"
        tag_str = Fore.GREEN + "Tags:"
        created_str = Fore.GREEN + "Created at:"

        title_body = Fore.WHITE + "Add title\n"
        note_body = Fore.WHITE + "Add note\n"
        tag_body = ""
        created_body = Fore.LIGHTBLACK_EX + f"{self.__created_at}"

        if self.tags and type(self.tags) is list:
            tags_str = ", ".join(tag.tag for tag in self.__tags)
        if self.__title is None and tags_str is None and self.__body is None:
            pass
        elif tags_str is None and not self.__body:
            title_body = Fore.WHITE + f"{self.__title}\n".capitalize()
        elif self.__title is None and not self.__body:
            tag_body = Fore.WHITE + f"{tags_str}\n"
        elif self.__title is None and tags_str is None:
            note_body = Fore.WHITE + f"{self.__body}\n".capitalize()
        elif self.__title is None:
            tag_body = Fore.WHITE + f"{tags_str}\n"
            note_body = Fore.WHITE + f"{self.__body}\n".capitalize()
        elif not self.__body:
            title_body = Fore.WHITE + f"{self.__title}\n".capitalize()
            tag_body = Fore.WHITE + f"{tags_str}\n"
        else:
            title_body = Fore.WHITE + f"{self.__title}\n".capitalize()
            note_body = Fore.WHITE + f"{self.__body}\n".capitalize()
            tag_body = Fore.WHITE + f"{tags_str}\n"
        if tags_str is None:
            return "{:<18}{:<5}{:<17}{:<2}{:<17}{:<2}\n".format(
                title_str,
                title_body,
                body_str,
                note_body,
                created_str,
                created_body,
            )
        return "{:<18}{:<5}{:<17}{:<2}{:<17}{:<2}{:<17}{:<2}\n".format(
            title_str,
            title_body,
            tag_str,
            tag_body,
            body_str,
            note_body,
            created_str,
            created_body,
        )

    def __input_note(self, txt_message):
        input_txt = input(f"{txt_message} : ")
        return input_txt
