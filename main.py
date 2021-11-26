contacts = [{'Vorname': 'Niklas', 'Nachname': 'Rex', 'Telefon': '0176/312456', 'Straße': 'Weg zur Mühle 11D', 'PLZ': '21244', 'Ort': 'Buchholz'}]
new_contact = {'Vorname': 'Annika', 'Nachname': 'Rex', 'Telefon': '0176/312356', 'Straße': 'Weg zur Mühle 11D', 'PLZ': '21244', 'Ort': 'Buchholz'}
contacts.append(new_contact)

i = 0

while i < len(contacts):
    print(f"Kontakt: {i+1}")
    for key in contacts[i]:
        print(f"{key}: {contacts[i][key]}")
    print("\n")
    i += 1

def create_contact():
    pass

def search_contact():
    pass

def delete_contact():
    pass

def show_contacts():
    pass
