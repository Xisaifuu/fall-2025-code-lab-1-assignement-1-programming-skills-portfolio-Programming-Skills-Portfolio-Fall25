names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
target = "Sam"

if target in names:
    print(f"Found {target} at index {names.index(target)}.")
else:
    print(f"{target} not found in the list.")