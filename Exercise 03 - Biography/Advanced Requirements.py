# Prompt the user for name and hometown (input() accepts spaces)
name = input("Enter your full name: ").strip()
hometown = input("Enter your hometown: ").strip()

# Validate age input and convert to int
while True:
    age_input = input("Enter your age (integer): ").strip()
    try:
        age = int(age_input)
        break
    except ValueError:
        print("Invalid age. Please enter an integer value (e.g., 19).")

person = {
    "name": name,
    "hometown": hometown,
    "age": age
}

# Print values on separate lines using a single print() call
print(person["name"], person["hometown"], person["age"], sep="\n")