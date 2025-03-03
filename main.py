import json
from scrapers import habr
from utils.logger import setup_logger
from time import sleep


def main():
    logger = setup_logger()
    logger.info("Запуск скрапинга")
    try:
        data = habr.scrape_habr(logger)
        logger.info(f"Успешно собраны данные: {len(data)} элементов")

        with open("data/scraped_data.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        logger.info("Данные сохранены в data/scraped_data.json")

    except Exception as e:
        logger.error(f"Произошла ошибка: {e}", exc_info=True)

    logger.info("Скрапинг завершен")


if __name__ == "__main__":
    main()