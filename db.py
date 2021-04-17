"""Create and modify database"""

import sqlite3

CONNECTION = sqlite3.connect("contacts.db")
CURSOR = CONNECTION.cursor()
CURSOR.execute("""CREATE TABLE contacts (
    first_name TEXT,
    last_name TEXT,
    company TEXT,
    phone_number TEXT,
    email TEXT,
    address TEXT,
    notes TEXT
)""")

print("Database initialized")
