person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if person.get('skills'):
    if len(person['skills']) % 2 == 0:
        print(person['skills'][(len(person['skills'])//2) - 1],
              person['skills'][(len(person['skills'])//2)])
    else:
        print(person['skills'][len(person['skills'])//2])
else:
    print("No Skills")

if person.get('skills'):
    if 'Python' in person.get('skills'):
        print("Python is one of the skills")
    else:
        print("No Python in skills")
else:
    print("No Skills")

if person.get('skills'):
    if 'Javascript' in person.get('skills') and 'React' in person.get('skills'):
        print('He is a front end developer')
    elif 'Node' in person.get('skills') and 'Python' in person.get('skills') and 'MongoDB' in person.get('skills'):
        print('He is a backend developer')
    elif 'Node' in person.get('skills') and 'React' in person.get('skills') and 'MongoDB' in person.get('skills'):
        print('He is a fullstack developer')
    else:
        print('unknown title')
else:
    print("No Skills")