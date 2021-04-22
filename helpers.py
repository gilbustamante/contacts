"""Helper functions for main.py"""
import re
import sqlite3
import inquirer
from inquirer import errors


def select_contact(cursor_object):
    """Ask user to select a contact via inquirer"""
    all_contacts = []

    # Fetch all contacts
    try:
        sql = ("SELECT first_name, last_name "
               "FROM contacts")
        contacts_object = cursor_object.execute(sql).fetchall()
    except sqlite3.OperationalError as op_err:
        print(f"Database has not been initialized! ({op_err})"
              "\nUse command 'python db.py' to initialize.")
        return None

    # If contacts db is empty, return
    if contacts_object == []:
        print("There are no contacts in the database.\n"
              "Add a contact with command 'python main.py -a'")
        return None

    # Convert name tuples to strings (for inquirer display)
    for contact in contacts_object:
        all_contacts.append(f"{contact[0]} {contact[1]}")

    # Inquirer
    questions = [
        inquirer.List("contact",
                      message="Select a contact",
                      choices=all_contacts)
    ]

    answer = inquirer.prompt(questions)
    first_and_last_name = answer["contact"].split(" ")

    # Find and return contact object
    sql = ("SELECT first_name, last_name, company, "
           "phone_number, email, address, notes "
           "FROM contacts "
           "WHERE (first_name = ? or last_name = ?)")
    found_contact = cursor_object.execute(sql, (first_and_last_name[0],
                                                first_and_last_name[1]))
    for person in found_contact:
        return person


def get_update_answers(person):
    """Iterate through object and ask user for updated info"""
    update_questions = [
        inquirer.Text("first", message="First Name", default=person[0]),
        inquirer.Text("last", message="Last Name", default=person[1]),
        inquirer.Text("company", message="Company", default=person[2]),
        inquirer.Text("phone", message="Phone", default=person[3],
                      validate=phone_validation),
        inquirer.Text("email", message="Email", default=person[4],
                      validate=email_validation),
        inquirer.Text("address", message="Address", default=person[5]),
        inquirer.Text("notes", message="Notes", default=person[6]),
    ]
    answers = inquirer.prompt(update_questions)
    return answers


def phone_validation(_, current):
    """Validate entered phone numbers"""
    # If user leaves it blank, ignore
    if current == "":
        return True
    if not re.match(r"[\d+\(\)]*[\d ]+\d", current):
        raise errors.ValidationError("", reason="Invalid phone number")
    return True


def email_validation(_, current):
    """Validate entered emails"""
    # If user leaves it blank, ignore
    if current == "":
        return True
    if not re.match(r"^[\w\d.-]+@[\w\d]+\.+[\w]+[\.\w]*", current):
        raise errors.ValidationError("", reason="Invalid email")
    return True
