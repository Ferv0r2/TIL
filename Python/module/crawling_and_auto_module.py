import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import subprocess, shutil, pyautogui, json


ID = '###ID###'
PW = '###PW###'
WALLET = '###WALLET###'

loginURL = 'https://accounts.google.com/signin/v2/identifier?hl=ko&passive=true&continue=https%3A%2F%2Fwww.google.com%2F'\
        '%3Fgws_rd%3Dssl&ec=GAZAmgQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin'


address = "###ADDRESS##"

# 쿠키 제거 -> 로그인 다시 안해도 됨
# try:
#     shutil.rmtree(r"D:\chrometemp")  # remove Cookie, Cache files
# except FileNotFoundError:
#     pass

try:
    subprocess.Popen(r'###크롬위치### --remote-debugging-port=9222 '
                     r'--user-data-dir="D:\chrometemp"')   # Open the debugger chrome

except FileNotFoundError:
    subprocess.Popen(r'###크롬위치### --remote-debugging-p###PW###ort=9222 '
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

# 로그인 대신 해드립니다
# driver.get(url=loginURL)
# # Google login page

# pyautogui.write(ID)    # Fill in your ID or E-mail
# pyautogui.press('tab', presses=3)   # Press the Tab key 3 times
# pyautogui.press('enter')
# time.sleep(3)   # wait a process
# pyautogui.write(PW)   # Fill in your PW
# pyautogui.press('enter')


driver.get(url=address)

time.sleep(2)

## 팝업창 바꾸기
# 아래 xpath는 F12로 따로 찾아야 함
# .send_keys(넣고싶은 값)
# .click() -> 클릭
window = driver.window_handles
driver.switch_to_window(window[1])
passwd = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/form/div/div/input').send_keys(PW)

onClick = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div/button/span').click()

time.sleep(2)
onCheck = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[3]/label/div[1]').click()
onConnect = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[4]/header/button[2]').click()

time.sleep(2)
driver.switch_to_window(window[0])

# 이미지 업로드
img_Upload = driver.find_element_by_css_selector("input[type='file']")
img_Upload.send_keys(r"D:\pixel\line.PNG")

time.sleep(2)
pyautogui.press('enter')

time.sleep(4)
pyautogui.press('enter')

name_box = driver.find_element_by_id("name").send_keys("DOGE FRIENDS #%04d" %(2))
description_box = driver.find_element_by_id("description").send_keys("description")
attributes_box = driver.find_element_by_id("attributes").send_keys("attributes")

metadata_btn = driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/div/div/section[2]/button").click()

time.sleep(2)
pyautogui.press('enter')

time.sleep(4)
pyautogui.press('enter')

to_box = driver.find_element_by_id("to").send_keys(WALLET)
create_btn = driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/div/div/section[3]/button").click()

time.sleep(2)

window = driver.window_handles
driver.switch_to_window(window[1])

final_btn = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div[3]/header/button[2]").click()

driver.switch_to_window(window[0])

time.sleep(5)
pyautogui.press('enter')