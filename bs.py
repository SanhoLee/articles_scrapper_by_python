import requests
from bs4 import BeautifulSoup

URL = 'https://www.bridgestone.co.jp/corporate/news/'


## 원하는 곳의 클래스 이름이 안잡힌다.....일단보류.
def get_year_list():
    years = []
    results = requests.get(URL)
    soup = BeautifulSoup(results.content, 'html.parser')
    year_lump_data = soup.find_all('ul')
    print(year_lump_data)
# def articles():


def get_articles(list_of_years):
    results = requests.get(URL)
    soup = BeautifulSoup(results.content, 'html.parser')
    year_lump_data = soup.find_all('dl', {'class': 'dl_news01'})
    # print(year_lump_data[0])


get_year_list()