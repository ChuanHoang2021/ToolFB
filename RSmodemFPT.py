import time
import socket
import requests
import pyautogui
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#hàm kiểm tra kết nối mạng
REMOTE_SERVER = "one.one.one.one"
def is_connected(hostname):
  try:
    # see if we can resolve the host name -- tells us if there is
    # a DNS listening
    host = socket.gethostbyname(hostname)
    # connect to the host -- tells us if the host is actually
    # reachable
    s = socket.create_connection((host, 80), 2)
    s.close()
    return True
  except:
     pass
  return False

#hàm lấy ip
def lay_ip():
    get = requests.get('https://api.freegeoip.app/json/?apikey=353abc30-c2b9-11ec-82e8-0109dbd7171b')
    text = get.json()
    ip = text['ip']
    print("ĐỊA CHỈ IP HIỆN TẠI LÀ:",ip)

#hàm đếm ngược
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)  #tách phút và giây từ biến t
        timeformat = '{:02d}:{:02d}'.format(mins, secs) #định dạng thời gian hiển thị đếm ngược
        print('Còn ',timeformat, 'đến lần reset tiếp theo',end='\r') #hiển thị thời gian đếm ngược
        time.sleep(1) # chờ 1s và update thời gian
        t -= 1  #đếm ngược từng giây cho tới 0

#hàm mở chrome reset modem
def open_chrome(user,pasw):
    chr_options = Options()
    chr_options.add_argument('--incognito')
    chr_options.add_argument('--window-size=750,550')
    browser = webdriver.Chrome(chrome_options=chr_options, executable_path='chromedriver.exe')
    browser.get('http://192.168.1.1')
    sleep(2)
    browser.find_element_by_id('username').send_keys(user)
    sleep(1)
    browser.find_element_by_id('password').send_keys(pasw)
    sleep(1)
    browser.find_element_by_id('password').send_keys(Keys.ENTER)
    sleep(1)
    pyautogui.moveTo(700,200,0.25)
    sleep(1)
    pyautogui.click()
    pyautogui.moveTo(340,380,0.25)
    pyautogui.click()
    sleep(1)
    pyautogui.keyDown('Enter')
    pyautogui.keyUp('Enter')
    sleep(13)
    browser.close()
    sleep(2)
    print('Đang RESET modem...')
    # countdown(60)
    sleep(2)
    i = 0
    while not is_connected(REMOTE_SERVER):
        i+=1
        print('Chưa có mạng ',i, end='\r')
        sleep(1)
    print('Đã có kết nối mạng!')
    sleep(2)
    print('Đã có IP mới!')
    sleep(2)
    lay_ip()


#nhập thông số
while not is_connected(REMOTE_SERVER):
    i += 1
    print('Chưa có mạng ', i, end='\r')
    sleep(1)
lay_ip()
usermd = input('username = ')
paswmd = input(('password = '))
delay = int(input('Thời gian delay giữa các lần reset = '))
n = int(input('Số lần muốn reset = '))
sleep(1)
while n>0:
    print('Còn ',n,' lần RESET!')
    sleep(2)
    while not is_connected(REMOTE_SERVER):
        i += 1
        print('Chưa có mạng ', i, end='\r')
        sleep(1)
    print('Mở chrome')
    sleep(1)
    open_chrome(usermd, paswmd)
    n -= 1
    countdown(delay)
