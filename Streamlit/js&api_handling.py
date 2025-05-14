import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com/s?k=smartphones"
headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9"
}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

titles = soup.select("h2 span")
print(f"🧾 Titles found in raw HTML: {len(titles)}")
for t in titles[:3]:
    print(" -", t.get_text())



# URL from the request
url = "https://www.amazon.com/hz/rhf?currentPageType=Search&currentSubPageType=List&excludeAsin=&fieldKeywords=&k=smartphones&keywords=&search=&auditEnabled=&previewCampaigns=&forceWidgets=&searchAlias=&cardJSPresent=true"

# Set the headers from the browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) Gecko/20100101 Firefox/138.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "keep-alive",
    "Referer": "https://www.amazon.com/s?k=smartphones",
    "Cookie": "aws-ubid-main=958-4014882-0730417;"
}

response = requests.get(url, headers=headers)

# Check if the response is in JSON format
if response.status_code == 200 and response.headers["Content-Type"] == "application/json;charset=UTF-8":
    print("API Response:")
    print(response.json())  # This prints the JSON response returned by Amazon
else:
    print("No API response or failed request.")




import requests

# Common places for RSS feeds
rss_urls = [
    "https://www.aboutamazon.com/about-amazon-rss.rss",  # Placeholder for Amazon RSS
]

for rss_url in rss_urls:
    response = requests.get(rss_url)
    if response.headers["Content-Type"].startswith("application/xml"):
        print(f"RSS Feed found at {rss_url}")
        print(response.text)  # Or parse with an XML parser like lxml
    else:
        print(f"No RSS feed at {rss_url}")
