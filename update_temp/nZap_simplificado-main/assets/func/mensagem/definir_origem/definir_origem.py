from assets.func.uteis.popUp import popUp
from assets.func.planilha.info_planilha.info_planilha import info_planilha
from assets.func.sessao.sessao import sessao_id

usuario_id = sessao_id()
dados_contatos = []

def definir_origem(pagina_excel):
    global dados_contatos    

    try:
        sheet = info_planilha(pagina_excel)
        if not sheet:
            return []
    except Exception:
        popUp('Erro ao ler planilha')
        return []

    try:
        # Captura os nomes das colunas em minúsculas
        header = [cell.value.lower() for cell in sheet[1]]  
        dados_contatos = []

        for row in sheet.iter_rows(min_row=2, values_only=True):
            row_dict = dict(zip(header, row))
            
            if row_dict.get("nome") is None or row_dict["nome"] == "":
                break

            dados_contatos.append(row_dict)
    except Exception:
        popUp("Erro ao processar os dados da planilha")
        return []

    return dados_contatos
