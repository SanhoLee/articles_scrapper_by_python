import csv


def save_to_csv(articles):
    f = open('data.csv', 'w')
    datafile = csv.writer(f)
    datafile.writerow(['Category','Upload date','Title','link'])
    for article in articles:
        datafile.writerow(list(article.values()))
    return
