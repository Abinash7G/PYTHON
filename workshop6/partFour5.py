time_elapsed = int(input("Enter the number of seconds that have elapsed since you dropped the food: "))

if time_elapsed < 5:
    print("It's not okay to eat that. It's been on the floor for too short a time.")
elif time_elapsed < 60:
    print("It's probably okay to eat that. It's been on the floor for less than a minute.")
else:
    print("It's probably okay to eat that. It's been on the floor for more than a minute.")
