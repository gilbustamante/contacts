"""App that keeps track of a user's contacts"""
import argparse
import sqlite3

# Connect to database
DATABASE = "test.db"
CONNECTION = sqlite3.connect(DATABASE)
CURSOR = CONNECTION.cursor()


def setup_argparse():
    """Setup and parse arguments"""
    parser = argparse.ArgumentParser(
        description="Create, edit, and remove contacts using the command line.",
    )
    parser.add_argument("-a", action="store_true", help="Add a new contact",
                        default=False)
    parser.add_argument("-f", help="Find and display info about a contact")
    parser.add_argument("-r", help="Remove a contact")

    return parser.parse_args()


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


def find_contact(query):
    """Remove an existing contact"""
    found_contact = CURSOR.execute(
        """SELECT first_name, last_name, company, phone_number, email, address
        FROM contacts WHERE (first_name LIKE ? or last_name LIKE ?)""",
        (query, query)).fetchall()

    print(found_contact)


if __name__ == "__main__":
    args = setup_argparse()

    if args.a:
        create_contact()
    elif args.f:
        print(args.f)
        find_contact(args.f)
