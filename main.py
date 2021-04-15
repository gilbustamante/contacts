"""App that keeps track of a user's contacts"""
import argparse
import sqlite3
import inspect
import inquirer

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
    parser.add_argument("-u", action="store_true", help="Update a contact's"
                        " information", default=False)
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

# TODO: REFACTOR THIS FUNCTION!


def update_contact():
    """Update an existing contact"""
    all_contacts = []
    # Fetch all contacts
    contacts_from_db = CURSOR.execute("""SELECT first_name, last_name FROM
                                  contacts""").fetchall()
    # Looping to convert tuples to strings (for inquirer display)
    for name in contacts_from_db:
        all_contacts.append(f"{name[0]} {name[1]}")
    # Inquirer setup
    questions = [
        inquirer.List("contact",
                      message="Who do you want to update?",
                      choices=all_contacts)
    ]
    answer = inquirer.prompt(questions)
    name = answer["contact"].split(" ")
    # Find contact
    found_contact = CURSOR.execute(
        """SELECT first_name, last_name, company, phone_number, email, address
        FROM contacts WHERE (first_name = ? and last_name = ?)""",
        (name[0], name[1]))
    print(found_contact)
    for person in found_contact:
        update_questions = [
            inquirer.Text("first", message="First Name", default=person[0]),
            inquirer.Text("last", message="Last Name", default=person[1]),
            inquirer.Text("company", message="Company", default=person[2]),
            inquirer.Text("phone", message="Phone", default=person[3]),
            inquirer.Text("email", message="Email", default=person[4]),
            inquirer.Text("address", message="Address", default=person[5]),
        ]
        update_answers = inquirer.prompt(update_questions)
    # Update contact
    CURSOR.execute(
        """UPDATE contacts SET first_name = ?, last_name = ?,
        company = ?, phone_number = ?, email = ?, address = ? WHERE
        (first_name = ? and last_name = ?)""", (update_answers["first"],
                                                update_answers["last"],
                                                update_answers["company"],
                                                update_answers["phone"],
                                                update_answers["email"],
                                                update_answers["address"],
                                                name[0], name[1]))
    CONNECTION.commit()
    print(f"Contact {name[0] + name[1]} updated")


def remove_contact(query):
    """Remove an existing contact"""
    f_name, l_name = " ".split(query)
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
        update_contact()
