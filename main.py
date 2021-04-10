"""App that keeps track of a user's contacts"""
#import argparse
#import pathlib
#import sys
import sqlite3

connection = sqlite3.connect("contacts.db")
print(connection.total_changes)
cursor = connection.cursor()


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


# Temporary stuff for testing database
george = Contact('George')
george.add_phone_number('911')
try:
    cursor.execute("CREATE TABLE contacts (name TEXT, phone_number TEXT)")
except sqlite3.OperationalError as sqlite_error:
    print(sqlite_error)
cursor.execute("INSERT INTO contacts VALUES (?, ?)", (george.name,
                                                      george.phone_number))
rows = cursor.execute("SELECT name, phone_number FROM contacts").fetchall()
print(f"Rows: {rows}")
