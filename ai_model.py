API_KEY = "Your-API-key"
API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased"

import requests
from nltk.tokenize import sent_tokenize
import nltk
import re

nltk.download('punkt')

def clean_text(text):
    """Remove template syntax and unrendered variables."""
    text = re.sub(r'{{.*?}}', '', text)
    text = re.sub(r'\| currency:".*?":\d+', '', text)
    text = ' '.join(text.split())
    return text

def summarize_text(text):
    if not text or len(text) < 100:
        return "No meaningful content found."

    cleaned_text = clean_text(text)

    payload = {"inputs": f"Summarize the following text concisely: \n{cleaned_text}"}
    headers = {"Authorization": f"Bearer {API_KEY}"}
    
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=10)
        if response.status_code == 200:
            result = response.json()
            if isinstance(result, dict) and 'summary' in result[0]:
                return clean_text(result[0]['summary'])
        elif response.status_code == 503:
            st.warning("API service unavailable. Using fallback summarization.")
    except requests.RequestException:
        pass
    
    sentences = sent_tokenize(cleaned_text)
    if len(sentences) > 3:
        return '. '.join(sentences[:3]) + '.'
    return '. '.join(sentences) + '.'