# Intelligent Web Crawler & Analyzer

## 📝 Project Overview

A Streamlit-based dashboard that simulates intelligent web crawling on Amazon to assess crawlability, extract top-rated product data, analyze categories, and test JavaScript/API scraping logic.

---

## 🚀 Features

- **Crawlability score based on robots.txt**
- **Top product ratings and category insights**
- **Visual sitemap for crawl logic**
- **JS/API/RSS feed scraping demos**
- **Recommendations for scraping tools**

---

## 🖼️ Screenshots (Optional)

*Include screenshots or GIFs of your dashboard in action here.*

---

## ⚙️ Installation Instructions

```bash
# Clone the repo
git clone https://github.com/yourusername/intelligent-crawler.git
cd intelligent-crawler

# Create virtual environment (optional but recommended)
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Running the App

```bash
streamlit run dashboard.py
```

---

## ☁️ Deployment

### Streamlit Cloud

1. Push your repo to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your GitHub repo
4. Set the main file to `Dashboard.py`
5. Deploy 🚀

### Local Server

Just run:

```bash
streamlit run dashboard.py
```

---

## 📊 Data

- **tech_products.csv**: extracted product data from Amazon (scraped using ParseHub or manually)

---

## 📌 Notes

- Amazon is JS-heavy; scraping with BeautifulSoup may not reveal all data.
- Use Playwright or Selenium for full content scraping.

---

## ✅ requirements.txt

Make sure you include this in your project:

```
streamlit
pandas
matplotlib
graphviz
beautifulsoup4
requests
```

Generate it with:

```bash
pip freeze > requirements.txt
```

---

## 🔹 Deploy

### Streamlit Cloud

1. Push your project to GitHub.
2. Go to Streamlit Cloud.
3. Click “New App”, select your repo and branch.
4. Set the entry point to `dashboard.py`.
5. Click Deploy.

### Local Deployment

Just run:

```bash
streamlit run dashboard.py
```