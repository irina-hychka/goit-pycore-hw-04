def parse_input(user_input):
    '''
    Parses user input into a command and arguments.
    '''
    cmd, *args = user_input.split()
    return cmd.strip().lower(), args

def add_contact(args, contacts):
    '''
    Adds a new contact to the dictionary.
    '''
    if len(args) < 2:
        return "Error: please enter both name and phone number, be sure to separate it with a space"
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added."

def change_contact(args, contacts):
    '''
    Updates the phone number for an existing contact.
    '''
    if len(args) < 2:
        return "Error: please enter both name and new phone number, be sure to separate it with a space"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Contact {name} updated."
    return f"Error: contact {name} not found."

def show_phone(args, contacts):
    '''
    Returns the phone number for the contact.
    '''
    if not args:
        return "Error: please enter a contact name."
    name = args[0]
    return contacts.get(name, f"Error: contact {name} not found.")

def show_all(contacts):
    '''
    Outputs all saved contacts.
    '''
    if not contacts:
        return "No contacts available."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    '''
    Main function that handles user interaction in an infinite loop.
    '''
    contacts = {}
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