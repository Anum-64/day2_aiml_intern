contacts = { "alice": "8764325108", "bob": "9628407416", "darth": "7659825621"}
print(contacts)
contacts["charlie"] = "5327895031"      # add
contacts["Alice"] = "4906532174"      # update
found = contacts.get("Bob", "Contact not found")
not_found = contacts.get("Eve", "Contact not found")
for name, phone in contacts.items():
    print("Contact:", name, " Phone:", phone)
print(found)
print(not_found)