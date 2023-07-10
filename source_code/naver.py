#.py 파일로 만들기

import requests # 거의비슷= from urllib.request.Request
import pandas as pd
from bs4 import BeautifulSoup

url = "https://finance.naver.com/marketindex/"
response = requests.get(url)
# requests.get(), requests.post() - 두가지 방식 존재.
# response.text    --- response에 이미 담겨있음을 확인가능
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify()) - 주석처리 해도 된다고함 (이유 모름)

exchangeList = soup.select('#exchangeList > li')

exchange_datas = []
baseUrl = "https://finance.naver.com"

for item in exchangeList:
    # 시도해보는 클래스 리스트
    classes_to_try = ['head_info.point_dn', 'head_info.point_up']

    # 기본 updown 값을 설정
    updown = None

    # 각 클래스에 대해 시도
    for class_name in classes_to_try:
        element = item.select_one(f'.{class_name} > .blind')
        if element is not None:
            updown = element.text
            break

    data = {
        "title": item.select_one('.h_lst').text,
        "exchange": item.select_one(".value").text,
        "change": item.select_one('.change').text,
        "updown": updown,
        "link" : baseUrl + item.select_one('a').get('href')
    }
    exchange_datas.append(data)

df = pd.DataFrame(exchange_datas)
df.to_excel("./naverfinance.xlsx", encoding="utf-8")