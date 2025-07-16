import requests
from bs4 import BeautifulSoup


try:
    response = requests.get("https://ratcatcher.ru/media/summer_prac/parcing/25/index.html")
    if response.status_code == 200:
        html_content = response.content
    else:
        raise Exception(f"Не получилось скачать файл, статус: {response.status_code}")
    soup = BeautifulSoup(html_content, "html.parser")

    urls = soup.find("ul").get_text().split()

    with open('urls.txt', 'w') as file:
        file.write("\n".join(urls))
except Exception as e:
    print(f'Ошибка: {e}')
