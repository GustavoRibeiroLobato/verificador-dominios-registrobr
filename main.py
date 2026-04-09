from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from random import uniform
import pandas as pd


def digitar_como_humano(elemento, texto):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(uniform(0.1, 0.5)) 


def iniciar_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(options=options)

def ler_excel(caminho):
    df = pd.read_excel(caminho,
                   sheet_name="Plan1",
                   usecols=[0],
                   header= None          
                   )
    return df.iloc[:,0].values

def verifica_dominio(driver, dominio):
    try:
        wait = WebDriverWait(driver, 15)

        

        pesquisa = wait.until(
            EC.presence_of_element_located((By.ID, "is-avail-field")))
        
        pesquisa.clear()
        
        
        digitar_como_humano(pesquisa, dominio)
        sleep(uniform(0.05, 0.2))

        

        pesquisa.send_keys(Keys.RETURN)
        sleep(2)

        texto = driver.page_source.lower()
        sleep(uniform(2, 3.0))
        
        if "não disponível" in texto or "já está registrado" in texto:
            return f"{dominio}  INDISPONÍVEL\n"
        elif "disponível" in texto:
            return f"{dominio}  DISPONÍVEL\n"
        else:
            return f"O Dominio {dominio} ERRO NA VERIFICAÇÃO\n"

    except Exception as e:
        return f"ERRO AO BUSCAR O DOMINIO {dominio}: {e}\n"
        

print("Iniciando robô\n")

dominios = ler_excel("excel.xls")
print(dominios)
driver = iniciar_driver()
driver.get("https://registro.br/")


with open("resultado.txt", "w", encoding="utf-8") as arq:
    for dominio in dominios:
        print(dominio)
        texto = verifica_dominio(driver, dominio)
        print(texto)
        arq.write(texto)


driver.quit()