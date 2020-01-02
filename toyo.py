import requests
from bs4 import BeautifulSoup

URL = 'https://www.toyotires.co.jp'


def last_page(year_number):
    # get last page for single year range.
    # it finds page number, untill next page button is disappeared..
    i = 0
    while(1):
        results = requests.get(f'{URL}/press/{year_number}?page={i}')
        soup = BeautifulSoup(results.text, 'html.parser')
        next_button = soup.find('a', {'class': 'button'})
        if next_button == None:
            last_page = i
            break
        else:
            i += 1
    return last_page


def get_year_list():
    years = []
    results = requests.get(f'{URL}/press/2019')
    soup = BeautifulSoup(results.text, 'html.parser')
    year_lump_data = soup.find(
        'div', {'id': 'block-views-block-press-year-list-block-1'})
    list_year = year_lump_data.find_all('a')
    for year in list_year:
        year_num = year.get('href')
        year_num = year_num.split('/')[-1]
        years.append(int(year_num))
    # returns years that type of list(int)
    return years


def get_article_info(html):
    cate = html.find('span', {'class': 'label'}).get_text(strip=True)
    date = html.find('div', {'class': 'date-cell'}).get_text(strip=True)
    title = html.find('div', {'class': 'ttl-cell'}).find('a').get_text(strip=True)
    link = html.find('div', {'class': 'ttl-cell'}).find('a').get('href')
    return {
        'Category': cate,
        'Upload date': date,
        'Title': title,
        'link': f'{URL}{link}'
    }


# def get_articles_info(last_page, list_of_years):

def get_articles(list_of_years):
    articles = []
    for year in list_of_years:
        for page in range(last_page(year)):
            print(f'Scraping {year} year, {page+1} page..')
            results = requests.get(f'{URL}/press/{year}?page={page}')
            soup = BeautifulSoup(results.text, 'html.parser')
            articles_raw = soup.find_all('div', {'class': 'con'})
            for article in articles_raw:
                article_content = get_article_info(article)
                articles.append(article_content)
    return articles

def articles():
    years = get_year_list()
    articles_results = get_articles(years)
    print(f'Number of TOYO Articles : {len(articles_results)}')
    return articles_results