"""Module for defining the contact class"""


class Contact:
    """Represents a contact added by the user"""

    def __init__(self, contact):
        self.first_name = contact[0]
        self.last_name = contact[1]
        self.company = contact[2]
        self.phone_number = contact[3]
        self.email = contact[4]
        self.address = contact[5]

    def update_name(self, new_name):
        """Updates contact's name with new_name"""
        self.name = new_name
        print(f"Updated name: {self.name}")

    def add_phone_number(self, number):
        """Adds a phone number to the contact"""
        self.phone_number = number

    def print_contact(self):
        """Displays the contact's information"""
        info = f"""
        Contact Information
        Name: {self.name}
        Phone Number: {self.phone_number}
        """
        print(info)
