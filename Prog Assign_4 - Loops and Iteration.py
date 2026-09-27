# Author: Lewis Johnson
# Program: Prog Assign_4 - Loops and literation
# Date: Sept, 26 , 2026
# Git hub link

# Value counter for the bugs collected
total_bugs = 0
# Setting days of the week to go through the loop
for day in range(1, 6):
    # Interface for the user to input the number of bugs collected for the day asked
    bugs_today = int(input(f"Enter the number of bugs collected on day {day}: "))
    # Adding the number of bugs collected to the total collected
    total_bugs += bugs_today
# Out put to the user to see the number of bugs collected
print(f"\nTotal number of bugs collected over 5 days: {total_bugs}")

# Get number of years from user
num_years = int(input("Enter the number of years: "))

# Initialize variables
total_rainfall = 0
total_months = 0

# Outer loop for each year
for year in range(num_years):
    print(f"\nYear {year + 1}")
    print("-" * 10)

    # Inner loop for each month
    for month in range(12):
        # Get rainfall for the month
        rainfall = float(input(f"Enter inches of rainfall for month {month + 1}: "))

        # Add to total rainfall and months
        total_rainfall += rainfall
        total_months += 1

# Calculate average rainfall per month
average_rainfall = total_rainfall / total_months

# Display results
print("\n" + "=" * 30)
print("Rainfall Statistics")
print("=" * 30)
print(f"Number of months: {total_months}")
print(f"Total inches of rainfall: {total_rainfall:.2f}")
print(f"Average rainfall per month: {average_rainfall:.2f} inches")
