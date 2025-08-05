import streamlit as st
import requests
from bs4 import BeautifulSoup
import re

st.set_page_config(page_title="Web Scraper App", layout="wide")

st.title("🔍 Simple Web Scraper with Streamlit")

# --- Input URL ---
url = st.text_input("Enter a webpage URL:", "https://www.example.com")

if st.button("Scrape Webpage"):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Parse HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Remove script and style tags
        for tag in soup(["script", "style", "noscript"]):
            tag.decompose()

        # Extract text and clean
        raw_text = soup.get_text()
        cleaned_text = re.sub(r'\s+', ' ', raw_text).strip()

        st.success("✅ Scraping complete!")
        st.subheader("📄 Scraped Text:")
        st.text_area("Webpage Content", cleaned_text, height=400)

        # --- Download Button ---
        st.download_button("💾 Download as TXT", data=cleaned_text, file_name="scraped_content.txt")

    except requests.exceptions.RequestException as e:
        st.error(f"❌ Error: {e}")
