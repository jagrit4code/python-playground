contacts = {}
while True:
    print("1.add a contact ")
    print("2.view all contacts")
    print("3.search for an existing contact")
    print("4.exit the contact book")
    choice = int(input("enter your choice"))
    if choice == 1:
        name_input = input("enter the person's name ")
        number_input = input("enter the number of the person")
        contacts[name_input] = number_input
    elif choice == 2:
        if  len(contacts) == 0:
            print("no contacts yet!")
        else:
            for name_input, number_input in contacts.items():
                print(f"{name_input}: {number_input}")
    elif choice == 3:
        print("that feature is not available yet....")
        print("....wait , its just been added ")
        search_input = input("enter the name to search: ")
        if  len(contacts) == 0:
            print("no contacts yet!")
        else:
            if search_input in contacts:
                print(contacts[search_input])
            else:
                print("contact not found")
    elif choice == 4:
        print("thanks for using the contact book ")
        break
    else:
        print("enter a valid choice ")