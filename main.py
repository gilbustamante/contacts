"""App that keeps track of a user's contacts"""
import argparse
import sqlite3
from contact import Contact

DATABASE = "test.db"
CONNECTION = sqlite3.connect(DATABASE)
CURSOR = CONNECTION.cursor()


def setup_argparse():
    """Setup and parse arguments"""
    parser = argparse.ArgumentParser(
        prog="CLI Contact Book",
        description="Create, edit, and remove contacts using the command line",
        usage="main.py [options] values"
    )

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
                   (first_name, last_name, company, phone_number, email,
                    address))
    CONNECTION.commit()
    print("Contact created.")

# Temporary stuff for testing database
#rows = CURSOR.execute("SELECT name, phone_number FROM contacts").fetchall()
#for contact in rows:
#    print(contact)

create_contact()
