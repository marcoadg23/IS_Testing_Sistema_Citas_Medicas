from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://search.brave.com")
time.sleep(1)

busqueda = driver.find_element(By.NAME,"q")
busqueda.send_keys("Facultad de ingeniería")
time.sleep(2)
busqueda.send_keys(Keys.ENTER)

time.sleep(50)

driver.quit()
