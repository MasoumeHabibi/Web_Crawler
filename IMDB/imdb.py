import requests as re
from bs4 import BeautifulSoup as bs
import pandas as pd
import time


link = "https://www.imdb.com/title/tt"
first_page_number = 1190634


def main():
    df = pd.DataFrame(columns=['summery'])
    index = 1
    for page_number in range(first_page_number, 1190664):
        try:
            page = re.get(link + str(page_number))
            soup = bs(page.content, 'html.parser')
            # title = soup.find('div', {'class': 'title_wrapper'})
            summery = soup.find('div', {'class': 'summary_text'})

            data = {'Summery': summery}

            df.append(data, ignore_index = "True")

        except AttributeError:
            continue

    df.to_csv("imdb" + str(index) + ".csv", encoding="utf-8-sig")


if __name__ == "__main__":
    t = time.time()
    main()
    t2 = time.time() - t
    print(t2)