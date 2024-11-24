def input_error(func):
    """
    Декоратор для обробки помилок введення користувача.
    Обробляє KeyError, ValueError, IndexError.
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Error: Provide valid arguments for the command (e.g., name and phone)."
        except KeyError:
            return "Error: Contact not found."
        except IndexError:
            return "Error: Provide all required arguments for the command."
    return inner


@input_error
def add_contact(args, contacts):
    """
    Додає новий контакт до записника.
    """
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    """
    Змінює номер телефону для існуючого контакту.
    """
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    raise KeyError


@input_error
def show_phone(args, contacts):
    """
    Виводить номер телефону для заданого імені.
    """
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    raise KeyError


@input_error
def show_all(contacts):
    """
    Виводить всі контакти зі словника.
    """
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


def parse_input(user_input):
    """
    Парсер для введеного користувачем рядка.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def main():
    """
    Основний цикл програми.
    """
    contacts = {}  # Словник для збереження контактів
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()

