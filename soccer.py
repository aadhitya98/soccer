import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.android.webdriver import WebDriver
def main():
    driver=webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')
    wait = WebDriverWait(driver, 100)
    driver.get("https://www.fifa.com/worldcup/players/player/229397/")
    val=driver.find_element_by_xpath("//h1[@class='fi-ph__player__name']")
    print(val.text)
    val2=driver.find_element_by_xpath("//div[@class='fi-p__profile-text']")
    print(driver.find_element_by_xpath("//div[@class='fi-p__profile-text']").text)
    driver.quit()
if __name__ == '__main__':
    main()
