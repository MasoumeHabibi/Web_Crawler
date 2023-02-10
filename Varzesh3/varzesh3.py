from bs4 import BeautifulSoup as bs
import requests as req

def main():
    for i in range(1746931, 1746939):
        try:
            link = 'https://www.varzesh3.com/news/'
            page = req.get(link + str(i))
            soup = bs(page.content, 'html.parser')
            title = soup.find("h1", {"class": "news-page--news-title"}).get_text()
            print(title)

        except AttributeError:
            continue


if __name__ == "__main__":
    main()
