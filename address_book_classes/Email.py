import re

class Email:
    def __init__(self, email):
        if self.validate_email(email):
            self.email = email
        else:
            raise ValueError("Invalid email address")

    def validate_email(self, email):
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(email_pattern, email) is not None

try:
    my_email = Email("example@example.com")
    print(f"Email address: {my_email.email}")
except ValueError as e:
    print(e)
