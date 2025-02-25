import json
import tkinter as tk
from pathlib import Path
from tkinter import ttk

from assets.interface.telas.tela_enviar.uteis.opcoes_frequencia import *
from assets.func.planilha.info_planilha.info_planilha import listar_paginas, selecionar_arquivo, arquivo_selecionado
from assets.func.mensagem.listar_mensagens.listar_mensagens import listar_mensagens
from assets.interface.telas.tela_enviar.uteis.obter_mensagem import obter_mensagem
from assets.func.mensagem.montar_msg.montar_msg import montar_msg
from assets.func.mensagem.definir_origem.definir_origem import definir_origem

#from assets.interface.telas.tela_enviar.frame_frequencia import tela_frequencia
from assets.interface.telas.tela_enviar.uteis.salvar_mensagem import salvar_mensagem
from assets.func.sessao.sessao import sessao_id

usuario_id = sessao_id()
lista_paginas = []


def atualizar_lista_mensagens():
    """Atualiza a lista de mensagens disponíveis no Combobox."""
    escolher_mensagem["values"] = listar_mensagens(usuario_id)

def salvar_e_atualizar_mensagem():
    """Salva a mensagem e atualiza o Combobox com as mensagens disponíveis."""
    salvar_mensagem(usuario_id, entrada_mensagem.get("1.0", tk.END).strip())
    atualizar_lista_mensagens()

def tela_enviar(raiz_principal):
    global lista_paginas, entrada_mensagem, enviar_agenda, enviar_excel, escolher_pagina_planilha, escolher_mensagem

    janela_principal = raiz_principal.winfo_toplevel()
    janela_principal.geometry(f"{janela_principal.winfo_reqwidth()}x{janela_principal.winfo_reqheight()}")
    
    mensagem_raiz = tk.Frame(raiz_principal) 
    frame_checkbuttons = tk.Frame(mensagem_raiz)
    frame_checkbuttons.pack(pady=(15,5))
    
    frame_escolher_pagina = tk.Frame(mensagem_raiz)
    frame_escolher_pagina.pack(pady=5)
    
    def alternar_excel():
        global lista_paginas, arquivo_selecionado  
        
        if not arquivo_selecionado:
            selecionar_arquivo()
            
        lista_paginas = listar_paginas()

        if lista_paginas:  
            escolher_pagina_planilha['values'] = lista_paginas
            escolher_pagina_planilha.current(0)
        else:
            print("Nenhuma planilha foi selecionada ou erro ao carregar páginas.")
        
        janela_principal.update_idletasks()
        janela_principal.geometry(f"{raiz_principal.winfo_reqwidth()}x{raiz_principal.winfo_reqheight()}")           

    escolher_pagina_planilha = ttk.Combobox(frame_escolher_pagina, width=30)
    escolher_pagina_planilha.pack(pady=5)

    botao_abrir_excel = tk.Button(
        frame_escolher_pagina,
        text="Abrir Excel",
        command=alternar_excel
    )
    botao_abrir_excel.pack(pady=5)


    frame_destinatario = tk.Frame(frame_escolher_pagina)
    frame_destinatario.pack(pady=5)

    tk.Label(frame_destinatario, text="Escolher campo\ncom contato do usuario").pack(pady=5)

    entrada_destinatario = tk.Text(frame_destinatario, width=15, height=1)
    entrada_destinatario.insert('1.0' , 'contato')
    entrada_destinatario.pack(pady=5)

    tk.Label(mensagem_raiz, text="Mensagem:").pack(pady=5)
    
    frame_escolher_mensagem = tk.Frame(mensagem_raiz)
    frame_escolher_mensagem.pack(pady=5)

    escolher_mensagem = ttk.Combobox(frame_escolher_mensagem, values=listar_mensagens(usuario_id), width=30)
    escolher_mensagem.pack(side=tk.LEFT)

    botao_escolher_mensagem = tk.Button(
        frame_escolher_mensagem,
        text="Selecionar",
        command=lambda: obter_mensagem(
            usuario_id,
            escolher_mensagem.current(),
            entrada_mensagem
        )
    )
    botao_escolher_mensagem.pack(padx=5)
    entrada_mensagem = tk.Text(mensagem_raiz, width=50, height=10)
    entrada_mensagem.pack(pady=5)

    botao_enviar = tk.Button(
    mensagem_raiz,
    text="Enviar",
    command=lambda: montar_msg( 
        definir_origem(            
            escolher_pagina_planilha.current()
            ),
            entrada_mensagem.get('1.0', tk.END),
            entrada_destinatario.get('1.0', tk.END).strip()            
    ))
    botao_enviar.pack(pady=5)

    """
    frame_frequencia = tela_frequencia(mensagem_raiz)
    frame_frequencia.pack(pady=5)
    """
    
    return mensagem_raiz
