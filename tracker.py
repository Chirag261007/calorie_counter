
# tracker.py
# Name: chirag
# Date: 2025-10-20
# Project: Daily Calorie Tracker

# This program helps you track what you eat and how many calories you take in a day

import datetime  # for saving time in the report

# Welcome message
print("===================================")
print("  Hey there! Welcome to your Daily Calorie Tracker!")
print("===================================\n")
print("This simple tool will help you:")
print("- Record what you've eaten today")
print("- Count your total and average calories")
print("- See if you're under or over your calorie goal\n")

# Lists to store meals and calories
meal_names = []
calorie_amounts = []

# Ask how many things they ate
meal_count = int(input("How many meals or snacks did you have today? "))

# Loop to collect each meal/snack info
for i in range(meal_count):
    print(f"\nEntry #{i + 1}")
    meal = input("What did you eat? (e.g., Breakfast, Chips, Dinner): ")
    calories = float(input("About how many calories was that? "))
    
    # Save to lists
    meal_names.append(meal)
    calorie_amounts.append(calories)

# Calculate total and average
total_calories = sum(calorie_amounts)
average_calories = total_calories / len(calorie_amounts)

# Ask for user's calorie goal
daily_limit = float(input("\nWhat's your calorie target for today? "))

# Check if user is within or over limit
if total_calories > daily_limit:
    limit_message = "Looks like you've gone over your calorie target today."
else:
    limit_message = "You're within your calorie goal. Well done!"

# Show a simple summary
print("\n===================================")
print("       What You Ate Today       ")
print("===================================\n")
print("Item\t\tCalories")
print("-----------------------------")
for meal, cal in zip(meal_names, calorie_amounts):
    print(f"{meal}\t\t{cal}")
print("-----------------------------")
print(f"Total:\t\t{total_calories}")
print(f"Average:\t{round(average_calories, 2)}")
print(limit_message)

# Ask if they want to save this log
save_report = input("\nWant to save this summary to a file? (yes/no): ").lower()

if save_report == "yes":
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = "calorie_report.txt"

    with open(filename, "w") as file:
        file.write("Daily Calorie Tracker Report\n")
        file.write(f"Date: {timestamp}\n\n")
        file.write("Meal\tCalories\n")
        file.write("-----------------------------\n")
        for meal, cal in zip(meal_names, calorie_amounts):
            file.write(f"{meal}\t{cal}\n")
        file.write("-----------------------------\n")
        file.write(f"Total:\t{total_calories}\n")
        file.write(f"Average:\t{round(average_calories, 2)}\n")


