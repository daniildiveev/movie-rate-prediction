from typing import List, Union, Tuple
from time import sleep
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def parse_links(url:str, 
                time_to_load_url:Union[float, int]=3.) -> List[str]:
    with webdriver.Chrome(ChromeDriverManager().install()) as driver:
        driver.get(url)

        sleep(time_to_load_url)
        
        links = driver.find_elements(By.CLASS_NAME, 'base-movie-main-info_link__YwtP1')
        links = [link.get_property("href") for link in links]

    return links

def parse_data(urls:List[str], 
                                 time_to_load_url:Union[float, int]=3.) -> Tuple[List[str], List[float]]:
    descriptions, rates, genres_list = [], [], []
    
    with webdriver.Chrome(ChromeDriverManager().install()) as driver:

        for url in tqdm(urls):
            driver.get(url)

            sleep(time_to_load_url)

            desc = driver.find_elements(By.CLASS_NAME, 'styles_paragraph__wEGPz')[0].text
            rate = driver.find_elements(By.CLASS_NAME, 'film-rating-value')[0].text
            genres = driver.find_elements(By.CLASS_NAME, 'styles_valueLight__nAaO3')[5]

            genres = genres.replace(",", "").split()
            print(genres)

            descriptions.append(desc)
            genres_list.append(genres)
            rates.append(float(rate))
    
    return descriptions, rates, genres_list
