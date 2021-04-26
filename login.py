from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import search


url='****'
url_2='****'
url_3='****'

userid='****'
passwd='****'

options = Options()
options.add_argument('--headless')
browser=webdriver.Chrome(executable_path=chrome,options=options)

def Login():
    browser.get(url)

    id=browser.find_element_by_xpath("//input[@name='USERID']")
    password=browser.find_element_by_xpath("//input[@name='USERPASSWD']")

    if id and password:
        id.send_keys(userid)
        password.send_keys(passwd)

        osu=browser.find_element_by_xpath(".//input[@type='submit']")
        osu.click()
        sleep(1)
        return next()
    else:
        return False

def next():
    url=browser.current_url
    if url==url_2:
        osu=browser.find_element_by_xpath(".//input[@type='submit'][@value='この車種を選択']")
        osu.click()
        sleep(1)
        return last()
    else:
        return False

def last():
    url=browser.current_url
    tugi=browser.current_url
    if url==url_3:
        html=browser.page_source
        kekka=search.clear(html)
        if len(kekka)==1:
            return False
        else:
            return kekka
    else:
        return False

def main():
    browser.get(url)
    log=Login()
    return log
