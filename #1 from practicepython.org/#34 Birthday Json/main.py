import json


# Function to add a new birthday entry
def add_birthday():
    x = input("Enter the name: ")
    y = input("Enter the date (YYYY-MM-DD): ")
    

    date = {
        x : y
    }


    try:
        with open('C:/Users/USER/Desktop/Python Prep/Python-Prep_1/#1 from practicepython.org/#34 Birthday Json/Birth.json', 'r+') as file:
            birthdays = json.load(file) 
            birthdays[x] = y
            file.seek(0)
            json.dump(birthdays, file, indent=4)
            file.truncate()


    except FileNotFoundError:
        with open('C:/Users/USER/Desktop/Python Prep/Python-Prep_1/#1 from practicepython.org/#34 Birthday Json/Birth.json', 'w') as file:
            json.dump(date, file)


while True:
    us = input("Do you want to Add or Get a birthday? (Add/Get): ").strip().lower()
    if us == 'add':
        add_birthday()
    elif us == 'get':
        name = input("Please enter the name: ")
        try:
            with open('C:/Users/USER/Desktop/Python Prep/Python-Prep_1/#1 from practicepython.org/#34 Birthday Json/Birth.json', 'r') as file:
                data = json.load(file)
                if name in data:
                    print(f"{name}'s birthday is on {data[name]}")
                else:
                    print(f"No birthday found for {name}.")

        except FileNotFoundError:
            print("No birthday data found. Please add a birthday first.")