import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
from scrapers.check_word import contains_any_word, contains_any_word_reg



def scrape_toscrape(logger):

    url = "https://habr.com/ru/articles/"
    headers = Headers(browser='chrome', os='win').generate()
    key_words = ['дизайн', 'it', 'web', 'python']
    logger.info(f"Начинаем скрапинг {url}")


    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, features='lxml')
        articles_list = soup.select('article.tm-articles-list__item')
        parsed_data = []
        for article in articles_list:
            article_link = 'https://habr.com' + article.select_one('a.tm-title__link')['href']
            response_article = requests.get(article_link )
            soup = BeautifulSoup(response_article.text, features='lxml')
            article_title = soup.select_one('h1').text.strip()
            article_time = soup.select_one('time')['datetime']
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




