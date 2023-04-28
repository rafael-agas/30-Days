age = input("Enter your age: ")
if int(age) >= 18:
    print("You are old enough to learn to drive.")
else:
    print("You need " + str(18 - int(age)) + " more years to learn to drive.")


if int(age) == 26:
    print("We are the same age!")
elif int(age) - 26 == 1 :
    print("You are one year older than me.")
elif int(age) > 26:
    print("You are " + str(int(age) - 26) + "years older than me.")
else:
    print("You are " + str(26 - int(age)) + "years younger than me.")

person={
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

if 'skills' in person:
   print(person['skills'][len(person['skills']) // 2])
   print('Python' in person['skills'])
if 'Javascript' in person['skills'] and 'React' in person['skills'] and len(person['skills']) == 2:
    print("He is a front-end developer.")
elif 'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills'] and len(person['skills']) == 3:
    print("He is a back-end developer.")
elif 'Node' in person['skills']  and 'React' in person['skills'] and 'MongoDB' in person['skills']:
    print("He is a full-stack developer")
else:
    print("Unknown title.")