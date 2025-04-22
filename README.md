# AI_Web_Summarizer

## Overview

The Smart Web Summarizer is a web application built with Streamlit that allows users to input a webpage URL and receive a concise, AI-generated summary of the main content. It includes a fallback summarization mechanism to handle API unavailability, ensuring a seamless user experience.

## Features

- Accepts any webpage URL as input.
- Fetches and analyzes the content of the provided URL.
- Extracts key information from the webpage.
- Generates a concise summary using an AI model or a fallback method.
- Cleans up templating artifacts (e.g., `{{ variable }}`) from the output.

## Prerequisites

- Python 3.12 or later
- Required Python packages:
  - `streamlit`
  - `requests`
  - `beautifulsoup4`
  - `nltk`

## Installation

1. Clone the repository or download the files (`app.py` and `ai_model.py`).

2. Navigate to the project directory in your terminal.

3. Install the required packages:

   ```bash
   pip install streamlit requests beautifulsoup4 nltk
   ```

4. Run the application for the first time to download NLTK data:

   ```bash
   streamlit run app.py
   ```

   - Note: The NLTK `punkt` data will download automatically on the first run.

## Configuration

- Open `ai_model.py` and replace `your_hf_api_key_here` with your Hugging Face API key.
- The default API URL uses `distilbert-base-uncased`. For better summarization, consider using `facebook/bart-large-cnn` (if supported) and update `API_URL` accordingly.

## Usage

1. Run the application:

   ```bash
   streamlit run app.py
   ```

2. Open your web browser and go to the provided local URL (e.g., `http://localhost:8501`).

3. Enter a webpage URL in the text input field.

4. Click "Generate Summary" to fetch and summarize the content.

5. View the summary in the expandable section.


## MODEL USED

## Model Name: facebook/bart-large-cnn
Purpose: Text summarization
Size: Approximately 1.6GB
API URL: https://api-inference.huggingface.co/models/facebook/bart-large-cnn
Source: Developed by Facebook AI, trained on the CNN/Daily Mail dataset.
