from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.google.com.br')
driver.find_element_by_name('q').send_keys('blogdoiphone')
driver.find_element_by_name('q').send_keys(Keys.RETURN)