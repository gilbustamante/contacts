import inquirer


def select_contact(cursor_object):
    """Ask user to select a contact via inquirer"""
    all_contacts = []
    # Fetch all contacts
    contacts_object = cursor_object.execute("""SELECT first_name, last_name FROM
                                  contacts""").fetchall()
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
    found_contact = cursor_object.execute(
        """SELECT first_name, last_name, company, phone_number, email, address
        FROM contacts WHERE (first_name = ? or last_name = ?)""",
        (first_and_last_name[0], first_and_last_name[1]))
    for person in found_contact:
        return person
    #return found_contact


def get_update_answers(person):
    """Iterate through object and ask user for updated info"""
    update_questions = [
        inquirer.Text("first", message="First Name", default=person[0]),
        inquirer.Text("last", message="Last Name", default=person[1]),
        inquirer.Text("company", message="Company", default=person[2]),
        inquirer.Text("phone", message="Phone", default=person[3]),
        inquirer.Text("email", message="Email", default=person[4]),
        inquirer.Text("address", message="Address", default=person[5]),
    ]
    answers = inquirer.prompt(update_questions)
    return answers
