import streamlit as st
import requests
from bs4 import BeautifulSoup

st.set_page_config(page_title="Web Page Scraper", layout="wide")

st.title("🌐 Web Page Scraper")

# Input section
url = st.text_input("Enter the URL of the webpage you want to scrape:")

tag = st.text_input("Optional: HTML tag to extract (e.g., p, h1, h2, div)", "")

if st.button("Scrape Now"):
    if not url.startswith("http"):
        st.error("Please enter a valid URL starting with http or https")
    else:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")

            # Get title
            title = soup.title.string if soup.title else "No title found"
            st.subheader("🔖 Page Title:")
            st.write(title)

            # Extract specific tag or all visible text
            if tag:
                elements = soup.find_all(tag)
                st.subheader(f"📌 All <{tag}> tags:")
                for i, elem in enumerate(elements):
                    if elem.text.strip():
                        st.markdown(f"**{i+1}.** {elem.text.strip()}")
            else:
                # Extract visible text
                for script in soup(["script", "style"]):
                    script.decompose()
                text = soup.get_text()
                lines = [line.strip() for line in text.splitlines()]
                text_output = "\n".join(line for line in lines if line)
                st.subheader("📄 Extracted Page Text:")
                st.text_area("Text Content", value=text_output, height=400)

        except Exception as e:
            st.error(f"Failed to scrape the webpage: {e}")
