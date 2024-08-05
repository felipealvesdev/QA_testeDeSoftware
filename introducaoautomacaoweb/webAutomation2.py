from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://wcaquino.me/cypress/componentes.html")

nome = driver.find_element(By.CSS_SELECTOR, "#formNome")
nome.send_keys("Felipe")

sobrenome = driver.find_element(By.CSS_SELECTOR, "#formSobrenome")
sobrenome.send_keys("Alves")

sexo = driver.find_element(By.CSS_SELECTOR, "#formSexoMasc")
sexo.click()

comidaFavorita = driver.find_element(By.CSS_SELECTOR, "#formComidaCarne")
comidaFavorita.click()

escolaridade = driver.find_element(By.CSS_SELECTOR, "#formEscolaridade")
escolaridade.click()
escolaridadeSelecionada = driver.find_element(By.TAG_NAME, "option[1]")
escolaridadeSelecionada.click()


time.sleep(5)

driver.close()