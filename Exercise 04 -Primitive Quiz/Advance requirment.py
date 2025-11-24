# ...code...
questions = {
    "France": "Paris",
    "Spain": "Madrid",
    "Germany": "Berlin",
    "Italy": "Rome",
    "United Kingdom": "London",
    "Portugal": "Lisbon",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Sweden": "Stockholm",
    "Norway": "Oslo"
}

score = 0
for country, capital in questions.items():
    answer = input(f"What is the capital of {country}? ").strip().lower()
    if answer == capital.lower():
        print("Correct —", capital)
        score += 1
    else:
        print("Wrong — the correct answer is", capital)

print(f"\nYou got {score} out of {len(questions)} correct.")