"""Module for defining the contact class"""


class Contact:
    """Represents a contact added by the user"""

    def __init__(self, contact):
        self.first_name = contact["first_name"]
        self.last_name = contact["last_name"]
        self.company = contact["company"]
        self.phone_number = contact["phone_number"]
        self.email = contact["email"]
        self.address = contact["address"]

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
