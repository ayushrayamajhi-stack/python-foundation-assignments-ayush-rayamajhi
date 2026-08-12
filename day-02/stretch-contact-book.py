"""
Exercise: Contact Book Menu
Student: Ayush Rayamajhi
Day: 2
"""

contacts = {}

while True:
    print("\n===== Contact Book =====")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. Display all contacts")
    print("5. Exit")

    choice = input("Enter your choice: ").strip()

    # Add contact
    if choice == "1":
        name = input("Enter name: ").strip()
        phone = input("Enter phone number: ").strip()
        email = input("Enter email address: ").strip()

        contacts[name] = {
            "phone": phone,
            "email": email
        }

        print("Contact added successfully.")

    # Search contact
    elif choice == "2":
        name = input("Enter name to search: ").strip()

        if name in contacts:
            contact = contacts[name]
            print(f"Name: {name}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
        else:
            print("Contact not found.")

    # Delete contact
    elif choice == "3":
        name = input("Enter name to delete: ").strip()

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    # Display contacts
    elif choice == "4":
        if not contacts:
            print("No contacts available.")
        else:
            print("\nContacts:")

            for name, contact in contacts.items():
                print(f"\nName: {name}")
                print(f"Phone: {contact['phone']}")
                print(f"Email: {contact['email']}")

    # Exit
    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1-5.")