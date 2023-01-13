import requests
from bs4 import BeautifulSoup
from carcode import *

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

# https://www.bobaedream.co.kr/dealguide/market_price_new.php?gubun=K&view_size=20&maker_no=49

base_url = "https://www.bobaedream.co.kr/dealguide/market_price_new.php?gubun=K&view_size=20"
brand_value = Brand['현대']
url = f"{base_url}&maker_no={brand_value}"

response = requests.get(url, headers=headers)
html = response.text
soup = BeautifulSoup(html, "html.parser")
a = soup.find_all('div', class_='area-model')
# b=str(a)
# with open('모델리스트.txt','w',encoding='UTF-8') as f:
#     f.write(b)