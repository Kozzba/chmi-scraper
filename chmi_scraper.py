import requests
import csv
from bs4 import BeautifulSoup

table = []
for i in range(61,120):
    URL = f'https://www.chmi.cz/files/portal/docs/meteo/ok/uzemni_data/uzs{str(i)[-2:]}_6190_cs.html'

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    j = 0
    for row in soup.find_all(class_="portlet-table-body"):
        list = []
        j+=1
        for souhrn_srazek in row.find_all(class_="Number"):
            value = f"{''.join(filter(str.isdigit, str(souhrn_srazek)))}"
            list.append(value)
        if j == 1:
            list.append('S')
        if j == 2:
            list.append('N')
        if j == 3:
            list.append('P')
            j = 0
        if i < 100:
            list.append(f'19{str(i)[-2:]}')
        else:
            list.append(f'20{str(i)[-2:]}')
        try:
            place = row.find(valign="middle").get_text()
        except AttributeError:
            pass
        list.append(place)
        table.append(list)
print(table)

with open('values.csv', 'w', newline='') as csvfile:
    weather_writer = csv.writer(csvfile)
    weather_writer.writerow(['mesic_1','mesic_2','mesic_3','mesic_4','mesic_5','mesic_6','mesic_7','mesic_8','mesic_9',
                             'mesic_10','mesic_11','mesic_12','suma_rok','typ','rok','kraj'])
    weather_writer.writerows(table)