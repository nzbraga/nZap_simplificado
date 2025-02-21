import os
import sys
import time
import requests
import zipfile
import shutil

# Configurações
GITHUB_REPO = "nzbraga/nZap_simplificado"
BRANCH = "main"  # Ou outra branch específica
APP_EXECUTAVEL = "app.exe"  # Nome do executável gerado pelo PyInstaller
TEMP_FOLDER = "update_temp"

def baixar_atualizacao():
    print(f"Versão atual do app: {sys.version}")
    print("""Baixa a versão mais recente do app do GitHub""")
    url = f"https://github.com/{GITHUB_REPO}/archive/{BRANCH}.zip"
    zip_path = os.path.join(TEMP_FOLDER, "update.zip")

    os.makedirs(TEMP_FOLDER, exist_ok=True)
    print(f"Baixando atualização de {url}...")
    
    with requests.get(url, stream=True) as r:
        with open(zip_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    print("Download concluído!")
    return zip_path

def extrair_atualizacao(zip_path):
    print("""Extrai os arquivos baixados""")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(TEMP_FOLDER)
    print("Arquivos extraídos!")

def substituir_arquivos():
    print("""Substitui os arquivos do app antigo pelos novos""")
    pasta_extraida = os.path.join(TEMP_FOLDER, f"repositorio-{BRANCH}")
    
    for item in os.listdir(pasta_extraida):
        src = os.path.join(pasta_extraida, item)
        dst = os.path.join(os.getcwd(), item)
        
        if os.path.isdir(src):
            if os.path.exists(dst):
                shutil.rmtree(dst)
            shutil.copytree(src, dst)
        else:
            shutil.copy2(src, dst)

    print("Arquivos atualizados!")

def reiniciar_app():
    print("""Reinicia o aplicativo atualizado""")
    print("Reiniciando app...")
    os.execv(APP_EXECUTAVEL, [APP_EXECUTAVEL])

def atualizar():
    """Executa todo o processo de atualização"""
    print("Verificando atualizações...")
    zip_path = baixar_atualizacao()
    extrair_atualizacao(zip_path)
    substituir_arquivos()
    reiniciar_app()

if __name__ == "__main__":
    atualizar()
