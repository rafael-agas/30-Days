# Functions
# Counting the number of even and odds

def even_and_odds(nums):
   even = 0
   odd = 0
   i = 0
   while i <= nums:
      if i % 2 == 0:
         even += 1
      else:
         odd += 1
      i += 1
   print("Number of evens: " + str(even))
   print('Number of odds: ' + str(odd))

even_and_odds(100)

def factorial(nums):
   number = 1
   for i in range(1, nums):
      number += i * number
   return number

print(factorial(15))

# Prime number finder
def is_prime(nums):
   prime = False
   if nums == 1:
      return prime
   for i in range(2, nums):
      if nums % i == 0:
         prime = True
      return prime
   return prime

print(is_prime(6))