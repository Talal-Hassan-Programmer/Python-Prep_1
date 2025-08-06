# Birthday Dictionaries


Birthday_dict = {
    "Alice": "1990-01-01",
    "Bob": "1992-02-02",
    "Charlie": "1993-03-03"
    }

while True:
    user_input = input("Add or Get or Remove a birthday? (add/get): ").strip().lower()


    if user_input == "add":
        name = input("Enter the name: ").strip().lower()
        date = input("Enter the birthday (YYYY-MM-DD): ").strip()
        
        if name in Birthday_dict:
            print(f"{name} already exists in the dictionary.")
        else:
            Birthday_dict[name] = date
            print(f"Added {name} with birthday {date}.")    


    elif user_input == "get":
        name = input("Enter the name: ").strip().lower()
        if name in Birthday_dict:
            print(f"{name}'s birthday is {Birthday_dict[name]}.")
        else:
            print( f"{name} not found in the dictionary.")
    


    elif user_input == "remove":
        name = input("Enter the name to remove: ").strip().lower()
        if name in Birthday_dict:
            del Birthday_dict[name]
            print(f"Removed {name} from the dictionary.")
        else:
            print(f"{name} not found in the dictionary.")