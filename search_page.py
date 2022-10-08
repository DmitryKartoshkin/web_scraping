import requests
from bs4 import BeautifulSoup


URL = 'https://habr.com'
HEADERS = {'Cookie': 'uxs_uid=0d68acd0-3cbe-11ed-b2cb-a1907aa785ba; _ym_uid=1664102253503231630; _ym_d=1664102254',
           'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
           'Sec-Fetch-Dest': 'empty',
           'Sec-Fetch-Mode': 'no-cors',
           'Sec-Fetch-Site': 'same-origin',
           'Cache-Control': 'max-age=0',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0'
           }

KEYWORDS = ['дизайн', 'фото', 'web', 'python'] #, 'IT', 'ИТ']

response = requests.get(URL, headers=HEADERS)
text = response.text

soup = BeautifulSoup(text, 'html.parser')

posts = soup.find_all('article')

for post in posts:
    publication = post.find(class_='tm-article-body tm-article-snippet__lead')

    for el in KEYWORDS:
        if el in publication.text:

            time = post.find(class_='tm-article-snippet__datetime-published') # поиск даты
            title= post.find('h2').find('span') # поиск заголовка
            href = post.find(class_='tm-article-snippet__title-link').attrs['href']  # поиск ссылки
            result = f' Дата публикации: {time.text} заголовок статьи: {title.text} ссылка: {URL + href}'
            print(result)

