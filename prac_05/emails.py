"""
Emails
Estimate: 20 minutes
Actual:   18 minutes
"""

def main():
    contacts = {}
    load_contacts(contacts)
    print_contacts(contacts)

def load_contacts(contacts):
    while True:
        email = input("Email: ")

        if email == "":
            break

        try:
            name = email[:email.index("@")]
        except ValueError:
            print("Invalid email address")
            return None

        if name.count(".") != 0:
            name = " ".join(name.split("."))

        name = name.title()

        name_confirmation = input(f"Is your name {name}? (Y/n) ").upper()
        if name_confirmation != "" and name_confirmation != "Y":
            name = input("Name: ")

        contacts[email] = name

def print_contacts(contacts):
    for email, name in contacts.items():
        print(f"{name} ({email})")

main()