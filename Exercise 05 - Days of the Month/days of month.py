months = {
    1: 31, 2: 28, 3: 31, 4: 30,
    5: 31, 6: 30, 7: 31, 8: 31,
    9: 30, 10: 31, 11: 30, 12: 31
}

try:
    month_num = int(input("Enter month number (1-12): ").strip())
except ValueError:
    print("Invalid input. Please enter an integer between 1 and 12.")
else:
    if month_num < 1 or month_num > 12:
        print("Invalid month number. Please enter a value from 1 to 12.")
    else:
        if month_num == 2:
            leap = input("Is it a leap year? (y/n): ").strip().lower()
            days = 29 if leap in ("y", "yes") else 28
        else:
            days = months[month_num]
        print(f"Month {month_num} has {days} days.")
