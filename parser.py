from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from requests import Session

headers = {"User-Agent": UserAgent().opera}
payload = {"__RequestVerificationToken": "", "Email": "testuser022@gmail.ru",
           "Password": "testuser12345", "RememberMe": False}

work = Session() # Создаем сессию

work.get('https://www.moscowbooks.ru', headers=headers) # Отправляем get запрос,
                                                        # аналогия входа на станицу

response = work.get('https://www.moscowbooks.ru/user/login/', headers=headers)

soup = BeautifulSoup(response.text, 'lxml')

token = soup.find('form', class_="account-form form js-account-form").find('input').get('value') # получаем токен
payload = {"__RequestVerificationToken": token, "Email": "testusert022@gmail.com",
           "Password": "testusert12345", "RememberMe": False}
work.post('https://www.moscowbooks.ru/user/login/', headers=headers, data=payload, allow_redirects=True)

def search_page():
    for page in range(1, 2):
        url = f'https://www.moscowbooks.ru/books/fiction/?page={page}'
        response = work.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
