"""App that keeps track of a user's contacts"""
import argparse
import pathlib
import sys

# TODO: Add sqlite3 functionality


class Contact:
    """Represents a contact added by the user"""

    def __init__(self, name):
        self.name = name
        self.phone_number = ""
        self.business = ""
        self.address = ""


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

george = Contact('George')
george.print_contact()
george.update_name('Jorge')
george.add_phone_number('3106664208')
george.print_contact()
