import json
from pathlib import Path

# Define o caminho seguro para armazenar arquivos de sessão
base_dir = Path.home() / "nZap" 
base_dir.mkdir(parents=True, exist_ok=True)  # Garante que a pasta exista
caminho_arquivo = base_dir / "sessao" / ".sessao.json"

def sessao_id():
    
    return 'sessao_teste_id'

def sessao_nome():
    return 'versao_teste'