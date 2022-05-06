import pandas as pd

from bs4 import BeautifulSoup as bs
import requests
from urllib.request import urlopen as uReq
import logging as lg

def scraping():
  urls = []
  for i in range(1,10):
    url = f"https://www.realethio.com/property-type/house-for-sale/page/{i}/"
    urls.append(url)
  return(urls)


def web_scrap():
    addreses = []
    prices = []
    size = []
    for j in scraping():
        req = requests.get(j)
        bs_file = bs(req.content, 'html.parser')
        new = bs_file.find_all("div", {"class": "d-flex align-items-center h-100"})
        address = [k.find("address", {"class": "item-address"}).text for k in new]
        price = price = [k.find("li", {"class": "item-price"}).text for k in new]

        addreses.extend(address)
        prices.extend([i.split()[1] for i in price])
        df = pd.DataFrame({"Addreses": addreses, "prices": prices})
    return df