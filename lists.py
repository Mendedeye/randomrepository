#Task 1: Accessing a Value
print("\n\nTask 1\n")

code_languages = ["JavaScript", "Python", "Java", "Django", "React"]

print(f"This is the second language on the list: {code_languages[1]}")

#Task 2: Adding and Changing Values
print("\n\nTask 2\n")

instructors = ["Nevin", "Mike", "Jake", "Dan", "Megan"]

instructors.append("Dan") 
instructors.append("James")
instructors.append("John-Boy")

instructors.remove("Dan")
instructors.append("Danimal")

for names in instructors:
    print(names)

#Task 3: Popping a Value
print("\n\nTask 3\n")

instructors.pop(6)

for names in instructors:
   print(names)

#Task 4: Removing a Value
print("\n\nTask 4\n")

instructors.remove("Mike")

for names in instructors:
    print(names)

#Task 5: Looping over a List
print("\n\nTask 5\n")

list_1 = ["fan", "bull-", "high-", "barrel-o-", "slap"]
list_2 = ["dango", "rider", "horse", "monkeys", "stick"]
count = 0

for word in list_1:
    print(word + list_2[count])
    count += 1

#Task 6: List Checker
print("\n\nTask 6\n")

is_duplicate = False
first_name = input("Please enter in a first name of an instructor: ")

for name in instructors:
    if first_name == name:
        is_duplicate = True
        break

if is_duplicate == False:
    instructors.append(first_name)
    for name in instructors:
        print(name)
else:
    print("\nSorry that name has been provided please provide a nickname")

#Task 7: Joining Lists
print("\n\nTask 7\n")

first_destinations = ["Alaska", "Disneyland"]
second_destinations = ["Denmark", "Israel", "Germany"]
third_destinations =[]

print("\n\n\tMethod 1") #extend() list joining
first_destinations.extend(second_destinations)
for location in first_destinations:
    print(f"\t\t{location}")

print("\n\n\tMethod 2") #append() list joining
first_destinations = ["Alaska", "Disneyland"]
for location in second_destinations:
    first_destinations.append(location)

for location in first_destinations:
    print(f"\t\t{location}")

print("\n\n\tMethod 3") #'+' list joining
first_destinations = ["Alaska", "Disneyland"]
third_travel = first_destinations + second_destinations

for location in third_destinations:
    print(f"\t\t{location}")

#Task 8: Copy Lists
print("\n\nTask 8\n")

fav_vehicles = ["4Runner", "Hellcat", "Tacoma"]
copy_1 = []
copy_2 = []
copy_3 = []

print("\n\n\tMethod 1") # append() list copying
for car in fav_vehicles:
    copy_1.append(car)

for car in copy_1:
    print(f"\t\t{car}")

print("\n\n\tMethod 2") # copy() list copying

copy_2 = fav_vehicles

for car in copy_2:
    print(f"\t\t{car}")

print("\n\n\tMethod 3") # loop list copying

copy_3 = list(fav_vehicles)

for car in copy_3:
    print(f"\t\t{car}")

#Task 9: Sort Lists
print("\n\nTask 9\n")

fav_food_dishes = ["Grilled Chicken", "Pizza", "Quesadia", "Chicken wrap", "Crumble Cookies"]

print("\n\n\tMethod 1") # sort() asscending

fav_food_dishes.sort(reverse=True)

for dish in fav_food_dishes:
    print(f"\t\t{dish}")

print("\n\n\tMethod 2") # sort() descending

fav_food_dishes.sort(reverse=False)

for dish in fav_food_dishes:
    print(f"\t\t{dish}")

print("\n\n\tMethod 3") # bubble sort alphabetic asscending