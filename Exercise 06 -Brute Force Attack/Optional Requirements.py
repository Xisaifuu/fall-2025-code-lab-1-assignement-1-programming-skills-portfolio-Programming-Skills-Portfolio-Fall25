correct_password = "12345"
max_attempts = 5
attempt = 0

while attempt < max_attempts:
    entered = input("Enter password: ").strip()
    attempt += 1
    if entered == correct_password:
        print("Access granted. Correct password entered.")
        break
    remaining = max_attempts - attempt
    if remaining > 0:
        print(f"Incorrect password. {remaining} attempt(s) remaining.")
    else:
        print("Maximum attempts reached. Authorities have been alerted.")