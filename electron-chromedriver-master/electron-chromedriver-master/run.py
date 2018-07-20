import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pageobjects.login import LoginPage
from pageobjects.menu import MainMenu

chromedriver_path = "./chromedriver"
electron_path = "./electron-chromedriver-master"

opts = Options()
opts.binary_location = electron_path
driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=opts)
driver.implicitly_wait(15)  # seconds

time.sleep(3)  # wait for application to start

login_page = LoginPage(driver)
#add login for agama un and pw
login_page.login('', os.environ['PASS'])

time.sleep(15)  # wait for sign in

main_menu = MainMenu(driver)
main_menu.logout()

time.sleep(3)  # wait for logout

main_menu.quit()

driver.quit()
