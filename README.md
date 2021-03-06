# Contacts
Simple CLI contacts app. View a contact's information quickly!

## Requirements
* [inquirer](https://pypi.org/project/inquirer/)
```
pip install inquirer
```

## Usage
First initialize a database:
```
python db.py
```
Then use the following syntax to add/view/remove contacts:
```
python main.py [option]
```
| Option | Description                        |
|--------|------------------------------------|
| `-a`   | Add a contact.                     |
| `-u`   | Update a contact's info.           |
| `-f`   | Find and display a contact's info. |
| `-r`   | Remove a contact.                  |
| `-h`   | Display help.                      |

## To Do
* ~~Validate phone number and email entry~~
* Additional fields if needed
