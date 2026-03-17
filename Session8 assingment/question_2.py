# Create contact book using dictionary
contacts = {
    "Ravi": "9876543210",
    "Anita": "9123456780",
    "Rahul": "9988776655"
}

# Print all contacts
print("All Contacts:")
for name, number in contacts.items():
    print(name, ":", number)

# Ask user for a name
search_name = input("\nEnter name to search: ")

# Dictionary lookup using 'in' keyword
if search_name in contacts:
    print("Phone number:", contacts[search_name])
else:
    print("Contact not Found")
