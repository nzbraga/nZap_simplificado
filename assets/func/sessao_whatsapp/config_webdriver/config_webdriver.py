import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from assets.func.sessao_whatsapp.uteis.definir_pasta import definir_pasta

driver = None
navegador_aberto = False

def config_webdriver(headless, client):
    global driver, navegador_aberto

    if driver is not None:
        driver.quit()
    
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'eager'
    if headless:
        options.add_argument("--headless=new")  # Usa um modo mais estavel do headless
    options.add_argument("--disable-gpu")  # Corrige problemas graficos em headless
    options.add_argument("--no-sandbox")  # Evita problemas de permissões
    options.add_argument("--disable-dev-shm-usage")  # Evita uso excessivo de memória compartilhada
    options.add_argument(f"user-data-dir={definir_pasta(client)}")

    driver = webdriver.Chrome(options=options)
    driver.get("https://web.whatsapp.com")

    if driver is not None:
        navegador_aberto = True

    

def check_login(existe_login=False):
    global driver
    if existe_login:
        try:       
            logado = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
            )
            if logado:
                return True
            else:
                print("erro ao checar login")
        except:
            qr_code = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//canvas[@aria-label='Scan this QR code to link a device!']"))
            )
            print("Elemento encontrado:", qr_code)
            return False
    else:
        try:
             # Aguarda até que o elemento <canvas> com o atributo 'aria-label' correto esteja presente
            qr_code = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//canvas[@aria-label='Scan this QR code to link a device!']"))
            )
            #print("Elemento encontrado:", qr_code)
            return False
        except:
            logado = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))            
            )
            if logado:
                return True
            else:
                print("erro ao checar login")


def enviar_mensagem(numero, mensagem, primeira_execucao=[True], nome_arquivo=[None]):
    global driver 
    try:
        # Define o nome do arquivo na primeira execução
        if primeira_execucao[0]:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            nome_arquivo[0] = f"{timestamp}"  # Define o nome do arquivo
            primeira_execucao[0] = False  # Atualiza a flag
        
        # Busca pelo contato ou número
        search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
        search_box.click()
        search_box.clear()
        search_box.send_keys(str(numero) + Keys.ENTER)
        time.sleep(2)  # Aguarda a tela do contato carregar

        # Digita e envia a mensagem
        msg_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
        msg_box.click()
        msg_box.send_keys(mensagem + Keys.ENTER)
        time.sleep(5)
        

        # Registra o sucesso no arquivo
        with open(f"enviados_{nome_arquivo[0]}.txt", "a", encoding="utf-8") as f:
            f.write(f"{numero}: {mensagem}\n")
    
            
        print(f"Mensagem enviada para {numero}\n{mensagem}")
    except Exception as e:
        # Registra o erro no arquivo
        with open(f"erros_{nome_arquivo[0]}.txt", "a", encoding="utf-8") as f:
            f.write(f"Erro ao enviar para {numero}: {str(e)}\n")
        
        print(f"Erro ao enviar para {numero}")
    
    time.sleep(2)
