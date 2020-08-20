from selenium import webdriver
from time import sleep

# import pyautogui
from chrome_options import getChromeOptions
from plyer_test import notify
from quoka import getToQuokaArticleListPage, getAnzahl, clickOnFirstElement

driver = webdriver.Chrome('C:/Users/Alex/Downloads/chromedriver_win32/chromedriver.exe', options=getChromeOptions())
getToQuokaArticleListPage(driver)
anzahlOld = getAnzahl(driver)


while True:
    # pyautogui.hotkey('F5')
    sleep(3)
    anzahl = getAnzahl(driver)
    if anzahl != anzahlOld:
        name, standort = clickOnFirstElement(driver)
        notify(standort.text, name.text)
    print(anzahl)
    button = driver.find_element_by_css_selector('#searchbutton')
    button.click()
# driver.close()
