from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import sys
import tty
tty.setcbreak(sys.stdin)


def get(site):
    try:
        driver.get(site)
        assert ord(sys.stdin.read(1)) == 27
    except:
        get(site)


page_order = [
    "http://127.0.0.1:5000/",
    "http://127.0.0.1:5000/auth/login",
    "http://127.0.0.1:5000/auth/signup/student",
    "http://127.0.0.1:5000/shop/item/1",

]

driver = webdriver.Firefox()
running = True
while running:
    if(ord(sys.stdin.read(1)) == 27):
        if len(page_order) == 0:
            break
        driver.get(page_order.pop(0))


driver.close()


# ord(sys.stdin.read(1)) == 27
