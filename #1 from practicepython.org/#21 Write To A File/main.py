# Write to a File

#import 
import requests
from bs4 import BeautifulSoup

# Get the HTML content of the New York Times homepage
url = 'https://www.nytimes.com/'
response = requests.get(url)

# Check if the request was successful
print("Status code:", response.status_code)

n = input("Enter the name of File to save headlines: ")

soup = BeautifulSoup(response.text, 'html.parser')

# Find all the headlines in the HTML
headlines = soup.find_all("p", class_="indicate-hover")

# Print each headline
# Print each headline with its link
for i, headline in enumerate(headlines):
    text = headline.get_text(strip=True)
    link_tag = headline.find_parent("a")  # go up to the <a> tag
    link = link_tag["href"] if link_tag else "No link found"

    print(f"{i + 1}. {text}")
    print(f"    Link: {link} \n")

    # Save each headline to a file (IT SAVES THE FILE IN THE SAME DIRECTORY AS THE SCRIPT)
    with open(f"{n}.txt", "a") as file:
        file.write(f"{i + 1}. {text}\n")
        file.write(f"    Link: {link}\n\n")

    



# Print the total number of headlines found
print("Total headlines found:", len(headlines))
