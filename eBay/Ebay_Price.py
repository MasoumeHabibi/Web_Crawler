import requests
from bs4 import BeautifulSoup
import pandas as pd

def main():
    url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=camera&_sacat=0&Brand=Canon&_dcat=31388&LH_Sold=1&LH_Complete=1&rt=nc&LH_Auction=1"

    def get_data(url):
        r = requests.get(url + str(url))
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup

    def parse(soup):
        products_list = []
        results = soup.find_all('div', {'class': 's-item__info clearfix'})
        for item in results:
            products = {
                'title': item.find('div', {'class': "s-item__title"}).get_text(),
                'sold_price': item.find('span', {'class': "s-item__price"}).get_text(),
                'sold_date': item.find('span', {'class': "POSITIVE"}),
                'bids': item.find_all('div', {'class': "s-item__detail s-item__detail--primary"})[1].get_text(),
                'link': item.find('a', {'class': "s-item__link"})['href'],
            }
            # print(products)
            products_list.append(products)
        return products_list

    def output(products_list):
        productsDF = pd.DataFrame(products_list)
        productsDF.to_csv('output.csv', index=False)
        print("Saved to CSV")
        return

    soup = get_data(url)
    # parse(soup)
    products_list = parse(soup)
    output(products_list)


if __name__ == "__main__":
    main()