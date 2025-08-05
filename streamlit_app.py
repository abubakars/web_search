import streamlit as st
import requests
from bs4 import BeautifulSoup

st.set_page_config(page_title="Web Page Scraper", layout="wide")

st.title("🌐 Web Page Scraper")
st.write("Enter a URL to scrape its main content.")

# Input URL
url = st.text_input("Enter a website URL:", placeholder="https://example.com")

if url:
    try:
        # Fetch content
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract title
        page_title = soup.title.string if soup.title else "No title found"
        st.subheader(f"Page Title: {page_title}")

        # Extract paragraphs
        paragraphs = soup.find_all("p")
        if paragraphs:
            st.markdown("### Page Content:")
            for para in paragraphs[:30]:  # Show only first 30 paragraphs
                text = para.get_text(strip=True)
                if text:
                    st.write(text)
        else:
            st.warning("No paragraph content found on this page.")

    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching URL: {e}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
