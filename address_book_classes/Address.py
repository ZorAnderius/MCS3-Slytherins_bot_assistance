class Address:
    def __init__(self, text):
        if not text:
            raise ValueError("Please put text in the text format.")
        if not any(char.isalpha() for char in text):
            raise ValueError("Text must contain at least one alphabet character.")
        self.text = text

    def __str__(self):
        return self.text