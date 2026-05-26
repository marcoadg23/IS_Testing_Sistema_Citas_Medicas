from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#A - Preparar
driver = webdriver.Chrome()
driver.get("https://marcoadg23.github.io/IS2026-2-Sistema-citas-medicas/")

#A - Ejecutar
campos = driver.find_elements(By.CLASS_NAME,"entradaTexto")

campos[0].send_keys("marco.delgado.ingenieria@gmail.com")
campos[1].send_keys("123")

driver.find_element(By.ID,"btnIngresar").click()

time.sleep(5)

#A - Verificar
assert "principal.html" in driver.current_url
print("El login sí jala")

#limpiar
driver.quit()