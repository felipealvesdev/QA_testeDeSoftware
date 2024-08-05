from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")

campo_busca = driver.find_element(By.NAME, "q")
campo_busca.send_keys("Teste de software")
campo_busca.send_keys(Keys.ENTER)
time.sleep(5)

driver.close()