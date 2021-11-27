contacts = [{'First name': 'Niklas', 'Last name': 'Rex', 'Phone': '0176/312456', 'Street': 'Weg zur Mühle 11D', 'Postal code': '21244', 'City': 'Buchholz'}]
new_contact = {'First name': 'Annika', 'Last name': 'Rex', 'Phone': '0176/312356', 'Street': 'Weg zur Mühle 11D', 'Postal code': '21244', 'City': 'Buchholz'}
contacts.append(new_contact)

# i = 0
# while i < len(contacts):
#     print(f"Kontakt: {i+1}")
#     for key in contacts[i]:
#         print(f"{key}: {contacts[i][key]}")
#     print("\n")
#     i += 1

def create_contact():
    print('Creating a new contact')



def update_contact():
    print('Updating a contact')



def delete_contact():
    print('Deleting a contact')

search = '21244'

def search_contact():
    i = 0
    while i < len(contacts):
        for key in contacts[i]:
            if search in contacts[i][key]:
                for key in contacts[i]:
                    print(f'{key}: {contacts[i][key]}')
                print("\n")
                hit = input('Is this the contact you are looking for (y/n)?: ')
        if hit == 'y':
            change_contact = input('Do you want to update or delete this contact (1 = update, 2 = delete, 3 = no changes)?: ')
            if change_contact == '1':
                update_contact(contacts[i])
            elif change_contact == '2':
                delete_contact(contacts[i])
            else:
                break
        i += 1

search_contact()