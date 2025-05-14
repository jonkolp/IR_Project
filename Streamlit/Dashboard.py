import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from graphviz import Digraph
import requests
from bs4 import BeautifulSoup

# Import your Crawlability class
from crawl import CrawlabilityChecker  # Adjust the import path if needed

# Set page config FIRST
st.set_page_config(page_title="Amazon Crawl Report", layout="wide")

# Load extracted data
@st.cache_data
def load_data():
    df = pd.read_csv(r"c:\Users\youss_kk115ax\Desktop\IR\Project\Streamlit\tech_products.csv")
    return df

df = load_data()

# Title
st.title("🕷️ Intelligent Web Crawler & Analyzer Dashboard")

# Section 1: Crawlability Score (Based on robots.txt)
st.header("📊 Crawlability Score")
urls_tested = [
    'https://www.amazon.com/dp/B09G3HRMVP',
    'https://www.amazon.com/wishlist/universal',
    'https://www.amazon.com/gp/customer-reviews/write-a-review.html',
    'https://www.amazon.com/gp/help/customer/display.html',
    'https://www.amazon.com/gp/cart/view.html'
]

# Instantiate your Crawlability checker
crawl_checker = CrawlabilityChecker()

# Test each URL using can_crawl
crawl_results = [crawl_checker.can_crawl(url) for url in urls_tested]
score = int((sum(crawl_results) / len(crawl_results)) * 100)

col1, col2 = st.columns(2)
col1.metric("Score", f"{score}%", delta="+10% from last run")
col2.write("Checked URLs:")
for url, result in zip(urls_tested, crawl_results):
    col2.markdown(f"- {'✅' if result else '❌'} {url}")

# Section 2: Top Extracted Data
st.header("📦 Top Rated Products")

# Show top 20 products by customer rating
if "customer_ratings" in df.columns:
    # Extract numeric rating from string
    df["numeric_rating"] = df["customer_ratings"].str.extract(r'([0-9.]+)').astype(float)
    top20_df = df.sort_values(by="numeric_rating", ascending=False).head(20)
    st.dataframe(top20_df, use_container_width=True)
else:
    st.warning("No 'customer_ratings' column found in the data.")

# Section 3: Product Category Chart
st.subheader("Product Distribution by Category")
if "category" in df.columns:
    category_counts = df["category"].value_counts()
    st.bar_chart(category_counts)




st.header("🗺️ Visual Sitemap (Amazon Crawl Logic)")

dot = Digraph()

# Define nodes
dot.node("A", "Start")
dot.node("B", "Check robots.txt")
dot.node("C", "Allowed URL?")
dot.node("D", "Scrape Data")
dot.node("E", "Save Results")
dot.node("F", "Blocked – Skip")
dot.node("G", "Next URL")
dot.node("H", "Save to CSV File")

# Define edges
dot.edges(["AB", "BC"])
dot.edge("C", "D", label="Yes")
dot.edge("C", "F", label="No")
dot.edge("D", "E")
dot.edge("E", "G")
dot.edge("F", "G")
dot.edge("G", "C", label="Loop")
dot.edge("E", "H", label="Final Step")

st.graphviz_chart(dot)

st.markdown("This sitemap shows the basic logic followed by the crawler when processing Amazon product pages.")

# Section 5: JS & API Handling Demo
st.header("🧪 JS & API Handling Examples")

# --- Raw HTML Scraping Example ---
st.subheader("Raw HTML Scraping (BeautifulSoup)")
url_html = "https://www.amazon.com/s?k=smartphones"
headers_html = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9"
}
try:
    res = requests.get(url_html, headers=headers_html, timeout=10)
    soup = BeautifulSoup(res.text, 'html.parser')
    titles = soup.select("h2 span")
    st.write(f"🧾 Titles found in raw HTML: {len(titles)}")
    for t in titles[:3]:
        st.write(" -", t.get_text())
except Exception as e:
    st.warning(f"Failed to fetch or parse HTML: {e}")

st.info(
    "⚠️ **Note:** based on the above Results, Amazon is a JavaScript-heavy website. "
    "To get fully rendered content with all products, you often need to use browser automation tools like **Playwright** or **Selenium**. "
    "Requests and BeautifulSoup can only access the initial HTML, not dynamic JS-rendered content."
)
# --- API Endpoint Example ---
st.subheader("API Endpoint Request (XHR/JSON)")
url_api = "https://www.amazon.com/hz/rhf?currentPageType=Search&currentSubPageType=List&excludeAsin=&fieldKeywords=&k=smartphones&keywords=&search=&auditEnabled=&previewCampaigns=&forceWidgets=&searchAlias=&cardJSPresent=true"
headers_api = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:138.0) Gecko/20100101 Firefox/138.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "X-Requested-With": "XMLHttpRequest",
    "Connection": "keep-alive",
    "Referer": "https://www.amazon.com/s?k=smartphones",
    "Cookie": "aws-ubid-main=958-4014882-0730417;"
}
try:
    response = requests.get(url_api, headers=headers_api, timeout=10)
    if response.status_code == 200 and "application/json" in response.headers.get("Content-Type", ""):
        st.success("API JSON response received!")
        st.json(response.json())
    else:
        st.info("No API response or failed request.")
except Exception as e:
    st.warning(f"API request failed: {e}")

# --- RSS Feed Example ---
st.subheader("RSS Feed Check")
rss_urls = [
    "https://www.aboutamazon.com/about-amazon-rss.rss",  # Example RSS feed
]
for rss_url in rss_urls:
    try:
        rss_response = requests.get(rss_url, timeout=10)
        if rss_response.headers.get("Content-Type", "").startswith("application/xml"):
            st.success(f"RSS Feed found at {rss_url}")
            st.code(rss_response.text[:1000] + " ...", language="xml")
        else:
            st.info(f"No RSS feed at {rss_url}")
    except Exception as e:
        st.warning(f"RSS check failed for {rss_url}: {e}")




st.header("🧰 Recommendations for Crawling Tools")
st.markdown("""
- ✅ **Scrapy**: Great for large-scale, structured web scraping.
- ✅ **Selenium / Playwright**: Best for JavaScript-rendered sites.
- ✅ **BeautifulSoup**: Good for quick parsing and cleaning.
- ✅ **ParseHub**: Ideal for visual scraping without writing code.
- 🧪 Combine tools for hybrid scraping where APIs are unavailable.
""")

