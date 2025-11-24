correct_password = "12345"
entered = ""

while entered != correct_password:
    entered = input("Enter password: ").strip()
    if entered != correct_password:
        print("Incorrect password. Try again.")

print("Access granted. Correct password entered.")