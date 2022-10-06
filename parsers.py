from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def parse_links(url):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)

    sleep(3)

    html 



if __name__ == '__main__':
    parse_descriptions("https://www.kinopoisk.ru/lists/movies/country--1/?ss_subscription=ANY")
