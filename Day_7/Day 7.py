# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

len(it_companies)
it_companies.add("Twitter")
it_companies.update(["Accenture", "Infosys", "Tata"])
it_companies.remove("Tata")
# Difference between discard and remove:
# Remove: removes a specific item in set, raises errors if not found in set
# Discard: removess a specific item in set, ignores if not found in set

A_B = A.union(B)
print(A_B)
A_intersect_B = A.intersection(B)
print(A_intersect_B)
print(A.issubset(B))
print(A.isdisjoint(B))
B_A = B.union(A)
set_diff = A.symmetric_difference(B)
print(set_diff)
del A
del B

#--------------------------
set_age = set(age)
print(len(age), len(set_age))
# string: text
# list: a collectoin of items that are mutable; ordered
# tuple: a collection of items that are immutable; ordered
# set: a collection of items. items are immutable; unordered; no dupes


sentence = "I am a teacher and I love to inspire and teach people"

def is_unique(words):
   list_words = words.split(" ")
   unique = set()
   for word in list_words:
      unique.add(word)
   return len(unique)

print(is_unique(sentence))