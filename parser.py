from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from requests import Session
import time

headers = {"User-Agent": UserAgent().opera}

work = Session() # Создаем сессию

work.get('https://www.moscowbooks.ru', headers=headers) # Отправляем get запрос,
                                                        # аналогия входа на станицу

response = work.get('https://www.moscowbooks.ru/user/login/', headers=headers)

soup = BeautifulSoup(response.text, 'lxml')

token = soup.find('form', class_="account-form form js-account-form").find('input').get('value') # получаем токен

pyload = {"__RequestVerificationToken": token, "Email": "testusert022@gmail.com",
           "Password": "testusert12345", "RememberMe": False}

work.post('https://www.moscowbooks.ru/user/login/', headers=headers, data=pyload, allow_redirects=True)

def download(url_img):

    result = work.get(url_img, headers=headers, stream=True)
    with open('/home/lich/Desktop/Github/Parser/image_books/' + url_img.split('/')[-1], 'wb') as file:
        for url in result.iter_content():
            file.write(url)

def search_page():
    for page in range(1, 2):
        url = f'https://www.moscowbooks.ru/books/fiction/?page={page}'
        response = work.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        url_list = soup.find_all('div', class_='catalog__item col-xs-2 col-sm-1 col-md-1 js-catalog-item')
        for url in url_list:
            url_books = 'https://www.moscowbooks.ru' + url.find('a').get('href')
            yield url_books

def array_books():
    for url_book in search_page():
        response = work.get(url_book, headers=headers)
        time.sleep(1)
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find('div', class_='container')
        author = data.find('a', class_='author-name').text
        name_book= data.find('h1', class_='page-header__title').text.strip()
        price = data.find('span', class_='rubs').text
        genre = data.find('div', class_='genre_block').find('a', class_='genre_link').text
        publisher = data.find('dt', class_='book__details-value').find('a').text
        annotathion = data.find('div', class_='book__description collapsed js-book-description').text.strip()
        img_url = 'https://www.moscowbooks.ru' + data.find('div', class_='book__cover').find('img').get('src')
        download(img_url)
        yield author, name_book, price, genre, publisher, annotathion
