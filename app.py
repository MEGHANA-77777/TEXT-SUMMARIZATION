import streamlit as st
import requests

# Set your Cohere API key here
API_KEY = "KGzncCCfHjKlNhAUwedCm7jWsq0i7Evz9hbijD3s"
API_URL = "https://api.cohere.ai/v1/summarize"

# Streamlit app layout
st.title("Text Summarization using Cohere API")
text_input = st.text_area("Enter text for summarization")

if st.button("Summarize"):
    if text_input:
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "text": text_input,
            "summary_length": "short"  # Or specify your own summary length
        }
        response = requests.post(API_URL, json=data, headers=headers)
        
        if response.status_code == 200:
            summary = response.json().get("summary")
            st.write("Summary: ", summary)
        else:
            st.error("Error: Unable to summarize. Check API key or try again later.")
