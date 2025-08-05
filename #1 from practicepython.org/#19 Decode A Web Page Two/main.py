import requests
from bs4 import BeautifulSoup

url = "https://www.theguardian.com/world/2025/aug/04/gaza-starvation-un-expert-michael-fakhri"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
print("Status code:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

container = soup.find("div", class_="article-body-viewer-selector")
if container:
    paragraphs = container.find_all("p", class_="dcr-16w5gq9")
    for para in paragraphs:
        print(para.get_text(strip=True), end="\n\n")
    print("✅ Total paragraphs:", len(paragraphs))

else:
    print("❌ Article container not found. HTML structure may have changed.")
