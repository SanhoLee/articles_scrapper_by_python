import csv
from toyo import articles as toyo_articles
from bs import articles as bs_articles
from save import save_to_csv

toyo = toyo_articles()
# bs = bs_articles()
# articles = toyo_articles + bs_articles


save_to_csv(toyo)