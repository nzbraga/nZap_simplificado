import tkinter as tk

def tela_ajuda(raiz_principal):

    frame_inicial = tk.Frame(raiz_principal)      

    tk.Label(frame_inicial, text="> A mensagem sera enviada para\no campo 'Contato' do arquivo excel", font=("Arial", 10, "italic")).pack(pady=5)
    tk.Label(frame_inicial, text="> Use @ parar marcar campos da planilha\nex.: @nome\n(exibira o conteudo do campo nome na msg)\n assim como qualquer outro campo existente na planilha", font=("Arial", 10, "italic")).pack(pady=5)
    tk.Label(frame_inicial, text="> Confira os dados da planilha antes de enviar as mensagens", font=("Arial", 10, "italic")).pack(pady=5)
       
    raiz_principal.update_idletasks()  
    raiz_principal.geometry("")  


    return frame_inicial
