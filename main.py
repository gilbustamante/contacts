"""App that keeps track of a user's contacts"""
import argparse
import sqlite3

DATABASE = "test.db"
CONNECTION = sqlite3.connect(DATABASE)
CURSOR = CONNECTION.cursor()


def setup_argparse():
    """Setup and parse arguments"""
    parser = argparse.ArgumentParser(
        prog="CLI Contact Book",
        description="Create, edit, and remove contacts using the command line.",
    )

    subparsers = parser.add_subparsers()

    # Add contact
    parser_add_contact = subparsers.add_parser("add", help="Add new contact")
    parser_add_contact.set_defaults(func=create_contact)

    # Update contact
    parser_update_contact = subparsers.add_parser("update", help="Update contact")
    parser_update_contact.set_defaults(func=update_contact)

    # Remove contact
    parser_remove_contact = subparsers.add_parser("remove", help="Remove contact")
    parser_remove_contact.set_defaults(func=remove_contact)

    # List contacts
    parser_list_contacts = subparsers.add_parser("list", help="List contacts")
    parser_list_contacts.set_defaults(func=list_all_contacts)

    options = parser.parse_args()
    options.func()


def create_contact():
    """Guide user through creating a contact"""
    print("Create Contact\nTip: press RETURN to skip field.")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    company = input("Company: ")
    phone_number = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")
    CURSOR.execute("INSERT INTO contacts VALUES (?, ?, ?, ?, ?, ?)",
                   (first_name, last_name, company, phone_number, email, address))
    CONNECTION.commit()
    print("Contact created.")


def update_contact():
    """Update an existing contact"""
    print('update_contact running')


def remove_contact():
    """Remove an existing contact"""
    print('remove_contact running')

def list_all_contacts():
    """Remove an existing contact"""
    rows = CURSOR.execute("SELECT first_name, last_name, company, phone_number,"
                          "email, address FROM contacts").fetchall()
    for contact in rows:
        print(f"\nFirst Name: {contact[0]}")
        print(f"Last Name: {contact[1]}")
        print(f"Company: {contact[2]}")
        print(f"Phone Number: {contact[3]}")
        print(f"Email: {contact[4]}")
        print(f"Address: {contact[5]}")


if __name__ == "__main__":
    try:
        setup_argparse()
    except AttributeError:
        print("You must provide an argument ('add', 'update', 'remove', 'list')")
