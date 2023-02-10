from bs4 import BeautifulSoup as bs
import requests as req

def main():
    link = "https://www.digikala.com/product/dkp-2563594"
    page = req.get(link)
    soup = bs(page.content, 'html.parser')
    title = soup.find("h1", {"class": "c-product__title"}).get_text()
    price = soup.find("div", {"class": "c-product__seller-price-real"}).get_text()
    print(title)
    print(price)


if __name__ == "__main__":
        main()