import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import time


link = "https://www.asriran.com/fa/news/"
first_page_number = 779408

def main():
    df = pd.DataFrame(columns=['title', 'content'])
    index = 1
    for page_number in range(first_page_number, 779410):
        try:
            page = requests.get(link + str(page_number))
            soup = bs(page.content, 'html.parser')
            title = soup.find('h1', {'class': 'title'}).get_text()
            content = soup.find('div', {'class': 'body'}).get_text()

            data = {"title": title, "content": content}

            df = df.append(data, ignore_index="True")
            # if page_number % 100 == 0:
            #     df.to_csv("asriran1" + str(index) + ".csv", encoding="utf-8-sig")
            #     index += 1
            #     df = pd.DataFrame(columns=['title', 'content'])

        except AttributeError:
            continue

    df.to_csv("asriran1" + str(index) + ".csv", encoding="utf-8-sig")


if __name__ == "__main__":
    t = time.time()
    main()
    t2 = time.time() - t
    print(t2)