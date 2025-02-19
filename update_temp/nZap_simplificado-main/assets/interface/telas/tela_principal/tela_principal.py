import tkinter as tk
from tkinter import Menu

from assets.interface.telas.tela_inicial.tela_inicial import criar_tela_inicial
from assets.interface.telas.tela_mensagem.tela_mensagem import tela_mensagem
from assets.interface.telas.tela_ajuda.tela_ajuda import tela_ajuda

def mostrar_tela(frame):

    frame.update_idletasks()  # Atualiza as dimensões do frame
    largura = frame.winfo_reqwidth()
    altura = frame.winfo_reqheight()
    
    raiz_principal.geometry(f"{largura}x{altura}")  
    frame.tkraise()


# Criar janela principal
raiz_principal = tk.Tk()
raiz_principal.title("nZap -  Bem vindo!")
raiz_principal.grid_rowconfigure(0, weight=1)
raiz_principal.grid_columnconfigure(0, weight=1)
raiz_principal.resizable(False, False)

raiz_principal.minsize(500, 250)

# Criar frames para cada "tela"

frame1 = criar_tela_inicial(raiz_principal)
frame2 = tela_mensagem(raiz_principal)
frame3 = tela_ajuda(raiz_principal)

for frame in (frame1, frame2, frame3):
    frame.grid(row=0, column=0, sticky="nsew")

# Criar Menu
menu_bar = Menu(raiz_principal)
raiz_principal.config(menu=menu_bar)

menu_bar.add_command(label="Conectar", command=lambda: mostrar_tela(frame1))
menu_bar.add_command(label="Mensagem", command=lambda: mostrar_tela(frame2))
menu_bar.add_command(label="Ajuda", command=lambda: mostrar_tela(frame3))

# Mostrar frame inicial

mostrar_tela(frame1)

raiz_principal.mainloop()