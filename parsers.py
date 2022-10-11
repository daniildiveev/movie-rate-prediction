from typing import List, Union, Tuple
from time import sleep
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

def get_headers() -> 'Options':
    user_agent = UserAgent().random
    options = Options()
    options.add_argument(f"user-agent={user_agent}")
    options.add_argument("window-size=1200,800")

    print(user_agent)

    return options


def parse_links(url:str, 
                time_to_load_url:Union[float, int]=3.,
                cooldown:Union[float, int]=4.) -> List[str]:
    options = get_headers()

    with webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options) as driver:
        driver.get(url)

        sleep(time_to_load_url)
        
        links = driver.find_elements(By.CLASS_NAME, 'base-movie-main-info_link__YwtP1')
        links = [link.get_property("href") for link in links]

        sleep(cooldown)

    return links


def parse_data(urls:List[str], 
               time_to_load_url:Union[float, int]=3.,
               cooldown:Union[float, int]=4.) -> Tuple[List[str], List[float], List[List[str]]]:
    descriptions, rates, genres_list = [], [], []
    options = get_headers()

    GENRES_XPATHS = ('//*[@id="__next"]/div[2]/div[2]/div[1]/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div[3]/div[2]/div',
                    '//*[@id="__next"]/div[2]/div[2]/div[2]/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div[3]/div[2]/div',
                    '//*[@id="__next"]/div[2]/div[2]/div[1]/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div[4]/div[2]/div')

    with webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options) as driver:

        for url in tqdm(urls):
            driver.get(url)

            sleep(time_to_load_url)

            desc = driver.find_elements(By.CLASS_NAME, 'styles_paragraph__wEGPz')[0].text
            rate = driver.find_elements(By.CLASS_NAME, 'film-rating-value')[0].text

            genres = []

            for xpath in GENRES_XPATHS:
                genres += driver.find_elements(By.XPATH, xpath)

            genres = [el.text for el in genres]
            print(genres)

            descriptions.append(desc)
            genres_list.append(genres)
            rates.append(float(rate))

            sleep(cooldown)
    
    return descriptions, rates, genres_list