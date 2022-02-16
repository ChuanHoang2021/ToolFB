import random
import pygame
from pygame import mixer
import pyautogui
import pygame
from pygame import mixer
from tkinter import *
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#biến
sound = '_dien.mp3'
lst = []
rs_ip = 0
so_acc = 0
id_modem = ''
mk_modem = ''
live, die, check, dis, sum, tong = 0, 0, 0, 0, 0, 0
#hàm âm thanh
def amthanh(s):
    mixer.init()
    mixer.music.load(f'Voice\{s}')
    mixer.music.play()
def info_modem():
    global id_modem, mk_modem, rs_ip
    id_modem = user_modem.get()
    mk_modem = pass_modem.get()
    rs_ip = int(reset_ip_sau_En.get())
#hàm reset modem
def reset_modem():
    global id_modem, mk_modem, sound
    sound = '_bat_dau.mp3'
    amthanh(sound)
    chrome_opt = Options()
    chrome_opt.add_argument('--incognito')
    chrome_opt.add_argument('--window-size=750,550')
    chrome = webdriver.Chrome(chrome_options=chrome_opt, executable_path='chromedriver.exe')
    chrome.get('http://192.168.1.1')
    sleep(1)
    chrome.find_element_by_id('username').send_keys(id_modem)
    sleep(1)
    chrome.find_element_by_id('password').send_keys(mk_modem)
    sleep(1)
    chrome.find_element_by_id('password').send_keys(Keys.ENTER)
    sleep(1)
    pyautogui.moveTo(700,200,0.25)
    pyautogui.click()
    sleep(1)
    pyautogui.moveTo(343,389,0.25)
    pyautogui.click()
    pyautogui.keyDown('Enter')
    pyautogui.keyUp('Enter')
#hàm lấy acclog
def lay_acclog():
    global lst
    acclog = open('acclog.txt')
    lst_acclog = acclog.readlines()
    for i in lst_acclog:
        lst.append(i.replace('\n', ''))
    acclog.close()
#hàm ghi file live
def acc_live(a, b):
    # cook = chrome.get_cookies()
    sleep(2)
    sb = 'sb=' + cook[5]['value'] + '; '
    wd = 'wd=' + cook[4]['value'] + '; '
    datr = 'datr=' + cook[2]['value'] + '; '
    c_user = 'c_user=' + cook[3]['value'] + '; '
    xs = 'xs=' + cook[1]['value'] + '; '
    fr = 'fr=' + cook[0]['value'] + '; '
    useragent = 'useragent=TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk1LjAuNDYzOC41NCBTYWZhcmkvNTM3LjM2; '
    _uafec = '_uafec=Mozilla%2F5.0%20(Windows%20NT%2010.0%3B%20Win64%3B%20x64)%20AppleWebKit%2F537.36%20(KHTML%2C%20like%20Gecko)%20Chrome%2F95.0.4638.54%20Safari%2F537.36; '
    full_cookies = sb + wd + datr + c_user + xs + fr + useragent + _uafec
    xuatfile = a + '|' + b + '|' + full_cookies + '\n'
    sleep(2)
    acclive = open('acclive.txt', mode='a+')
    acclive.write(xuatfile)
    acclive.close()
#hàm ghi file checkpoint
def acc_checkpoint(a, b):
    acccheckpoint = open('acccheckpoint.txt', mode='a+')
    acccheckpoint.write(a + '|' + b + '\n')
    acccheckpoint.close()
#hàm ghi file die
def acc_die(a, b):
    accdie = open('accdie.txt', mode='a+')
    accdie.write(a + '|' + b + '\n')
    accdie.close()
#hàm disable
def disable(a, b):
    accdisable = open('accdisable.txt', mode='a+')
    accdisable.write(a + '|' + b + '\n')
    accdisable.close()
#hàm mở chrome và chạy
def chay_chrome(a, b):
    global cook, check, dis, live, die, num_live, num_die, num_cp, num_dis
    # cài đặt 1 số options cho trình duyệt
    chrome_options = Options()
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--window-size=500,500')
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option('prefs', prefs)
    prefs_cache = {'disk-cache-size': 4096}
    chrome_options.add_experimental_option('prefs', prefs)
    #mở chrome
    chrome = webdriver.Chrome(chrome_options=chrome_options, executable_path='chromedriver.exe')
    chrome.get('https://fb.com')
    sleep(random.randint(1,5))
    id = chrome.find_element_by_id('email')
    id.send_keys(a)
    pas = chrome.find_element_by_id('pass')
    sleep(random.randint(1,3))
    pas.send_keys(b)
    sleep(random.randint(1,3))
    pas.send_keys(Keys.ENTER)
    adress = chrome.current_url
    cook = chrome.get_cookies()
    sleep(random.randint(1,3))
    chrome.refresh()
    adress = chrome.current_url
    print(adress)
    if '?next=https' in adress:
        dis+=1
        print('Tài khoản bị vô hiệu hoá! = ', dis)
        disable(a, b)
        print('Ghi ra file thành công!')
        num_dis.config(text=str(dis))
    elif 'https://www.facebook.com/checkpoint/?next' in adress:
        check+=1
        print('Tài khoản này checkpoint! = ', check)
        acc_checkpoint(a, b)
        print('Ghi ra file thành công!')
        num_cp.config(text=str(check))
    else:
        sleep(random.randint(1,3))
        chrome.get('https://www.facebook.com/settings')
        adress = chrome.current_url
        if 'https://www.facebook.com/settings' in adress:
            live+=1
            print('Tài khoản này live! = ', live)
            sleep(2)
            print('Đang lấy cookies...')
            sleep(random.randint(2,4))
            print(cook)
            acc_live(a, b)
            print('Ghi ra file thành công!')
            num_live.config(text=str(live))
        else:
            die+=1
            print('Tài khoản này die! = ', die)
            acc_die(a, b)
            print('Ghi ra file thành công!')
            num_die.config(text=str(die))

