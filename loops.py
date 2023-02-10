#Task 1: Five Hellos

for number in range(5):
    print("Hello")

#Task 2: Counting
print("\n\n")

for number in range(11):
    print(number)

#Task 3: Counting Backwards
print("\n\n")

for number in range (10,0,-1):
    print(number)

#Task 4: Prompted Output
user_count = input("\n\nPlease tell me how many times you want 'devCodeCamp' printed: ")

for number in range(int(user_count)):
    print("devCodeCamp")

#Task 5: Packers Split-up
print("\n\n")

packers = "Packers"

for character in packers:
    print(character)

#Task 6: Fizz Bizz
print("\n\n")

for number in range(101):
    if  number % 15 == 0 and number != 0:
        print("fizzbuzz")
    elif number % 5 == 0 and number != 0:
        print("buzz")
    elif number % 3 == 0 and number != 0:
        print("fizz")
    else:
        print(number)

#Task 7: Five Hellos(again)
print("\n\n")

count = 0
stop_case = 5

while count <= stop_case:
    print("Hello")
    count += 1

# Task 8: Validation
user_password = input("\n\nPlease put in a password: ")

user_password_verified = input("\nPlease put in password again: ")

while user_password != user_password_verified:
    user_password_verified = input("\nPlease put in password agian: ")

print("\nUser Validated")