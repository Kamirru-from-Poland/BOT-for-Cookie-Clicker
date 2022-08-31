from selenium import webdriver
import time
def initPickALanguage():
    element = window.find_element("xpath", "/html/body/div[2]/div[2]/div[12]/div/div[1]/div[1]/div[2]")
    element.click()
def clickACookie():
    element = window.find_element("xpath", "/html/body/div[2]/div[2]/div[15]/div[8]/button")
    element.click()
if __name__ == '__main__':
    window = webdriver.Chrome("D:\chromedriver.exe")
    window.get("https://orteil.dashnet.org/cookieclicker/")
    time.sleep(2)
    initPickALanguage()
    time.sleep(2)
    clickACookie()


