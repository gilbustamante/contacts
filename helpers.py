import inquirer

def get_update_answers(cursor_object):
    """Iterate through object and ask user for updated info"""
    for person in cursor_object:
        update_questions = [
            inquirer.Text("first", message="First Name", default=person[0]),
            inquirer.Text("last", message="Last Name", default=person[1]),
            inquirer.Text("company", message="Company", default=person[2]),
            inquirer.Text("phone", message="Phone", default=person[3]),
            inquirer.Text("email", message="Email", default=person[4]),
            inquirer.Text("address", message="Address", default=person[5]),
        ]
        update_answers = inquirer.prompt(update_questions)
    return update_answers
