"""App that keeps track of a user's contacts"""
import argparse
import sqlite3
import sys
import inspect
import inquirer
from helpers import get_update_answers, select_contact, phone_validation

# Connect to database
DATABASE = "contacts.db"
CONNECTION = sqlite3.connect(DATABASE)
CURSOR = CONNECTION.cursor()


def setup_argparse():
    """Setup and parse arguments"""
    parser = argparse.ArgumentParser(
        description="Create, edit, and remove contacts using the command line.",
    )
    parser.add_argument("-a", "-add",
                        help="add a new contact",
                        action="store_true",
                        default=False)
    parser.add_argument("-f", "-find",
                        help="find and display info about a contact",
                        action="store_true",
                        default=False)
    parser.add_argument("-u", "-update",
                        help="update a contact's information",
                        action="store_true",
                        default=False)
    parser.add_argument("-r", "-remove",
                        help="remove a contact",
                        action="store_true",
                        default=False)

    # If no args provided, print help
    if len(sys.argv) == 1:
        parser.print_help()

    return parser.parse_args()


def create_contact():
    """Guide user through creating a contact"""
    print("Create Contact\nTip: press RETURN to skip field.")
    questions = [
        inquirer.Text("first", message="First Name"),
        inquirer.Text("last", message="Last Name"),
        inquirer.Text("company", message="Company"),
        inquirer.Text("phone", message="Phone", validate=phone_validation),
        inquirer.Text("email", message="Email"),
        inquirer.Text("address", message="Address"),
        inquirer.Text("notes", message="Notes"),
    ]
    # Get user input
    answers = inquirer.prompt(questions)

    # If contact has no name, prompt user to enter again
    while not answers["first"] and not answers["last"]:
        print("Contact's name cannot be empty")
        answers = inquirer.prompt(questions)

    # Create contact
    try:
        CURSOR.execute("INSERT INTO contacts VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (answers["first"], answers["last"], answers["company"],
                        answers["phone"], answers["email"],
                        answers["address"], answers["notes"]))
    except sqlite3.OperationalError as op_err:
        print(f"Error: {op_err}\nUse the command 'python db.py' to create a "
              "database")
        return
    CONNECTION.commit()
    print(f"Contact {answers['first']} {answers['last']} created.")


def update_contact():
    """Update an existing contact"""
    # Select contact, format name for sqlite query
    found_contact = select_contact(CURSOR)
    f_name, l_name = found_contact[0], found_contact[1]
    update_answers = get_update_answers(found_contact)

    # Update contact
    CURSOR.execute(
        """UPDATE contacts SET first_name = ?, last_name = ?,
        company = ?, phone_number = ?, email = ?, address = ?, notes = ?
        WHERE (first_name = ? and last_name = ?)""", (update_answers["first"],
                                                      update_answers["last"],
                                                      update_answers["company"],
                                                      update_answers["phone"],
                                                      update_answers["email"],
                                                      update_answers["address"],
                                                      update_answers["notes"],
                                                      f_name, l_name))

    CONNECTION.commit()
    print(f"Contact {update_answers['first']} {update_answers['last']} "
          "updated")


def remove_contact():
    """Remove an existing contact"""
    contact_to_remove = select_contact(CURSOR)
    f_name, l_name = contact_to_remove[0], contact_to_remove[1]
    CURSOR.execute("""DELETE FROM contacts WHERE
                   (first_name = ? and last_name  = ?)""", (f_name, l_name))
    CONNECTION.commit()
    print("Removed contact")


def print_contact(person):
    """Format and display contact information"""
    # cleandoc to remove unnecessary spaces from string
    try:
        print(inspect.cleandoc(f"""
              Name    : {person[0]} {person[1]}
              Company : {person[2]}
              Phone   : {person[3]}
              Email   : {person[4]}
              Address : {person[5]}
              Notes   : {person[6]}
              """))
    except TypeError as print_err:
        print(f"Cannot display contact: {print_err}")


if __name__ == "__main__":
    args = setup_argparse()

    if args.a:
        create_contact()
    elif args.f:
        contact = select_contact(CURSOR)
        print_contact(contact)
    elif args.r:
        remove_contact()
    elif args.u:
        update_contact()
