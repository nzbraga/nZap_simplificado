import re
import sys
import time
import keyboard
from assets.func.uteis.popUp import popUp
from assets.func.sessao_whatsapp.config_webdriver.config_webdriver import enviar_mensagem
import tkinter as tk
from tkinter import messagebox

interromper = False

def substituir_variaveis(mensagem, contato):
    """Substitui palavras iniciadas com @ pelos valores correspondentes do dicionário contato."""
    def substituir(match):
        chave = match.group(1).lower()  # Converte a chave para minúsculas
        if chave not in contato:
            popUp(f"Erro: chave '{chave}' não encontrada para o contato {contato.get('nome', 'Desconhecido')}.")
            raise ValueError(f"Erro: chave '{chave}' não encontrada para o contato {contato.get('nome', 'Desconhecido')}.")
        return contato[chave]

    try:
        return re.sub(r"@(\w+)", substituir, mensagem)
    except ValueError as e:
        print(e)
        return None  # Retorna None para indicar erro


def montar_msg(contatos, mensagem):
    if not contatos:
        popUp("Nenhum contato selecionado.")
        return

    if not mensagem or not mensagem.strip():
        popUp("Mensagem vazia.")
        return
    
    contador = 0  # Contador local para controle de envios
    
    for contato in contatos:
        time.sleep(2)
        if keyboard.is_pressed("esc"):  # Checagem a cada iteração
            print("\n🛑 Envio interrompido pelo usuário!")
            return  # Sai imediatamente do loop
        
        mensagem_personalizada = substituir_variaveis(mensagem, contato)
        if mensagem_personalizada is None:
            popUp(f"Erro ao processar mensagem para {contato.get('nome', 'Desconhecido')}.")
            return  # Interrompe a execução se houver erro
        
        try: 
            mensagem_completa = f"{mensagem_personalizada}"        
            enviar_mensagem(contato["contato"], mensagem_completa)
            contador += 1
        except:
            popUp("Número não encontrado\nVerifique se o campo 'contato' existe\n\nA mensagem será enviada para o número no campo 'contato'")
        
        if contador >= 5:
            resposta = messagebox.askyesno("Confirmação", "Foram enviadas 5 mensagens, deseja continuar?")
            if resposta:
                contador = 0  # Reseta o contador para mais 5 envios
            else:
                return
