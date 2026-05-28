from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#A - Preparar
driver = webdriver.Chrome()
driver.get("https://marcoadg23.github.io/IS2026-2-Sistema-citas-medicas/")

#A - Ejecutar
campos = driver.find_elements(By.CLASS_NAME,"entradaTexto")

campos[0].send_keys("no_existe@gmail.com")
campos[1].send_keys("no_123")

driver.find_element(By.ID,"btnIngresar").click()

time.sleep(5)

mensaje = driver.find_element(By.ID,"mensaje").text

#A - Verificar
assert mensaje=="Credenciales incorrectas"
print("El login sí jala")
driver.save_screenshot("evidencias/test_login_fallido.png")
print("La captura se guardó correctamente")

#limpiar
driver.quit()