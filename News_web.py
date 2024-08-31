import streamlit as st
import requests

API_KEY = '2c01d02d6a41451f8dc606476275b7d0'

URL =('https://newsapi.org/v2/top-headlines?')

def get_article_by_category(category):
    query_paramneters = {
        "category": category,
        "pageSize": 100,
        "sortBy": "top",
        "country": "in",
        "apiKey": API_KEY
        
    }
    return _get_articles(query_paramneters)


def _get_articles(params):
    response = requests.get(URL, params=params)
    
    articles = response.json()['articles']
    
    results = []
    
    for article in articles:
        results.append({"title": article["title"],"description": article['description'], "url": article["url"]})
    
    return results
        
        
    


if __name__=='__main__':
    
    st.set_page_config(
        page_title="Latest News App🔥",
        page_icon="📰",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # category selection
    source = st.sidebar.selectbox(
    'What kind of news would you like?',
    ( 'General', 'Business','Entertainment', 'Health', 'Science', 'Sports', 'Technology')
    )   
   
    
    st.title(f"🔥🔥Latest {source} News!! ")

    results = get_article_by_category(source)       
    
    #Displays news of select category    
    for result in results:
        with st.container(border=True):
            st.subheader(result['title'])
            if result['description']: st.write(result['description'])
            st.write("Check the whole story [link](%s)" %result['url'])
    
