import tkinter as tk
from tkinter import ttk

from assets.func.mensagem.montar_msg.montar_msg import montar_msg
from assets.func.mensagem.definir_origem.definir_origem import definir_origem

from assets.func.planilha.info_planilha.info_planilha import listar_paginas, selecionar_arquivo

lista_paginas = []

def tela_mensagem(raiz_principal):
    global combo_frequencia, botao_agendar,  botao_enviar, lista_paginas
    
    mensagem_raiz = tk.Frame(raiz_principal) 
    frame_checkbuttons = tk.Frame(mensagem_raiz)
    frame_checkbuttons.pack(pady=(15,5))
        
    frame_escolher_pagina = tk.Frame(mensagem_raiz)
    frame_escolher_pagina.pack(pady=5)


    def escolher_planilha():
        global lista_paginas  # Torna a lista global para ser acessada dentro da função
        lista_paginas = listar_paginas()  # Preenche a lista com as páginas da planilha
        if lista_paginas:            
            escolher_pagina_planilha['values'] = lista_paginas  # Atualiza os valores no combobox
            escolher_pagina_planilha.current(0)
            escolher_pagina_planilha.pack(side=tk.LEFT, padx=5)
        raiz_principal.update_idletasks()
        raiz_principal.geometry(f"{raiz_principal.winfo_reqwidth()}x{raiz_principal.winfo_reqheight()}")
    
    tk.Label(frame_escolher_pagina, text="Abrir arquivo Excel:").pack(pady=5)
    escolher_pagina_planilha = ttk.Combobox(frame_escolher_pagina)
    escolher_pagina_planilha.pack_forget()

    botao_abrir_excel = tk.Button(
        frame_escolher_pagina,
        text="Abrir",
        command=lambda: [selecionar_arquivo(),escolher_planilha()]                       
        )
    botao_abrir_excel.pack(padx=5, pady=5)

    tk.Label(mensagem_raiz, text="Mensagem:").pack(pady=5)
    entrada_mensagem = tk.Text(mensagem_raiz, width=40, height=10)
    entrada_mensagem.pack(pady=5)

    frame_botoes = tk.Frame(mensagem_raiz)
    frame_botoes.pack(side="bottom",  pady=(10,20))

    botao_enviar = tk.Button(
        frame_botoes,
        text="enviar",
        command=lambda: montar_msg( 
            definir_origem(            
                escolher_pagina_planilha.current()),               
                entrada_mensagem.get('1.0', tk.END)           
        ))
    botao_enviar.pack(padx=5, pady=5)
    

    return mensagem_raiz