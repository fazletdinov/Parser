from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from requests import Session

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

def search_page():
    for page in range(1,2):
        url = f'https://www.moscowbooks.ru/books/fiction/?page={page}'
        response = work.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        url_list = soup.find_all('div', class_='catalog__item col-xs-2 col-sm-1 col-md-1 js-catalog-item')
        for url in url_list:
            url_books = 'https://www.moscowbooks.ru' + url.find('a').get('href')
            yield url_books

