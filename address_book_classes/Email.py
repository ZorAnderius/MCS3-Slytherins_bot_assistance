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

    @staticmethod
    def search_contacts(contacts, query):
        matching_emails = [contact.email for contact in contacts if query in contact.email]
        return matching_emails

    @staticmethod
    def add_email(contacts, name, email):
        for contact in contacts:
            if contact.name == name:
                if contact.email:
                    raise ValueError("Contact already has an email address.")
                if not Email.validate_email(email):
                    raise ValueError("Invalid email address.")
                contact.email = email
                return f"Added email {email} to contact {name}."
            
    @staticmethod
    def suggest_variants(contacts, query):
        suggested_emails = [contact.email for contact in contacts if contact.email.startswith(query)]
        return suggested_emails

    @staticmethod
    def edit_email(contacts, old_email, new_email):
        for contact in contacts:
            if contact.email == old_email:
                contact.email = new_email

    @staticmethod
    def delete_email(contacts, email):
        contacts[:] = [contact for contact in contacts if contact.email != email]

class Contact:
    def __init__(self, email):
        self.email = email

        
if __name__ == "__main__":
    contacts = [Contact("example1@example.com"), Contact("example2@example.com")]

    search_results = Email.search_contacts(contacts, 'exa')
    print("Search Results:", search_results)

    suggested_emails = Email.suggest_variants(contacts, 'exa')
    print("Suggested Emails:", suggested_emails)

    Email.edit_email(contacts, 'example1@example.com', 'new@example.com')
    print("Updated Contacts:")
    for contact in contacts:
        print(contact.email)

    Email.delete_email(contacts, 'new@example.com')
    print("Contacts After Deletion:")
    for contact in contacts:
        print(contact.email)
