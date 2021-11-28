contacts = [{'First name': 'Niklas', 'Last name': 'Rex', 'Phone': '0176/312456', 'Street': 'Meierstraße 23', 'Postal code': '21255', 'City': 'Hamburg'}, {'First name': 'Annika', 'Last name': 'Rex', 'Phone': '0176/312356', 'Street': 'Müllerstraße', 'Postal code': '21234', 'City': 'Düsseldorf'}]

def create_contact():
    while True:
        new_contact = {}
        for key in contacts[0]:
            value = input(f'{key}: ')
            new_contact[key] = value
        contacts.append(new_contact)
        print(contacts)
        print('Contact created.')
        choice = input('Do you want to create another contact? (y/n): ')
        if choice != 'y':
            break 

def update_search_contact(i):
    print('Updating a contact')   



def update_contact():
    print('Updating a contact')



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
    search = input('Please enter your search: ')
    hit = None
    i = 0
    while i < len(contacts):
        for key in contacts[i]:
            if search in contacts[i][key]:
                print('\nContact found:')
                for key in contacts[i]:                    
                    print(f'{key}: {contacts[i][key]}')
                print("\n")
                hit = input('Is this the contact you are looking for (y/n)?: ')
        if hit == 'y':
            change_contact = input('Do you want to update or delete this contact (1 = update, 2 = delete, 3 = no changes)?: ')
            if change_contact == '1':
                update_search_contact(i)
                break
            elif change_contact == '2':
                delete_search_contact(i)
                print('\nClosing application.')
                break
            else:
                print('\nClosing application.')
                break
        i += 1

def show_contacts():
    i = 0
    while i < len(contacts):
        print(f"\nContact {i+1}:")
        for key in contacts[i]:
            print(f"{key}: {contacts[i][key]}")
        i += 1

while True:

    print('\nWelcome to your contact book!\n1 = Create contact\n2 = Update contact\n3 = Delete contact\n4 = Search contact\n5 = Show all contacts\n6 = Close contact book')
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
        print('Application closed.')
        break  

    else:
        print('You didn\'t choose a valid option.\nApplication closed.')
        break