#hàm khởi chạy chương trình
def start_app():
    start.config(text='Đã xong', bg='#ccec29')
    global sum, tong, rs_ip, sound
    sound = '_start_get.mp3'
    amthanh(sound)
    for i in lst:
        i = i.split('|')
        a = i[0]
        b = i[1]
        chay_chrome(a,b)
        sum+=1
        tong+=1
        print('Tổng số acc đã GET = ', tong, ' LIVE = ', live, " DIE = ", die, ' CHECKPOINT = ', check, ' DISABLE = ', dis)
        if sum==rs_ip:
            sound = '_cbi_reset.mp3'
            amthanh(sound)
            sleep(5)
            reset_modem()
            sleep(100)
            sound = '_tiep_tuc.mp3'
            sum=0
        da_get.config(text=f'ĐÃ GET {tong} ACC!', fg='#9ab502')
    print('CHƯƠNG TRÌNH ĐÃ CHẠY XONG!')
    sound = '_da_xong.mp3'
    amthanh(sound)
#hàm đóng chương trình
def exit():
    win.destroy()
def update():
    global so_acc, rs_ip, sound
    sound = '_da_luu.mp3'
    info_modem()
    so_acc = len(lst)
    reset_tb.config(text=f'Reset IP sau = {rs_ip}', font=10, fg='#9ab502')
    tong_get.config(text=f'Tổng số acc = {so_acc}', font=10, fg='#9ab502')
    thong_bao.config(text='Đã cập nhật!', fg='#9ab502')
    num_live.config(text=str(live))
    num_die.config(text=str(die))
    num_cp.config(text=str(check))
    num_dis.config(text=str(dis))
    amthanh(sound)
#giao diện
lay_acclog()
amthanh(sound)
win = Tk()
win.title('Get Cookies FB')
win.geometry("570x250")
win.eval('tk::PlaceWindow . center')

reset_tb = Label(win, text='acc', font=10)
reset_ip_sau_lb = Label(win, text='Reset ip sau:   ', font=10)
da_get = Label(win, text='ĐÃ GET = 0', font=10, fg='#000e87')
tong_get = Label(win, text='Số acc chưa update!', font=10)
thong_bao = Label(win, text='Chưa cập nhật!', font=10, fg='red')
user = Label(win, text='Tên đăng nhập:', font=10)
pas_md = Label(win, text='Mật khẩu:         ', font=10)
reset_ip_sau_En = Entry(win)
user_modem = Entry(win)
pass_modem = Entry(win, show='*')
reset_ip = Button(win, text='RESET IP', font='10', bg='#fe7653', height=2, width=10, command=reset_modem)
start = Button(win, text='Chạy', font='10', bg='green', height=2, width=10, command=start_app)
exit = Button(win, text='Thoát', font='10', bg='red', height=2, width=10, command=exit)
up = Button(win, text='Cập nhật', font='10', bg='#45d091', height=2, width=10, command=update)

ac_live = Label(win, text='Live', font='10', bg='#fec780', height=2, width=15)
ac_die = Label(win, text='Die', font='10', bg='#fec780', height=2, width=15)
ac_cp = Label(win, text='Checkpoint', font='10', bg='#fec780', height=2, width=15)
ac_dis = Label(win, text='Disable', font='10', bg='#fec780', height=2, width=15)

num_live = Label(win, text='0', font='10', bg='#c1e401', height=2, width=15)
num_die = Label(win, text='0', font='10', bg='red', height=2, width=15)
num_cp = Label(win, text='0', font='10', bg='yellow', height=2, width=15)
num_dis = Label(win, text='0', font='10', bg='blue', height=2, width=15)

da_get.grid(column=3, row=4)
tong_get.grid(column=2, row=4)
thong_bao.grid(column=2, row=3)
reset_ip.grid(column=0, row=2)
start.grid(column=1, row=2)
exit.grid(column=2, row=2)
up.grid(column=3, row=2)
user.grid(column=0, row=3)
pas_md.grid(column=0, row=4)
user_modem.grid(column=1, row=3)
pass_modem.grid(column=1, row=4)
reset_ip_sau_lb.grid(column=0, row=5)
reset_ip_sau_En.grid(column=1, row=5)
reset_tb.grid(column=2, row=5)

ac_live.grid(column=3, row=0)
ac_die.grid(column=2, row=0)
ac_cp.grid(column=1, row=0)
ac_dis.grid(column=0, row=0)

num_live.grid(column=3, row=1)
num_die.grid(column=2, row=1)
num_cp.grid(column=1, row=1)
num_dis.grid(column=0, row=1)

win.mainloop()