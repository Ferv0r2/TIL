import requests
from bs4 import BeautifulSoup

# 기상청(도시별 현재날씨) 주소
address = r'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&oquery=%EB%82%A0%EC%94%A8&tqi=hkh4zsprvN8ssO7dffNssssstaV-304653'

source = requests.get(address)
soup = BeautifulSoup(source.content, "html.parser")

weather = soup.select_one('#main_pack > section.sc_new.cs_weather_new._cs_weather > div._tab_flicking > div.content_wrap > div.open > div:nth-child(1) > div > div.weather_info > div > div.temperature_info > p > span.weather.before_slash')

print(weather.text)