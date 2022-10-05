import time
from threading import Thread
import requests
from bs4 import BeautifulSoup


def get_vacancies(count):
    for i in range(count):
        url = f'https://www.work.ua/ru/jobs-developer/?page={i}'
        response = requests.get(url=url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            vacancies_names = soup.find_all('div', class_='card card-hover card-visited wordwrap job-link')
            for name in vacancies_names:
                price = name.b.text
                if 'грн' in price:
                    print(f'{name.a["title"]} - {price}')


start = time.perf_counter()
get_vacancies(16)
print('end\n')
end = time.perf_counter()
print(f'time wthout threads = {end - start:0.2f}')


start2 = time.perf_counter()
threads = []
x = Thread(target=get_vacancies, args=(16,))
x.start()
# threads.append(x)
# for x in threads:
#     x.join()

end2 = time.perf_counter()
print(f'time wthout threads = {end2 - start2:0.2f}')