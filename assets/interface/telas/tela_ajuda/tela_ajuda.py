import tkinter as tk
import json
import os

from assets.func.uteis.popUp import popUp

CONFIG_FILE = "config.json"

def carregar_destinatario():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
                return data.get("destinatario", "contato")
            except json.JSONDecodeError:
                return "contato"
    return "contato"

def salvar_destinatario(novo_destinatario, label_dest, label_entrada, entrada_destinatario):
    with open(CONFIG_FILE, "w", encoding="utf-8") as file:
        json.dump({"destinatario": novo_destinatario}, file, indent=4)
    label_dest.config(text=f"> A mensagem será enviada para o campo '{novo_destinatario}' do arquivo Excel")
    label_entrada.config( text=f"Deseja mudar o campo {novo_destinatario}? ")
    entrada_destinatario.delete(0, tk.END)

def tela_ajuda(raiz_principal):
    destinatario = carregar_destinatario()
    frame_ajuda = tk.Frame(raiz_principal)

    tk.Label(frame_ajuda, text="DICAS!", font=("Arial", 10)).pack(pady=5)
    tk.Label(frame_ajuda, text="> Use @ para marcar campos da planilha\nex.: @nome (exibirá o conteúdo do campo nome na msg)\nassim como qualquer outro campo existente na planilha", font=("Arial", 10, "italic")).pack(pady=5)
    tk.Label(frame_ajuda, text="> Confira os dados da planilha antes de enviar as mensagens", font=("Arial", 10, "italic")).pack(pady=5)

    label_dest = tk.Label(frame_ajuda, text=f"> A mensagem será enviada para o campo '{destinatario}' do arquivo Excel", font=("Arial", 10), bg="light gray")
    label_dest.pack(pady=5)
    label_entrada =tk.Label(frame_ajuda, text=f"Deseja mudar o campo {destinatario}? ")
    label_entrada.pack(pady=5)

    entrada_destinatario = tk.Entry(frame_ajuda, width=20)
    #entrada_destinatario.insert(0, destinatario)
    entrada_destinatario.pack(pady=5)

    def atualizar_destinatario():
        novo_destinatario = entrada_destinatario.get().strip()
        if novo_destinatario:
            salvar_destinatario(novo_destinatario, label_dest, label_entrada, entrada_destinatario)
            popUp("Salvo com sucesso!")

    botao_mudar_destinatario = tk.Button(
        frame_ajuda,
        text="Salvar",
        command=atualizar_destinatario
    )
    botao_mudar_destinatario.pack(padx=5, pady=(5,25))

    raiz_principal.update_idletasks()
    raiz_principal.geometry("")

    return frame_ajuda
