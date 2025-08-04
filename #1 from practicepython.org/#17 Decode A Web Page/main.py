# Decode A Web Page
#This program gets all news headlines from a  New York Times homepage and prints them out.

#import 
import requests
from bs4 import BeautifulSoup

# Get the HTML content of the New York Times homepage
url = 'https://www.nytimes.com/'
response = requests.get(url)

# Check if the request was successful
print("Status code:", response.status_code)

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



# Print the total number of headlines found
print("Total headlines found:", len(headlines))

