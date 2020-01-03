import csv
from toyo import articles as toyo_articles
from yoko import articles as yoko_articles
from save import save_to_csv

toyo = toyo_articles()
yoko = yoko_articles()
articles = toyo + yoko


save_to_csv(articles)