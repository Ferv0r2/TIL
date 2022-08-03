import requests
from bs4 import BeautifulSoup

# 기상청(도시별 현재날씨) 주소
address = 'https://www.weather.go.kr/weather/observation/currentweather.jsp'

source = requests.get(address)
soup = BeautifulSoup(source.content, "html.parser")

table = soup.find('table', {'class':'table_develop3'})

print("Today's Weather")
print('지점\t 기온\t 습도')

for tr in table.find_all('tr'):
    tds = list(tr.find_all('td'))
    for td in tds:
        if td.find('a'):
            point = td.find('a').text
            temp = tds[5].text
            humidity = tds[9].text
            print("{0:<7} {1:<7} {2:<7}".format(point,temp,humidity))

# 하나의 항목만 선택하고 싶을 때, Selector를 가져와서 넣으면 됨
weather = soup.select_one('#digital-forecast > div.cmp-dfs-slider.hr1-fct')
weather = soup.select('#digital-forecast > div.cmp-dfs-slider.hr1-fct')