# Personal Basic Assistant - Voldebot

## Overview

The Personal Basic Assistant is a program designed to manage information records such as email addresses, physical addresses, phone numbers, names, and more. Its primary goal is to provide users with a user-friendly console-based interface for storing, searching, and interacting with their contact information through a set of intuitive commands.

- **Description of classes:** The classes serve as a base for various record fields.

### Name

- **Description:** This class is responsible for storing contact names, such as "Harry Potter" or "Ron Weasley."
- **Mandatory Field:** Yes

### Record

- **Description:** This class stores contact information, including names and a list of phone numbers.
- **Attributes:**
  - **Name:** Stores the contact's name.
  - **Phone Numbers:** Stores a list of phone numbers.
- **Methods:**
  - **Add Phone:** Adds a phone number to the record.
  - **Remove Phone:** Removes a phone number from the record.
  - **Edit Phone:** Edits a phone number within the record.
  - **Find Phone:** Searches for phone numbers in the record.
  - **Delete Record:** Deletes the entire record based on the name.
  - **Remove Record:** Removes a piece of information from the record book. 

### AddressBook

- **Description:** This class manages contact records.
- **Methods:**
  - **Add Record:** Adds a record to the address book.
  - **Find:** Finds a record by name.
  - **Delete:** Deletes a record by name.

### Email

- **Description:** This class is responsible for storing and validating email addresses.
- **Methods:**
  - **Validate Email:** Validates the format of an email address using a regular expression.

### Email Functions

- **Method: Search Contacts**
  - **Description:** Allows users to search for email addresses within a list of contacts based on a specific query.
  - **Returns:** A list of email addresses that match the query.

- **Method: Suggest Variants**
  - **Description:** Provides email address variants that start with a specified query.

- **Method: Edit Email**
  - **Description:** Allows users to edit an existing email address in the contact list.

- **Method: Delete Email**
  - **Description:** Enables the deletion of email addresses from the contact list based on a specified value.

### Phone

- **Description:** This class validates phone numbers based on the input method:
  - **With country code:** It must start with a '+,' and the length should be between 10 and 15 digits.
  - **Without a country code:** It must consist of 10 digits.
  - Hyphens ('-') may be used as separators.

## Usage

This Personal Basic Assistant provides an easy-to-use console-based interface for managing contact information efficiently. Users can add, edit, search for contacts, validate contact details, and manage text notes using simple commands.

## Getting Started

- Clone this repository to your local machine.
- Install pycharm, vs-code or any other program that supports python files to run the assistant on your machine. 

## Contributing

You are welcome to contribute to this project by creating issues, suggesting improvements, or submitting pull requests. We are open to new improvements and suggestions. Thanks!

## Acknowledgments

Special thanks to the wonderful team of slytherin.
Translation into Ukraninian
***************************************************************************************************************
***************************************************************************************************************
# Особистий Базовий Асистент

## Огляд

Особистий Базовий Асистент - це програма, розроблена для управління інформаційними записами, такими як email-адреси, фізичні адреси, номери телефонів, імена та більше. Його основна мета - забезпечити користувачам зручний консольний інтерфейс для зберігання, пошуку та взаємодії з інформацією про контакти за допомогою набору інтуїтивних команд.

- **Опис:** Цей клас служить основою для різних полів записів.

### Ім'я

- **Опис:** Цей клас відповідає за зберігання імен контактів, таких як "Гаррі Поттер" або "Рон Візлі".

- **Опис:** Цей клас зберігає інформацію про контакти, включаючи імена та список номерів телефонів.
- **Атрибути:**
  - **Ім'я:** Зберігає ім'я контакту.
  - **Номери телефонів:** Зберігає список номерів телефонів.
- **Методи:**
  - **Додати Телефон:** Додає номер телефону до запису.
  - **Видалити Телефон:** Видаляє номер телефону з запису.
  - **Редагувати Телефон:** Редагує номер телефону в записі.
  - **Знайти Телефон:** Шукає номери телефонів в записі.
  - **Видалити Запис:** Видаляє весь запис за іменем.

### Адресна Книга

- **Опис:** Цей клас відповідає за зберігання та управління контактними записами.
- **Методи:**
  - **Додати Запис:** Додає запис до адресної книги.
  - **Знайти:** Знаходить запис за іменем.
  - **Видалити:** Видаляє запис за іменем.

### Email

- **Опис:** Цей клас відповідає за зберігання та перевірку email-адрес.
- **Методи:**
  - **Перевірити Email:** Перевіряє формат email-адреси за допомогою регулярного виразу.

### Функції Email

- **Метод: Пошук Контактів**
  - **Опис:** Дозволяє користувачам шукати email-адреси в списку контактів на основі конкретного запиту.
  - **Повертає:** Список email-адрес, які відповідають запиту.

- **Метод: Запропонувати Варіанти**
  - **Опис:** Надає варіанти email-адрес, які починаються з вказаного запиту.

- **Метод: Редагувати Email**
  - **Опис:** Дозволяє користувачам
Наша команда відкрита для зауважен стосовно покращень.
Слова подяки команді слізеренду, яка працювала над ботом.
