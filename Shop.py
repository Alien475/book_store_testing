
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in")
my_account=driver.find_element_by_link_text('My Account')
my_account.click()
username=driver.find_element_by_id('username')
username.send_keys("tarsasov446@rambler.ru")
password=driver.find_element_by_id('password')
password.send_keys('Ujlrhscs2021')
password.clear()
password.send_keys('Ujlrhscs2021')
login=driver.find_element_by_xpath('//input[@value="Login"]')
login.click()
shop=driver.find_element_by_link_text('Shop')
shop.click()
book=driver.find_element_by_xpath('//a[@href="http://practice.automationtesting.in/product/html5-forms/"]')
book.click()
name=WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR,'div>h1'), "HTML5 Forms"))
