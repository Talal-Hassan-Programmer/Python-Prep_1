# Read From File

Count_cat = {}

with open('C:/Users/USER/Desktop/Python Prep/Python-Prep_1/#1 from practicepython.org/#22 Read From FilE/IMAGES.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if line:  # Check if the line is not empty
            parts = line.split('/')
            if len(parts) > 2:
                category = parts[2]
                if category in Count_cat:
                    Count_cat[category] += 1
                else:
                    Count_cat[category] = 1


# Print the count of each category
for category, count in Count_cat.items():
    print(f"{category}: {count}")