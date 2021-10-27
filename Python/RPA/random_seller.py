import time, sys, random, pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
import subprocess, shutil, pyautogui, json

PW = '###PW###'

login_addr = "###주소###"
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


# 로그인
driver.get(url=login_addr)

time.sleep(1)
show = driver.find_element_by_xpath('/html/body/div[1]/div[1]/main/div/div/div/div[2]/button').click()
kaikas = driver.find_element_by_xpath("/html/body/div[1]/div[1]/main/div/div/div/div[2]/ul/li[5]/button").click()

time.sleep(1)
window = driver.window_handles
driver.switch_to_window(window[1])
passwd = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div/input').send_keys(PW)

onClick = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/button/span').click()

time.sleep(1)
onCheck = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[3]/label/div[1]').click()
onConnect = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[4]/header/button[2]').click()

time.sleep(1)
driver.switch_to_window(window[0])
time.sleep(2.5)

# 작업 시작
index = start - 300
for page in range(start, end+1):
    driver.get(url=address+str(page+3))
    time.sleep(4)

    div_scroll = driver.find_element_by_xpath("/html/body/div[1]/div[1]/main/div/div/div/div[1]/div/div[1]/div[2]/div[3]/div[2]/div/div/div/div/div/div")


    for _ in range(8): # 길이에따라 조정 필요
        driver.execute_script("arguments[0].scrollBy(0, 1000)", div_scroll)
        time.sleep(1.5)

    content = driver.find_element_by_xpath("/html/body/div[1]/div[1]/main/div/div/div/div[1]/div/div[1]/div[2]/div[3]/div[2]/div/div/div/div/div/div/ul")
    keywords = content.text.split('\n')

    string = ""
    string_list = []
    cost_list = [] # 가격 미달 필터
    final_list = [] # 이름만 추출

    keywords.insert(5, 'null')
    for i in range(len(keywords)):
        if i > 5:
            string += keywords[i] + " "
            if (i+1) % 6 == 0:
                string_list.append(string)
                string = ""

    for i in range(len(string_list)):
        if float(string_list[i][0:3]) >= 0:
                cost_list.append(string_list[i])

    for i in range(len(cost_list)):
        value = cost_list[i].split(' ')[-3]
        if value not in final_list:
            final_list.append(value)

    print('최종 리스트 : ', final_list)
    ran = random.randrange(len(final_list))

    print('랜덤 번호 : ', ran)
    
    give = driver.find_element_by_xpath(
        f'/html/body/div[1]/div[1]/main/div/div/div[2]/div[1]/div/div[1]/div[2]/div[3]/div[2]/div/div/div/div/div/div/ul/li[{ran+2}]/div[5]').text
    
    acpt = driver.find_element_by_xpath(
        f'/html/body/div[1]/div[1]/main/div/div/div[2]/div[1]/div/div[1]/div[2]/div[3]/div[2]/div/div/div/div/div/div/ul/li[{i+2}]/div[6]/div/div/div/span/button').send_keys(Keys.ENTER)

    index += 1

    print('============================')
    print('#%4d 당첨자는 %s 님입니다. : ' %(page,give))
    print('거래 진행중')
    print('============================')
    
    # 첫 거래만 안전하게 테스팅 진행
    if index == 1:
        print(give)
        input()

    time.sleep(2)
    papup_btn = driver.find_element_by_xpath(
        '//*[@class="Blockreact__Block-sc-1xf18x6-0 Modalreact__ModalFooter-sc-xyql9f-4 CheckoutModalreact__StyledFooter-sc-3k02w3-0 dBFmez hLwTLZ iaPZMm"]/div/div').click()
    time.sleep(2)
    
    papup_btn = driver.find_element_by_xpath('//*[@class="Panel--content-container"]/div/button').click()
    time.sleep(2)
    
    window = driver.window_handles
    driver.switch_to_window(window[1])

    onClick = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[3]/header/button[2]').click()

    time.sleep(20)

    driver.switch_to_window(window[0])


driver.close()
print('작업완료')