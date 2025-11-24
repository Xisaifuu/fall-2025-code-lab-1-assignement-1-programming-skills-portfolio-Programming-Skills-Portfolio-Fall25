def is_even(n: int) -> str:
    return f"{n} is even." if n % 2 == 0 else f"{n} is odd."

def main():
    while True:
        user_input = input("Enter an integer: ").strip()
        try:
            number = int(user_input)
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    result = is_even(number)
    print(result)

if __name__ == "__main__":
    main()