import requests 
from lxml import etree 
import time

def  get_house_price(url):
    html = requests.get(url).content 
    seletor = etree.HTML(html) 
    prices = seletor.xpath('//*[@class="price"]/span')
    for price in prices:
        house_price = price.xpath('text()')[0]
    get_house_info(url,house_price)

def get_house_info(url,house_price):
    html = requests.get(url).content
    seletor = etree.HTML(html)
    names = seletor.xpath('//*[@class="hsname"]')
    for name in names:
        house_name = name.xpath('text()')[0]
        house_list.append(house_name)
        print(house_name+'   '+house_price )


if __name__ == '__main__':
    house_list = []
    base_url = 'http://xf.fangdd.com/wuxi/loupan/pg1%s'
    start = time.time()
    for page in range(1,5):
        url=base_url % str(page)
        get_house_price(url)
    end = time.time()
    timeout = end - start
    print('')

