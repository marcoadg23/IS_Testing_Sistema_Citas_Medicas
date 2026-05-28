import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

URL="https://marcoadg23.github.io/IS2026-2-Sistema-citas-medicas/"

@pytest.fixture
def driver():
    d=webdriver.Chrome()
    yield d
    d.quit()

def test_carga_pagina(driver):
    driver.get(URL)
    assert driver.title=="Login"

def test_login_correcto(driver):
    driver.get(URL)
    campos = driver.find_elements(By.CLASS_NAME,"entradaTexto")
    campos[0].send_keys("marco.delgado.ingenieria@gmail.com")
    campos[1].send_keys("123")
    driver.find_element(By.ID,"btnIngresar").click()
    time.sleep(2)
    try:
        assert "principal.html" in driver.current_url
    except:
        os.makedirs("evidencias",exist_ok=True)
        driver.save_screenshot("evidencias/test_fallido.png")
        raise

def test_login_incorrecto(driver):
    driver.get(URL)
    campos = driver.find_elements(By.CLASS_NAME,"entradaTexto")
    campos[0].send_keys("no_esta@gmail.com")
    campos[1].send_keys("no_123")
    driver.find_element(By.ID,"btnIngresar").click()
    time.sleep(2)
    try:
        assert driver.find_element(By.ID,"mensaje").text=="Credenciales incorrectas"
    except:
        os.makedirs("evidencias",exist_ok=True)
        driver.save_screenshot("evidencias/test_fallido.png")
        raise