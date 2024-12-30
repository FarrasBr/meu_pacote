from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


def digitar(xpaht=None, classe=None, Texto=None, Enter=None):
    if xpaht != None:
        campo = navegador.find_element(By.XPATH, xpaht)
        campo.send_keys(Texto)
    elif classe != None:
        campo = navegador.find_element(By.CLASS_NAME, classe)
        campo.send_keys(Texto)
    if Enter == "y" or "Y" or "yes":
        campo.send_keys(Keys.RETURN)

def esperar(xpath=None, classe=None):
    if xpath != None:
        botao = WebDriverWait(navegador, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        action = ActionChains(navegador)
        action.move_to_element(botao).perform()
        print("Botão encontrado!")
    elif classe != None:
        botao = WebDriverWait(navegador, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, classe))
        )
        action = ActionChains(navegador)
        action.move_to_element(botao).perform()
        print("Botão encontrado!")

def clikar(xpath=None, movex=None, classe= None):
    if xpath != None:
        botao = navegador.find_element(By.XPATH, xpath)
        botao.click()
    elif movex != None:
        botao = navegador.find_element(By.XPATH, movex)
        action = ActionChains(navegador)
        action.move_to_element(botao).perform()
    elif classe != None:
        botao = navegador.find_element(By.CLASS_NAME, classe)
        botao.click()

if __name__ == "__main__":
    chromedriver_autoinstaller.install()
    navegador = webdriver.Chrome()