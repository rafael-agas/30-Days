# Modules
from random import *
import string

'''
def random_user_id():
   characters = string.ascii_lowercase + string.digits
   user = random.sample(characters, 6)
   return ''.join(user)
print(random_user_id()) '''


"""def random_user_id_by_user():
   number = input("Number of Characters:")
   number_ids = input("Number of Ids: ")
   characters = string.ascii_lowercase + string.digits
   for i in range(int(number_ids)):
      user = random.sample(characters, int(number))
      print(''.join(user))
random_user_id_by_user()
"""

def rgb_color_gen(nums):
   return ["rgb({},{},{})".format(randint(0, 255), randint(0, 255), randint(0, 255)) for i in range(nums)]

def list_of_hexa_colors(nums):
   hex_number = string.hexdigits
   return [('#' + "".join(sample(hex_number, 6))) for i in range(nums)]

def generate_colors(type, nums):
   color_type = {'hexa': list_of_hexa_colors, 'rgb': rgb_color_gen}
   if type not in color_type or not isinstance(nums, int):
      raise ValueError("Please choose hexa or rgb or you entered an invalid number")
   while True:
      try: 
         return color_type[type](nums)
      except Exception as error:
         print(str(error))
         print("Please chooose a valid color type or number")

code = input("Which type of color code? ")
amount = input("How many do you need? ")
print(generate_colors(code, int(amount)))
