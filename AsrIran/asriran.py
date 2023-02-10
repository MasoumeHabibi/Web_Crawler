from bs4 import BeautifulSoup as bs
import requests as req


def main():
    for i in range (777373, 777383):
        try:
            link = "https://www.asriran.com/fa/news/"
            page = req.get(link + str(i))
            soup = bs(page.content, 'html.parser')
            title = soup.find("h1", {"class": "title"}).get_text()
            print(title)
        except AttributeError:
            continue


if __name__ == "__main__":
    main()