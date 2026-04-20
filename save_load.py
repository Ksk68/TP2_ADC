import json
import os 

FICHEIRO_CLIENTE = "save/clientes.json"
FICHEIRO_ESTABELECIMENTO = "save/estabelecimentos.json"

def guardar_dados(lista: list, caminho: str): # Recebe a lista por argumento
    if caminho == "cliente":
        caminho = FICHEIRO_CLIENTE
    elif caminho == "estabelecimento":
        caminho = FICHEIRO_ESTABELECIMENTO

    pasta = os.path.dirname(caminho)
    
    if pasta and not os.path.exists(pasta):
        os.makedirs(pasta, exist_ok=True)

    dados_para_salvar = [obj.para_dicionario() for obj in lista]
    
    try:
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(dados_para_salvar, f, indent=4)
    except Exception as e:
        print(f"\n[Erro ao guardar: {e}]")

def carregar_save(ficheiro: str, obj: object):
    """Carrega os clientes e reconverte-os em objetos Cliente."""

    if ficheiro == "cliente":
        ficheiro = FICHEIRO_CLIENTE
    elif ficheiro == "estabelecimento":
        ficheiro = FICHEIRO_ESTABELECIMENTO

    if os.path.exists(ficheiro):
        with open(ficheiro, "r", encoding="utf-8") as f:
            dados = json.load(f)
            return [obj(**item) for item in dados] # 'nome': "Raul" --> nome="Raul"
    return []


