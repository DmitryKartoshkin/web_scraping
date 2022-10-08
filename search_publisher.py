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

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

response = requests.get(URL, headers=HEADERS)
text = response.text

soup = BeautifulSoup(text, 'html.parser')

posts = soup.find_all('article')
list_result = []

for post in posts:
    href = post.find(class_='tm-article-snippet__title-link').attrs['href']  # поиск ссылки
    URL_NEW = URL + href

    response = requests.get(URL_NEW, headers=HEADERS)
    text = response.text

    soup = BeautifulSoup(text, 'html.parser')
    posts_new = soup.find_all('article')

    for post_new in posts_new:
        text_full = post_new.find(id="post-content-body")
        for el in KEYWORDS:
            if el in text_full.text:
                time = post.find(class_='tm-article-snippet__datetime-published')  # поиск даты
                title = post.find('h2').find('span')  # поиск заголовка
                href = post.find(class_='tm-article-snippet__title-link').attrs['href']  # поиск ссылки
                result_list = [time.text, title.text, URL + href]
                for res in list_result:
                    if res[1] == result_list[1]:
                        break
                else:
                    list_result.append(result_list)
for el in list_result:
    print(f' Дата публикации: {el[0]} заголовок статьи: {el[1]} ссылка: {el[2]}')


