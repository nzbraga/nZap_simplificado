import os
import subprocess
import sys

from assets.interface.telas.tela_principal.tela_principal import mostrar_tela, frame1

def verificar_atualizacoes():
    """Roda o updater em segundo plano para evitar travamento."""
    if sys.platform == "win32":
        subprocess.Popen(["python", "updater.py"], creationflags=subprocess.CREATE_NO_WINDOW)
    else:
        subprocess.Popen(["python", "updater.py"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def main():
    verificar_atualizacoes()
    mostrar_tela(frame1)

if __name__ == "__main__":
    main()
