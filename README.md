# Streamlit News Aggregator

A simple news aggregator app built with Streamlit that fetches the latest news headlines by category using the NewsAPI.

## Features

- **Category-Based News:** Choose from categories like General, Business, Entertainment, Health, Science, Sports, and Technology.
- **Top Headlines:** Displays the latest top headlines from India.
- **Interactive UI:** Modern interface with easy navigation via Streamlit's sidebar.

## Installation

1. Clone the repository and navigate to the project directory.
2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
3. Add your [NewsAPI](https://newsapi.org/) API key to the script by replacing the placeholder `API_KEY` with your own key.

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```
2. Select a news category from the sidebar.
3. View the latest headlines along with descriptions and direct links to the full articles.

## Code Overview

- **get_article_by_category(category):** Fetches articles based on the selected category.
- **_get_articles(params):** Helper function to call the NewsAPI and process the response.

## Files

- `app.py`: The main script containing the Streamlit app.
- `requirements.txt`: A file listing the required Python packages.

## Credits

Developed by Ankit kujur.
