dog = {}
dog['name'] = 'Poppy'
dog['color'] = 'Brown'
dog['breed'] = 'Corgi'
dog['legs'] = 'Short'
dog['age'] = 2

student = {'first_name' : 'Rafael', 'last_name' : 'Agas', 'Gender' : 'Man', 'Age' : '26',
           'Marital Status' : 'Single', 'Skills' : ['Java', 'Python', 'C'], 'Country' : 'US', 'City' : 'Redmond',
           'address'  : {'street' : 'Roosevelt', 'Zipcode' : '98122'}}

print(len(student))
print(student['Skills'])
student['Skills'].append("HTML")
student['Skills'].append('CSS')
print(student['Skills'])

print(student.keys())
print(student.values())
student_list = student.items()
print(student_list)
student.pop('address')
print(student)
del student