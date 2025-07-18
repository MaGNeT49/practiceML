import requests
import pandas as pd
from bs4 import BeautifulSoup


def DownloadUrls():
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


def get_urls():
    urls = []
    try:
        with open('urls.txt', 'r') as file:
            urls = file.read().split()

    except Exception:
        print("Не удалось прочитать файл")

    return urls


def get_head():
    try:
        response = requests.get(get_urls()[0])

        if response.status_code == 200:
            html_content = response.content
        else:
            print(f"Ошибка: {response.status_code}")
            raise Exception("Ошибка с сайтом")
    except Exception as e:
        print(f"Ошибка: {e}")

    soup = BeautifulSoup(html_content, "html.parser")

    table = soup.find(id="trilobite")
    head = table.find("thead").get_text().split()

    return head


def get_all_element_table():
    elements = []

    urls = get_urls()

    for url in urls:
        try:
            response = requests.get(url)

            if response.status_code == 200:
                html_content = response.content
            else:
                print(f"Ошибка: {response.status_code}")
                raise Exception("Ошибка с сайтом")
        except Exception as e:
            print(f"Ошибка: {e}")
            break

        soup = BeautifulSoup(html_content, "html.parser")

        table = soup.find(id="trilobite")

        body = table.find("tbody")

        for tr in body.find_all("tr"):
            tds = []
            for td in tr.find_all("td"):
                td = td.get_text()
                tds.append(td)

            elements.append(tds)

    return elements


def download_table_to_csv():
    df = pd.DataFrame(get_all_element_table(), columns=get_head())

    df.to_csv('table.csv', index=False)


download_table_to_csv()
