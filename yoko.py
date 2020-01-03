import requests
from bs4 import BeautifulSoup

URL = 'https://www.y-yokohama.com/release/'
# https://www.y-yokohama.com/release/?sp=2400&lang=ja

def last_page():
    num = 0
    last_page = 0
    print('Trying find last page number..')
    while(1):
        results = requests.get(f'{URL}?sp={num}&lang=ja')
        soup = BeautifulSoup(results.content,'html.parser')
        next_button_section = soup.find('div',class_='sec-contents--lv3')
        next_button = next_button_section.find_all('a')
        if (num != 0 and len(next_button) == 1):
            break
        else:
            num +=20
    last_page = num
    print(f'last page number is {last_page}')
    return last_page

def get_article_info(html):
    cate_tr = html.find('span', class_='tr')
    cate_ms = html.find('span', class_='ms')
    cate = (cate_tr or cate_ms)
    # if cate_tr != None or cate_ms != None:
    if cate != None:
        cate = cate.get_text(strip=True)
        date = html.find('dt',class_='md-head').get_text(strip=True)
        title = html.find('p',class_='md-ttl').get_text(strip=True)
        link = html.find('a').get('href').strip('/')
        return{
            'Category' : cate,
            'Upload date' : date,
            'Title' : title,
            'link' : f'https://{link}'
        }
    else:
        return None

def get_articles(last_page):
    articles = []
    for num in range(0,last_page+20,20):
        print(f'Scrapping {int((num/20)+1)} page...')
        results = requests.get(f'{URL}?sp={num}&lang=ja')
        soup = BeautifulSoup(results.content,'html.parser')
        article_raw = soup.find_all('li', class_='li-06-inr')
        for article in article_raw:
            article_content = get_article_info(article)
            # it needs exclude None data
            if article_content != None:
                articles.append(article_content)
            else:
                None
    return articles

def articles():
    print('Scrapping Start : YOKOHAMA COMPANY')
    last_page_num = last_page()
    articles_results = get_articles(last_page_num)
    return articles_results


