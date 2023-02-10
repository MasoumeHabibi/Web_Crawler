from bs4 import BeautifulSoup as bs
import requests as req

def main():
    for i in range(2563594, 2563599):
        try:
            link = "https://www.digikala.com/product/dkp-"
            page = req.get(link + str(i))
            soup = bs(page.content, 'html.parser')
            title = soup.find("h1", {"class": "c-product__title"}).get_text()
            print(title)

        except AttributeError:
            continue



if __name__ == "__main__":
    main()