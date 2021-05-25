import requests

from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

years = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']
months = ['leden', 'unor', 'brezen', 'duben', 'kveten', 'cerven', 'cervenec', 'srpen', 'zari', 'rijen', 'listopad', 'prosinec']

for i in range(2,len(years)):
    # for j in range(len(months)):
    URL = 'https://www.e-pocasi.cz/archiv-pocasi/' + years[i] + '/' + months[4]

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    for img in soup.find_all('img'):
        link = str(img.get('src'))
        if 'chart.google' in link:
            response = requests.get(link).content
            with open('graf_' + years[i] + '_' + months[4] + '.jpg', 'wb') as graph:
                graph.write(response)