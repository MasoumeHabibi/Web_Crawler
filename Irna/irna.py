from bs4 import BeautifulSoup as bs
import requests as req

def main():
    for i in range(84281681, 84281691):
        try:
            link = "https://www.irna.ir/news/"
            page = req.get(link + str(i))
            saw = bs(page.content, 'html.parser')
            title = saw.find("h1", {"class": "title"}).get_text()
            paragraph = saw.find("p", {"class": "summary introtext"}).get_text()
            print(title)
            print(paragraph)
            print("---------------------------")

        except AttributeError:
            continue



if __name__ == "__main__":
    main()