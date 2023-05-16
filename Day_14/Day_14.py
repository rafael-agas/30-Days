# Higher Order Functions
# map() takes a function and iterables as parameters. Applies the function to each iterable
# filter() takes a function and iterables as parameters. Applies a boolean to each iterable.
# reduce() functools module. Takes  a function and iterables as parameters. Returns a single value.
# Higher order Function takes a function as a parameter or returns a function
# Closures are nested functions where the inner fucntion can access the outer function variables. returns the nested function
# Decorators is a way to add a new functionality to a function without changing the function. Uses wrapper() and returns it

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# New list of uppercase countries
countries_upper = map(lambda x: x.upper(), countries)
print(list(countries_upper))

numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))

names_upper = map(lambda x: x.upper(), names)
print(list(names_upper))

def contains_land(l):
   if l.find('land') > 0:
      return True
   return False
land_filter = filter(contains_land, countries)
print(list(land_filter))

def country_length(l):
   if len(l) == 6:
      return True
   return False
six = filter(country_length, countries)
print(list(six))

def more_than_six(l):
   if len(l) >= 6:
      return True
   return False
m = filter(more_than_six, countries)
print(list(m))

def start_e(l):
   if l.find('E') == 0:
      return True
   return False
k = filter(start_e,countries)
print(list(k))

g = map(lambda x : x.upper(), filter(start_e, countries))
print(list(g))

def get_string(l):
   return [word for word in l if type(word) == str]

