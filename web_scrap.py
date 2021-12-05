import requests
import bs4

URL = 'https://habr.com/ru/all/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
           'Chrome/95.0.4638.69 Safari/537.36', 'accept': '*/*'}
KEYWORDS = {'C++', 'C#', 'Linux', 'Python'}

response = requests.get(URL, headers=HEADERS)

soup = bs4.BeautifulSoup(response.text, features='html.parser')

articles = soup.find_all(class_='tm-articles-list__item')
for article in articles:
    list = []
    check = 0
    title = article.find(class_='tm-article-snippet__title-link').text
    list.append(title)
    tags = article.find(class_='tm-article-snippet__hubs')
    for tag in tags:
        t = tag.find(class_='tm-article-snippet__hubs-item-link').find('span').text
        list.append(t)
    art_text = article.find(class_='tm-article-body tm-article-snippet__lead').text.strip()
    list.append(art_text)
    for word in KEYWORDS:
        for item in list:
            if word in item:
                check += 1
    if check > 0:
        href = article.find(class_='tm-article-snippet__title tm-article-snippet__title_h2').find('a').get('href')
        address = 'https://habr.com'
        time = article.find(class_='tm-article-snippet__datetime-published').find('time').text
        print(f"{time} --- {title} --- {address}{href}")

