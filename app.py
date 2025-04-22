import streamlit as st
import requests
from bs4 import BeautifulSoup

st.set_page_config(page_title="Smart Web Summarizer", layout="wide")

st.title("Smart Web Summarizer")
st.markdown("Enter any webpage URL to get a clean, AI-generated summary from the main content.")

url = st.text_input("Enter Website URL")

if st.button("Generate Summary"):
    if url:
        st.info("Fetching and summarizing content...")
        try:
            response = requests.get(url, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
            }, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            text = ' '.join(p.get_text(strip=True) for p in soup.find_all('p') if p.get_text(strip=True))
            
            if not text or len(text) < 100:
                st.error("Could not extract meaningful content. Please try another link.")
            else:
                from ai_model import summarize_text
                summary = summarize_text(text[:3000])
                st.success("Summary generated!")
                with st.expander("Summary Output", expanded=True):
                    for sentence in summary.split('. '):
                        st.markdown(f"- {sentence.strip()}.")
        except requests.RequestException as e:
            st.error("Could not fetch the webpage. Please try another link.")
    else:
        st.warning("Please enter a valid URL to proceed.")