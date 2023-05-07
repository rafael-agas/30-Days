#list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
print([i for i in numbers if i <= 0])

list_of_lists = [[[1,2,3]],[[4,5,6]],[[7,8,9]]]
flat = [i for sublist in list_of_lists for subsublist in sublist for i in subsublist]
print(flat)

k = [(i, 1, i * i, i ** 2, i ** 3, i ** 4, i ** 5) for i in range(11)]
print(k)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output = [[country.upper(), country[:3].upper(), city.capitalize()] for [(country, city)] in countries]
print(output)
dict_output = [{'country' : country, 'city' : city} for [(country, city)] in countries]
print(dict_output)
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Barack', 'Obama')], [('Bill', 'Gates')]]
name_concat = [first + " " + last for (first, last) in names]
print(name_concat)

#lambda funcion

slope = lambda y, x, b: (y - b) / x
print(slope(1, 2, 3))