from selenium import webdriver
import time
def initPickALanguage():
    element = window.find_element("xpath", "/html/body/div[2]/div[2]/div[12]/div/div[1]/div[1]/div[2]")
    element.click()
def buyItems():
    buyMore = False
    for item in items:
        if item.get_attribute("class")=="product unlocked enabled":
            item.click()
            buyMore=True
            break
    if buyMore is True:
        buyItems()
if __name__ == '__main__':
    window = webdriver.Chrome("D:\chromedriver.exe")
    window.get("https://orteil.dashnet.org/cookieclicker/")
    time.sleep(2)
    initPickALanguage()
    time.sleep(2)
    cookie = window.find_element("xpath", "/html/body/div[2]/div[2]/div[15]/div[8]/button")
    items = window.find_elements("xpath", "/html/body/div/div[2]/div[19]/div[3]/div[6]/*")
    items.reverse()
    i = 0
    while True:
        cookie.click()
        i += 1
        if i >= 100:
            buyItems()
            i=0