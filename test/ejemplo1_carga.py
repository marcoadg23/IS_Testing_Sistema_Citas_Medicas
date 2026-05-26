from selenium import webdriver

#A - Preparar
driver = webdriver.Chrome()

#A - Ejecutar
driver.get("https://marcoadg23.github.io/IS2026-2-Sistema-citas-medicas/")

#A - Verificar
assert "Login" in driver.title
print("El sistema cargó correctamente")
print("Título:", driver.title)

#limpiar
driver.quit()