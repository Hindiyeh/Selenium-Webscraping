import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

path = "C:\chromedriver.exe"

driver = webdriver.Chrome(path)

driver.get("https://www.eastern.com.jo/")
print(driver.title)

driver.find_element_by_class_name("x-btn-navbar-search").click()

search = driver.find_element_by_id("s")
search.send_keys("about")
search.send_keys(Keys.RETURN)

WebDriverWait(driver, 10)

main = driver.find_element_by_id("x-root")

articles = main.find_element_by_class_name("entry-header")
for article in articles:
    header = article.find_element_by_class_name("entry-title")
    print(header.text)
    
print('yooooo')




