from pprint import pprint
import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
from scrapers.check_word import contains_any_word, contains_any_word_reg


def scrape_habr(logger):
    session = requests.Session()
    url = "https://habr.com/ru/articles/"
    headers = Headers(browser='chrome', os='win').generate()
    key_words = ['дизайн', 'it', 'web', 'python']
    logger.info(f"Начинаем скрапинг {url}")

    try:
        response = session.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, features='lxml')
        articles_list = soup.select('article.tm-articles-list__item')
        parsed_data = []
        for article in articles_list:
            article_link = 'https://habr.com' + article.select_one('a.tm-title__link')['href']
            article_title = article.select_one('h2').text.strip()
            article_time = article.select_one('time')['datetime']
            if contains_any_word_reg(article_title.lower(), key_words):
                parsed_data.append({
                    'date': article_time,
                    'title': article_title,
                    'link': article_link,
                })
        return parsed_data
    except requests.exceptions.RequestException as e:
        logger.error(f'Ошибка при скрапинге {url}: {e}', exc_info=True)
        return False