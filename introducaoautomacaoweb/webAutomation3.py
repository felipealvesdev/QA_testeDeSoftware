from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializar o webdriver
driver = webdriver.Chrome()

# Acessar uma página
driver.get("https://wcaquino.me/cypress/componentes.html")

# Localizar os elementos na tela
campo_nome = driver.find_element(By.ID, 'formNome')
campo_sobrenome = driver.find_element(By.CSS_SELECTOR, '#formSobrenome')
campo_sugestoes = driver.find_element(By.CSS_SELECTOR, 'textarea[id="elementosForm:sugestoes"]')
radio_sexo_masc = driver.find_element(By.CSS_SELECTOR, '#formSexoMasc')
btn_click_me = driver.find_element(By.CSS_SELECTOR, "#buttonSimple");

# Escrevendo em campos de texto
campo_nome.send_keys("David")
campo_sobrenome.send_keys("Brandao")
campo_sugestoes.send_keys("Consegui escrever aqui")

# Clicando em botões - radio buttons - checkboxes
radio_sexo_masc.click()

# Recuperar o valor de texto de um elemento (Método nativo)
print(campo_nome.text)

# Recuperar o texto via atributo (Caso o método ".text" nativo não funcione)
texto_antes = btn_click_me.get_attribute("value")
print(texto_antes)
btn_click_me.click()
texto_depois = btn_click_me.get_attribute("value")
print(texto_depois)

# Esperando antes/depos de interagir com um elemento

# Clicar no botão "Resposta demorada"
btn_delay = driver.find_element(By.CSS_SELECTOR, "#buttonDelay");
# Esperar 5 segundos
time.sleep(5)
# Mapear o novo campo
btn_novo = driver.find_element(By.ID, "novoCampo")
# Manipular o novo campo
btn_novo.send_keys("Teste")
# Percebam que sem o "Time.Sleep" na linha 42, o código não funciona
# O que podemos fazer caso o botão demore mais que 5 segundos para aparecer?


time.sleep(10)

driver.close()