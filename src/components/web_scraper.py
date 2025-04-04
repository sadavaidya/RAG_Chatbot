# import requests
# from bs4 import BeautifulSoup

# def scrape_news(urls):
#     all_news_articles = []

#     for url in urls:
#         response = requests.get(url)
#         print(f"Fetching {url}, Status code: {response.status_code}")

#         if response.status_code != 200:
#             print(f"Failed to fetch {url}")
#             continue

#         soup = BeautifulSoup(response.content, 'html.parser')
#         print(soup.prettify())  # To inspect the structure

#         news_articles = []

#         # Adjust selectors based on the structure of the target news website
#         for article in soup.find_all('article'):  # Modify based on website structure
#             headline = article.find('h2') or article.find('h3')  # Headline in h2 or h3 tag
#             summary = article.find('p')  # Description or summary in p tag
#             print(headline)
#             if headline and summary:
#                 print(f"Found article: {headline.text.strip()} - {summary.text.strip()}")
#                 news_articles.append(f"{headline.text.strip()}: {summary.text.strip()}")

#         all_news_articles.extend(news_articles)

#     return all_news_articles


from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
from newspaper import Article

def get_bbc_article_links(base_url="https://www.bbc.co.uk/news"):
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    links = set()
    for a in soup.find_all('a', href=True):
        href = a['href']
        if href.startswith('/news') and not href.endswith('live'):  # Avoid live updates
            full_url = urljoin(base_url, href)
            links.add(full_url)

    return list(links)[:10]  # Limit to 10 for testing

def scrape_articles(urls):
    articles = []
    for url in urls:
        try:
            article = Article(url)
            article.download()
            article.parse()
            articles.append(f"{article.title}: {article.text}")
        except Exception as e:
            print(f"Error scraping {url}: {e}")
    return articles

# Example usage
urls = get_bbc_article_links()
news_data = scrape_articles(urls)
print(news_data)
print(urls)