import time
from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in")
driver.execute_script("window.scrollBy(0, 600);")
ruby_book=driver.find_element_by_xpath("//a[@href='http://practice.automationtesting.in/product/selenium-ruby/']")
ruby_book.click()
Reviews_button=driver.find_element_by_xpath("//a[@href='#tab-reviews']")
Reviews_button.click()
stars=driver.find_element_by_css_selector('span>a:nth-child(5)')
stars.click()
comment=driver.find_element_by_id('comment')
comment.send_keys("Nice book!")
name=driver.find_element_by_id('author')
name.send_keys('Anastasiia')
email=driver.find_element_by_id('email')
email.send_keys("tarsasov446@rambler.ru")
submit_button=driver.find_element_by_xpath("//input[@name='submit']")
submit_button.click()
