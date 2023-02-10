#Task 1: Driving age
legal_driving_age = 16
user_age = input("Please enter in your current age: ")

if int(user_age) >= legal_driving_age:
    print("You are legally able to drive.")
else:
    print("You are not old enough to drive yet.")

#Task 2: Random Number
import random

random_number = random.randrange(11)

if random_number >= 0 and random_number < 3:
    print("0, 1, or 2")
elif random_number >= 3 and random_number < 6:
    print("3, 4, or 5")
elif random_number >= 6 and random_number < 9:
    print("6, 7, or 8")
else:
    print("9 or 10")

#Task 3: NFL Teams
nfl_team = input("Please enter in your favorite NFL team's name: ")

if nfl_team == "Bears":
    print("Quarterback much?")
elif nfl_team == "Vikings":
    print("Loud noises")
elif nfl_team == "Lions":
    print("LOL They bad")
elif nfl_team == "49ers":
    print("Packer beaters")
elif nfl_team == "Packers":
    print("Best team in the world! In the universe!")
else:
    print("Pick a different team")

