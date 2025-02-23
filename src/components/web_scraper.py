import requests
from bs4 import BeautifulSoup

def scrape_news(urls):
    all_news_articles = []

    for url in urls:
        response = requests.get(url)
        print(f"Fetching {url}, Status code: {response.status_code}")

        if response.status_code != 200:
            print(f"Failed to fetch {url}")
            continue

        soup = BeautifulSoup(response.content, 'html.parser')
        print(soup.prettify())  # To inspect the structure

        news_articles = []

        # Adjust selectors based on the structure of the target news website
        for article in soup.find_all('article'):  # Modify based on website structure
            headline = article.find('h2') or article.find('h3')  # Headline in h2 or h3 tag
            summary = article.find('p')  # Description or summary in p tag

            if headline and summary:
                print(f"Found article: {headline.text.strip()} - {summary.text.strip()}")
                news_articles.append(f"{headline.text.strip()}: {summary.text.strip()}")

        all_news_articles.extend(news_articles)

    return all_news_articles
