empty_list = []
not_empty_list = ["Apples", "Mangoes", "Pineapples", "Lychee", "Pears"]
print(len(not_empty_list))
print(not_empty_list[0], not_empty_list[len(not_empty_list) - 1], not_empty_list[int((len(not_empty_list)- 1) / 2)])
mixed_data_types = ["Rafael", 26, 178, "Single", "Seattle"]
companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(companies)
print(len(companies))
print(companies[0], companies[len(companies) - 1], companies[int((len(not_empty_list)- 1) / 2)])
companies[3] = "Meta"
print(companies)
companies[2] = companies[2].upper()
print(companies)
companies.append("Elsevier")
companies.insert(int((len(companies)) / 2), "Alibaba")
print("Facebook" in companies)
companies.sort()
print(companies)
companies.reverse
print(companies)
first_three = companies[0:3]
last_three = companies[-3:]
print(first_three)
print(last_three)
if len(companies) % 2 == 0:
   middle_company = companies[int((len(companies)- 1) / 2)]
else:
   middle_company = companies[int((len(companies)- 1) / 2): int((len(companies)- 1) / 2) + 2]
print(middle_company)
del companies[0]
del companies[len(companies) - 1]
del companies[int((len(companies)- 1) / 2)]
companies.clear()
front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", " Express", "MondoDB"]
full_stack = front_end + back_end
redux_index = full_stack.index("Redux") + 1
full_stack.insert(redux_index,"Python")
full_stack.insert(redux_index,"SQL")
print(full_stack)

#Exercise 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort
min_age = ages[0]
print(min_age)
max_age = ages[len(ages) - 1]
print(max_age)
ages.append(min_age)
ages.append(max_age)
range = max_age - min_age
print(range)
average = sum(ages) / len(ages)
median_age = 0
if len(ages) % 2 == 0:
   lower_median = ages[int((len(ages) - 1) / 2)]
   upper_median = ages[(int((len(ages) - 1) / 2)) + 1]
   median_age = (lower_median + upper_median) / 2
else:
   median_age = ages[int(len(ages - 1) / 2)]
print(median_age)
print(bool(abs(min_age - average) == abs(max_age - average)))

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_country, second_country, third_country, *scandic_countries = countries
print(first_country)
print(second_country)
print(third_country)
print(scandic_countries)