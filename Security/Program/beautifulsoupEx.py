from bs4 import BeautifulSoup as bs
import requests
url = 'https://d2zoxm4i0garux.cloudfront.net'
r = requests.get(url)
tree = bs(r.text, 'html.parser')  # 트리 구조로 구문 분석
for link in tree.find_all('a'):  # "a" 기호가 포함된 원소를 모두 탐색
    print(f"{link.get('href')}->{link.text}")
