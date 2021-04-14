"""App that keeps track of a user's contacts"""
import argparse
import sqlite3
import inspect

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
    parser.add_argument("-u", help="Update a contact's information")
    parser.add_argument("-r", help="Remove a contact (must use full name in"
                        " quotes")

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
    print(f"Contact {first_name} {last_name} created.")


def update_contact(query):
    """Update an existing contact"""
    found_cursor = CURSOR.execute(
        """SELECT first_name, last_name, company, phone_number, email, address
        FROM contacts WHERE (first_name = ? and last_name = ?)""",
        (query, query))
    return found_cursor

def remove_contact(query):
    """Remove an existing contact"""
    f_name, l_name = query.split(" ")
    CURSOR.execute("""DELETE FROM contacts WHERE
                   (first_name = ? and last_name  = ?)""", (f_name, l_name))
    CONNECTION.commit()
    print("Removed contact")

def find_contact(query):
    """Find an existing contact"""
    found_contact = CURSOR.execute(
        """SELECT first_name, last_name, company, phone_number, email, address
        FROM contacts WHERE (first_name LIKE ? or last_name LIKE ?)""",
        (query, query)).fetchall()
    return found_contact


def print_contact(found_contact):
    """Format and display contact information"""
    # 'for' loop in case there is more than one contact returned
    for person in found_contact:
        print(inspect.cleandoc(f"""
              Name    : {person[0]} {person[1]}
              Company : {person[2]}
              Phone   : {person[3]}
              Email   : {person[4]}
              Address : {person[5]}
              --------------------------------
              """))


if __name__ == "__main__":
    args = setup_argparse()

    if args.a:
        create_contact()
    elif args.f:
        contact = find_contact(args.f)
        print_contact(contact)
    elif args.r:
        remove_contact(args.r)
    elif args.u:
        contact = update_contact(args.u)
        print_contact(contact)
