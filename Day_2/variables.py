'''Day 2 of 30 Days of Python'''
import math

first_name = "Rafael"
last_name = "Agas"
full_name = first_name + last_name
country = "USA"
city = "Renton"
age = 26
year = 2023
is_married = "No"
is_true, is_light_on, = True, False

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_light_on))
print(type(is_married))
print(type(is_true))

print("The length of my first name is " + str(len(first_name)))
print("The length of my last name is " + str(len(last_name)))
if len(first_name) > len(last_name):
    print("My first name is longer by " + str(len(first_name) - len(last_name)) + " letters")
elif len(first_name) < len(last_name) :
    print("My last name is longer by " + str(len(last_name) - len(first_name)) + " letters")
else:
   print("Both names are equal length")

num_one = 5
num_two = 4
diff = num_two - num_one
product = num_two * num_one
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ^ num_two
floor_division = num_one // num_two

area_of_circle = math.pi * math.pow(30, 2)
cicrum_of_circle = math.pi * (30 * 2)
radius = input("Enter an radius for a circle: ")
area_user_circle = math.pi * math.pow(int(radius), 2)
print(area_user_circle)

f_name = input("what is your first name? ")
l_name = input("What is your last name? ")
home_country = input("What country do you live in? ")
age_now = input("what is your age? ")

print(f_name, l_name, home_country, str(age))