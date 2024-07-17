class ContactBook:          #creating the class 
    
    def __init__(self):
        self.contacts = {}

    # adding the contact details
    def addContact(self, name, phone, email):
        self.contacts[phone] = {'name': name, 'email': email}

    # viewing the contact details
    def viewContacts(self):
        for phone, details in self.contacts.items():
            print(f"Name: {details['name']}, Phone no.: {phone}, Email: {details['email']}")

    # searching the contact details
    def searchContact(self, search_item):
        for phone, details in self.contacts.items():
            if search_item.upper() in details['name'].upper() or search_item == phone:
                print(f"Name: {details['name']}, Phone: {phone}, Email: {details['email']}")
                return
        print("No results found")

    # updating the contact details            
    def updateContact(self, phone, name=None, email=None):
        if phone in self.contacts:
            if name:
                self.contacts[phone]['name'] = name
            if email:
                self.contacts[phone]['email'] = email
            print("Updated successfully")
        else:
            print("No results found")

    # deleting the contact details
    def deleteContact(self, phone):
        if phone in self.contacts:
            del self.contacts[phone]
            print("Contact deleted successfully")
        else:
            print("No results found")

    # to select the fuction for processing the program       
    def selectFunction(self):
        while True:
            print("\nContact Book")
            print("1. Add Contact")
            print("2. View Contact")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")
            choice = input("Enter your choice: ")
            
            if choice == '1':
                name = input("Enter the name: ")
                phone = int(input("Enter the phone no.: "))
                email = input("Enter the email: ")
                self.addContact(name, phone, email)
                
            elif choice == '2':
                self.viewContacts()
                
            elif choice == '3':
                search_item = input("Enter the name or phone number to search: ")
                self.searchContact(search_item)
                
            elif choice == '4':
                phone = int(input("Enter the phone number of the contact to update: "))
                name = input("Enter new name (leave blank to keep current): ")
                email = input("Enter new email (leave blank to keep current): ")
                self.updateContact(phone, name, email)
                
            elif choice == '5':
                phone = input("Enter the phone number of the contact to delete: ")
                self.deleteContact(phone)
                
            elif choice == '6':
                break
            else:
                
                print("Invalid choice... Please enter a valid choice")

# creating object to describe the class
contactDetails = ContactBook()
contactDetails.selectFunction()
