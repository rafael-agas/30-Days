empty_tuple = ()
siblings = ("Sharon", "Karen", "Jordan")
print(len(siblings))
family_members = siblings + ("Rose", "Someone")
print(family_members)
# -----
(younger, middle, youngest, *parents) = family_members
print(younger, middle, youngest)
print(parents)

fruits = ("melon", "banana", "mango", "strawberry")
vegetables = ("lettuce", "pumpkin", "bokchoy")
animal_products = ("eggs", "milk")
food_stuff_tp = fruits + vegetables + animal_products
food_list = list(food_stuff_tp)
first_three = food_stuff_tp[0:3]
print(first_three)
middle_food = food_stuff_tp[int((len(food_stuff_tp) - 1) / 2)]
print(middle_food)
last_three = food_stuff_tp[-3:len(food_stuff_tp)]
print(last_three)
del food_stuff_tp

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)