import time

contacts = [{'First name': 'Niklas', 'Last name': 'Rex', 'Phone': '0176/312456', 'Street & Streetnumber': 'Meierstraße 23', 'Postal code': '21255', 'City': 'Hamburg'}, {'First name': 'Annika', 'Last name': 'Rex', 'Phone': '0176/312356', 'Street & Streetnumber': 'Müllerstraße 25', 'Postal code': '21234', 'City': 'Düsseldorf'}]

def create_contact():
    while True:
        new_contact = {}
        for key in contacts[0]:
            value = input(f'{key}: ')
            new_contact[key] = value
        contacts.append(new_contact)
        print('\nContact created.')
        choice = input('Do you want to create another contact? (y/n): ')
        if choice != 'y':
            break 

def update_search_contact(i):
    while True:
        a = 1
        print('\nWhich entry do you want to update?')
        for key in contacts[i]:
            print(f'{a} = {key}: {contacts[i][key]}')
            a += 1
        try:
            choice = int(input('Please enter the number you want to update (e.g. 1 for First name): '))
            if choice <= len(contacts[i]):
                chosen_key = list(contacts[i])[choice-1] 
                print(f'\nCurrent value for {chosen_key}: {contacts[i][chosen_key]}')  
                new_value = input('Please enter a new value: ')
                contacts[i][chosen_key] = new_value
                print(f'{chosen_key} value has been updated.')
                choice = input('\nDo you want to update another entry? (y/n): ')
                if choice != 'y':  
                    break
            
            else:
                print('Please enter one of the given numbers')        
        
        except ValueError:
            print('Please enter a valid number.')


def update_contact():
    while True:
        show_contacts()        
        try:
            choice = int(input('\nPlease enter the contact number you want to update (e.g. 1 for contact 1): '))
            if choice <= len(contacts) and choice > 0:
                update_search_contact(choice-1)
                choice = input('Do you want to update another contact? (y/n): ')
                if choice != 'y':
                    break
        
        except ValueError:
                print('Please enter a valid number.')
                choice = input('Do you want to update another contact? (y/n): ')
                if choice != 'y':
                    break


def delete_search_contact(i):
    confirmation = input('Are you sure you want to delete this contact? (y/n): ')
    if confirmation == 'y':
        del contacts[i]
        print('This contact has been deleted.')
    else:
        print('This contact remains unchanged.')


def delete_contact():
    show_contacts()
    while True:        
        try:
            choice = int(input('\nPlease enter the contact number you want to delete (e.g. 1 for contact 1): '))
            if choice <= len(contacts) and choice > 0:
                del contacts[choice-1]
                print('\nContact deleted.')
                choice = input('Do you want to delete another contact? (y/n): ')
                if choice != 'y':
                    break
            else:
                print('\nThis contact doesn\'t exist')
                choice = input('Do you want to delete another contact? (y/n): ')
                if choice != 'y':
                    print('\nClosing application.')
                    break
        except ValueError:
            print('Please enter a valid number.')
            choice = input('Do you want to delete another contact? (y/n): ')
            if choice != 'y':
                break

def search_contact(): 
    searching = True
    while searching:
        search = input('Please enter your search: ')
        hit = None
        contact_found = False
        i = 0
        while i < len(contacts):
            for key in contacts[i]:
                if search in contacts[i][key]:
                    contact_found = True
                    print('\nContact found:')
                    for key in contacts[i]:                    
                        print(f'{key}: {contacts[i][key]}')
                    print("\n")
                    hit = input('Is this the contact you are looking for (y/n)?: ')
            if hit == 'y':
                change_contact = input('Do you want to update or delete this contact (1 = update, 2 = delete, 3 = no changes)?: ')
                if change_contact == '1':
                    update_search_contact(i)
                    choice = input('\nDo you want to do another search? (y/n): ')
                    if choice == 'y':
                        break
                    else:
                        searching = False
                elif change_contact == '2':
                    delete_search_contact(i)
                    choice = input('\nDo you want to do another search? (y/n): ')
                    if choice == 'y':
                        break
                    else:
                        searching = False
                else:
                    break
            else: contact_found = False
            i += 1
        if contact_found == False:
            print('\nNo contact found.')
            choice = input('Do you want to do another search? (y/n): ')
            if choice != 'y':
                break


def show_contacts():
    i = 0
    while i < len(contacts):
        print(f"\nContact {i+1}:")
        for key in contacts[i]:
            print(f"{key}: {contacts[i][key]}")
        i += 1

def export_contacts():
    timestr = time.strftime("%Y%m%d")
    contact_export = open(f"contact_book_export_{timestr}.txt", 'w')
    i = 0
    while i < len(contacts):
        contact_export.write(f"Contact {i+1}:")
        for key in contacts[i]:
            contact_export.write(f"\n{key}: {contacts[i][key]}")
        contact_export.write('\n\n')
        i += 1
    print('\nContacts exported.')

while True:

    print('\nWelcome to your contact book!\n1 = Create contact\n2 = Update contact\n3 = Delete contact\n4 = Search contact\n5 = Show all contacts\n6 = Export contacts\n7 = Close contact book')
    action = input('Please choose an option: ')

    if action == '1':
        create_contact()

    elif action == '2':
        update_contact()

    elif action == '3':
        delete_contact()

    elif action == '4':
        search_contact()

    elif action == '5':
        show_contacts()

    elif action == '6':  
        export_contacts()

    elif action == '7':
        print('Application closed.')
        break 

    else:
        print('You didn\'t choose a valid option.\nApplication closed.')
        break

