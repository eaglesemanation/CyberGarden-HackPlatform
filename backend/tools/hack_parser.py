from bs4 import BeautifulSoup
import json

with open('hackathons.htm', 'r', encoding='utf8') as html:
    page = BeautifulSoup(html.read(), 'html.parser')

data = []
for card in page.find_all(attrs={"class": "event-list-item"}):
    print(card)
    link = card.a['href']
    name = card.find(attrs={"class": "event-list-item__title"}).string.strip()
    url = 'https://cdn22.img.ria.ru/images/07e4/05/06/1571020469_0:0:1920:1080_600x0_80_0_0_8492ea5758147feadb42f576ad3ae00c.jpg'
    data.append({"url": link, "name": name, "image": url})


with open('data.json', 'w', encoding='utf8') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)
