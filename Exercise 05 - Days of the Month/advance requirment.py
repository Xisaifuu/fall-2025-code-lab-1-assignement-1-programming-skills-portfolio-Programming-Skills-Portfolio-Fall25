months = {
    1: 31, 2: 28, 3: 31, 4: 30,
    5: 31, 6: 30, 7: 31, 8: 31,
    9: 30, 10: 31, 11: 30, 12: 31
}

def is_leap_year(year: int) -> bool:
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

try:
    month_num = int(input("Enter month number (1-12): ").strip())
except ValueError:
    print("Invalid input. Please enter an integer between 1 and 12.")
else:
    if month_num < 1 or month_num > 12:
        print("Invalid month number. Please enter a value from 1 to 12.")
    else:
        if month_num == 2:
            # Ask for year and compute leap year accurately
            while True:
                year_input = input("Enter the year (e.g., 2024): ").strip()
                try:
                    year = int(year_input)
                    break
                except ValueError:
                    print("Invalid year. Please enter a numeric year (e.g., 2024).")
            days = 29 if is_leap_year(year) else 28
        else:
            days = months[month_num]
        print(f"Month {month_num} has {days} days.")