import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
import subprocess

address = "###주소###"

# 원하는 갯수
print('시작 갯수, 끝 갯수 입력')
start, end = map(int, sys.stdin.readline().split())

try:
    subprocess.Popen(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 '
                     r'--user-data-dir="D:\chrometemp"')   # Open the debugger chrome

except FileNotFoundError:
    subprocess.Popen(r'C:\Users\amlk\AppData\Local\Google\Chrome\Application\chrome.exe --remote-debugging-p###PW###ort=9222 '
                     r'--user-data-dir="D:\chrometemp"')

option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
option.add_argument("user-data-dir=C:\\Users\\Username\\AppData\\Local\\Google\\Chrome\\User Data")

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
    
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)

driver.implicitly_wait(10)

index = 0
for page in range(start, end+1):
    driver.get(url=address+str(page+3))    
    for i in range(len(name)):
        give = driver.find_element_by_xpath(
                f'/html/body/div[1]/div[1]/main/div/div/div[2]/div[1]/div/div[1]/div[2]/div[3]/div[2]/div/div/div/div/div/div/ul/li[{i+2}]/div[5]').text
        print('받는 사람 서치', give)  
        if give == name[index]:
            print('값 발견')
            acpt = driver.find_element_by_xpath(
                f'/html/body/div[1]/div[1]/main/div/div/div[2]/div[1]/div/div[1]/div[2]/div[3]/div[2]/div/div/div/div/div/div/ul/li[{i+2}]/div[6]/div/div/div/span/button').send_keys(Keys.ENTER)
            index += 1
            break

driver.close()