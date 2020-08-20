from time import sleep


def getToQuokaArticleListPage(driver):
    driver.get('http://quoka.de')
    elem = driver.find_element_by_css_selector(
        '#frmSearch > div > div > div.col-xs-4.f-group.horizontal > div:nth-child(1)')
    elem.click()
    button = driver.find_element_by_id("city")
    button.send_keys('Deutschland')
    button = driver.find_element_by_css_selector('#searchbutton')
    button.click()
    sleep(1)


def getAnzahl(driver):
    anzahl_raw = driver.find_element_by_css_selector(
        'body > div.spr-wrp > div.cnv > div.cnt > main > div.box.no-bdr.bg-grey.pad-sml.page-navigation-top > div > div.td.n2')
    anzahl_list = str(anzahl_raw.text).split()
    anzahl = anzahl_list[3].replace(".", "")
    return anzahl


def clickOnFirstElement(driver):
    firstElement = driver.find_element_by_id("ResultListData")
    firstElement.click()
    name = driver.find_element_by_css_selector(
        'body > div.spr-wrp > div.cnv > div.cnt > main > div.box.bdr-grey.docked.detail.big-image > div > div.headline > h1')
    standort = driver.find_element_by_css_selector(
        'body > div.spr-wrp > div.cnv > div.cnt > main > div.box.bdr-grey.docked.detail.big-image > div > div.data > div.details > div:nth-child(1) > strong > span > a > span')
    return name, standort
