names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Optional: allow user input; press Enter to search for "Sam"
target = input("Enter name to search (press Enter to search for 'Sam'): ").strip()
if not target:
    target = "Sam"

# Case-insensitive search
index = next((i for i, n in enumerate(names) if n.lower() == target.lower()), None)

if index is not None:
    print(f"Found {target} at index {index}.")
else:
    print(f"{target} not found in the list.")