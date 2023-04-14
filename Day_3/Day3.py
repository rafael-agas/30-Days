age = 26
height = 5.75
complex_number = 1 + 1j

print(type(age))
print(type(height))
print(type(complex_number))

base = input("Enter base: ")
triangle_height = input("Enter height: ")
area = (float(base) * float(triangle_height)) / 2
print("The area of the trianagle is " + str(area))


side_a = input("Enter side a: ")
side_b = input("Enter side b: ")
side_c = input("Enter side c: ")
perim = int(side_a) + int(side_b) + int(side_c)
print("The perimeter of the triangle is "  + str(perim))

rec_a = input("Enter side a: ")
rec_b = input("Enter side b: ")
area_rec = int(rec_a) * int(rec_b)
perim_rec = (int(rec_a) + int(rec_b)) * 2
print("The area of the rectangle is " + str(area_rec), 
      "The perimeter of the rectangle is " + str(perim_rec))\


radius = input("Enter radius: ")
area_circ = 3.14 * float(radius) ** 2
circum = 3.14 * float(radius) * 2
print("The area of the circle is " + str(area_circ), 
      "The circumference of the circle is " + str(circum))

slope = (10- 2)/(6 - 2)
euclid = ((6 - 2) ** 2 + (10 - 2) ** 2) ** (1/2)

print(bool(len("python") > len("dragon")))

data = ["python", "dragon"]
for word in data:
    print(bool("on" in word))

print(bool((7 // 3) == 2.7))

'''Calculate Pay'''
hours = input("Enter hours worked: ")
rate = input("Enter hourly rate: ")
print("Your weekly earnings: " + str((int(hours) * int(rate))))

'''Years lived in seconds'''
age_here = input("Enter number of years lived: ")
age_in_seconds = (((float(age_here) * 356) * 24) * 60) * 60
print("You have lived for "  + str(age_in_seconds) + " seconds")

numbers = [1, 2, 3, 4, 5]
for i in numbers:
    print(i, 1, i**1, i**2, i**3)