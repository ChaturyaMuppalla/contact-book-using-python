contact={}
print("* * * * * * * * * * * * * * * * * * * * * * * * * * ")
print("~~~~~~~~~~~~~~~~~~~~CONTACT BOOK~~~~~~~~~~~~~~~~~~~~")
print("* * * * * * * * * * * * * * * * * * * * * * * * * * ")

def display_contact():
    print("Name\t\tContact Number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key))) 
              
while True:
    print("\t ---------------MENU---------------")
    print("1.Add new contact")
    print("2.Search a contact")
    print("3.Display all contacts")
    print("4.Edit a contact")
    print("5.Delete a contact")
    print("6.Exit")
    choice = int(input("Enter your choice : "))
    print("\n")
    if choice==1:
        name=input("Enter the contact name : ")
        phone=input("Enter the mobile number : ")
        contact[name]=phone
    elif choice==2:
        search_name=input("Enter the contact name : ")
        if search_name in contact:
            print(search_name,"'s contact number is : ",contact[search_name])
        else:
            print("Name is not found in contact book")
    elif choice==3:
        if not contact:
            print("Empty contact book")
        else:
            display_contact()
    elif choice==4:
              edit_contact=input("Enter the contact to be edited : ")
              if edit_contact in contact:
                  phone=input("Enter mobile number : ")
                  contact[edit_contact]=phone
                  print("contact updated")
                  display_contact()
              else:
                print("Name is not found in contact book")
                 
    elif choice==5:
              del_contact=input("Enter the contact to be deleted : ")
              if del_contact in contact:
                  confirm=input("Do you want to delete this contact y/n? ")
                  if confirm=='y' or confirm=='Y':
                      contact.pop(del_contact)
                  display_contact()
              else:
                  print("Name is not found in contact book")
    else:
        print("END")
        breakcontact={}
print("* * * * * * * * * * * * * * * * * * * * * * * * * * ")
print("~~~~~~~~~~~~~~~~~~~~CONTACT BOOK~~~~~~~~~~~~~~~~~~~~")
print("* * * * * * * * * * * * * * * * * * * * * * * * * * ")

def display_contact():
    print("Name\t\tContact Number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key))) 
              
while True:
    print("\t ---------------MENU---------------")
    print("1.Add new contact")
    print("2.Search a contact")
    print("3.Display all contacts")
    print("4.Edit a contact")
    print("5.Delete a contact")
    print("6.Exit")
    choice = int(input("Enter your choice : "))
    print("\n")
    if choice==1:
        name=input("Enter the contact name : ")
        phone=input("Enter the mobile number : ")
        contact[name]=phone
    elif choice==2:
        search_name=input("Enter the contact name : ")
        if search_name in contact:
            print(search_name,"'s contact number is : ",contact[search_name])
        else:
            print("Name is not found in contact book")
    elif choice==3:
        if not contact:
            print("Empty contact book")
        else:
            display_contact()
    elif choice==4:
              edit_contact=input("Enter the contact to be edited : ")
              if edit_contact in contact:
                  phone=input("Enter mobile number : ")
                  contact[edit_contact]=phone
                  print("contact updated")
                  display_contact()
              else:
                print("Name is not found in contact book")
                 
    elif choice==5:
              del_contact=input("Enter the contact to be deleted : ")
              if del_contact in contact:
                  confirm=input("Do you want to delete this contact y/n? ")
                  if confirm=='y' or confirm=='Y':
                      contact.pop(del_contact)
                  display_contact()
              else:
                  print("Name is not found in contact book")
    else:
        print("END")
        break
