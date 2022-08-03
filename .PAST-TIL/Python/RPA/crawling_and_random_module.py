import time, sys, random, pandas as pd
from numpy import e
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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

excel_list = []
index_list = []
for page in range(start, end+1):
    driver.get(url=address+str(page+1))
    time.sleep(4)

    div_scroll = driver.find_element_by_xpath("/html/body/div[1]/div[1]/main/div/div/div/div[1]/div/div[1]/div[2]/div[3]/div[2]/div/div/div/div/div/div")

    for _ in range(4):
        driver.execute_script("arguments[0].scrollBy(0, 1000)", div_scroll)
        time.sleep(1.5)

    content = driver.find_element_by_xpath("/html/body/div[1]/div[1]/main/div/div/div/div[1]/div/div[1]/div[2]/div[3]/div[2]/div/div/div/div/div/div/ul")
    keywords = content.text.split('\n')

    string = ""
    string_list = []
    cost_list = []
    final_list = []
    for i in range(len(keywords)):
        string += keywords[i] + " "
        if (i+1) % 5 == 0:
            string_list.append(string)
            string = ""

    for i in range(len(string_list)):
        try:
            if int(string_list[i][0:2]) >= 10:
                cost_list.append(string_list[i])
        except:
            pass

    for i in range(len(cost_list)):
        value = cost_list[i].split(' ')[-2]
        if value not in final_list:
            final_list.append(value)

    print(final_list)
    ran = random.randrange(len(final_list))
    winner = final_list[ran]
    
    excel_list.append(winner)
    index_list.append(page)

df = pd.DataFrame(
    {
        'num' : index_list,
        'name': excel_list
    }
)
df.to_excel('./excel.xlsx', index=False, sheet_name='new_page')

df = pd.read_excel('./excel.xlsx')
print(df)

driver.close()