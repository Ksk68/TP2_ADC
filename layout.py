import os


# Erros default
ERRO_NUMERO = "Caracter invalido porfavor insira numeros"
ERRO_FLOAT = "Insira um número decimal (ex: 10.50)"

TITULO = 'D A S H'
num_opcao = 3

def criar_menu(menu_config: list, tamanho: int=76, sem_num: bool=False) -> int:
    while True:
        limpar()
        linha = "━"*tamanho
        titulo_texto = f"{TITULO:^{tamanho}}"
        
        menu_display = f"{linha}\n{titulo_texto}\n{linha}\n\n"
        
        num_opcoes = 1
        largura_sub = 28 

        for bloco in menu_config:
            sub = bloco["sub"]
            opcoes = bloco["opcoes"]
            
            for j in range(len(opcoes)):
                if sem_num:
                    num = "- "
                else:
                    num = f"[{num_opcoes}]"
                    
                if j == 0:
                    menu_display += f"    {sub:<{largura_sub}} {num} {opcoes[j]}\n"
                else:
                    menu_display += f"    {' ':<{largura_sub}} {num} {opcoes[j]}\n"
                
                num_opcoes += 1
            menu_display += "\n" 

        menu_display += f"    {'V O L T A R':<{largura_sub}} [0] Sair\n\n"
        menu_display += linha

        print(menu_display)

        try:
            if sem_num:
                res = input(": ")
            else:
                res = int(input(": "))
            return res
        except ValueError:
            print(ERRO_NUMERO)
            input("Pressione ENTER para tentar de novo...")

def limpar() -> None:
    """
        Limpa a comand line
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def perguntar(perguntas_config: list, tipo: object = str, exclusoes: list = None, tamanho: int = 76, titulo: str = "P E R G U N T A S"):
    """
    perguntas_config: Lista de listas no formato [["Pergunta", min, max], ...]
    tipo: Tipo de variável (str, int, float).
    exclusoes: Lista de valores que não são permitidos.
    tamanho: Largura do layout.
    titulo: Título do layout.
    """
    exclusoes = exclusoes or []

    linha = "━" * tamanho
    print(f"{linha}\n{titulo:^{tamanho}}\n{linha}")

    respostas_finais = []

    for item in perguntas_config:

        texto_pergunta = item[0]
        if len(item) > 1:
            min_v = item[1]
            if len(item) > 2:
                max_v = item[2]
            else:
                max_v = None
        else:
            min_v = None
            max_v = None

        while True:
            try:
                res = input(f"{texto_pergunta}: ").strip()

                if not res:
                    print("Erro: A entrada não pode estar vazia.")
                    continue

                valor_convertido = tipo(res)

                if valor_convertido in exclusoes:
                    print(f"Erro: O valor '{valor_convertido}' não é permitido.")
                    continue

                # Lógica de validação de limites
                if tipo is str:
                    dado = len(res) 
                else:
                    dado = valor_convertido
                
                if tipo is str:
                    termo = "caracteres" 
                else:
                    termo = "valor"

                if min_v is not None and dado < min_v:
                    print(f"Erro: Mínimo de {min_v} {termo}.")
                    continue
                if max_v is not None and dado > max_v:
                    print(f"Erro: Máximo de {max_v} {termo}.")
                    continue

                respostas_finais.append(valor_convertido)
                break # Sai do while e vai para a próxima pergunta

            except ValueError:
                print(f"Erro: Entrada inválida. Esperado {tipo.__name__}.")

    return respostas_finais

def titulo(texto: str, tamanho: int=76, sem_linha: bool=False, tipo_linha: str="━") -> None:
    linha = tipo_linha * tamanho
    if sem_linha:
        return f"{texto:^{tamanho}}"
    else:
        return f"{linha}\n{texto:^{tamanho}}\n{linha}"

def publicidade(list_objetos: list, largura_quadrado: int = 30, tamanho: int = 76) -> None:
    global num_opcao
    """
    Exibe quadrados centrados no ecrã, mas com texto interno alinhado à esquerda.
    """
    # Caracteres de borda
    topo = "╔" + "═" * (largura_quadrado - 2) + "╗"
    base = "╚" + "═" * (largura_quadrado - 2) + "╝"
    espaco_entre = "   "

    largura_interna = largura_quadrado - 2 # Descontando as duas bordas ║


    for i in range(0, len(list_objetos), 2):
        par = list_objetos[i:i+2]
        
        item1 = par[0]

        
        celula_telefone1   = f"║ {f'[{item1['telefone']}]':<{largura_interna-1}}║"
        celula_nome1 = f"║ {f"{item1['nome']} [{num_opcao}]"[:largura_interna-2]:<{largura_interna-1}}║"
        celula_hora1 = f"║ {item1['horario'][:largura_interna-2]:<{largura_interna-1}}║"

        if len(par) == 2:
            num_opcao += 1
            item2 = par[1]
            celula_nome2 = f"║ {f"{item2['nome']} [{num_opcao}]"[:largura_interna-2]:<{largura_interna-1}}║"
            celula_hora2 = f"║ {item2['horario'][:largura_interna-2]:<{largura_interna-1}}║"
            celula_telefone2   = f"║ {f'[{item2['telefone']}]':<{largura_interna-1}}║"

            l_topo = f"{topo}{espaco_entre}{topo}"
            l_telefone = f"{celula_telefone1}{espaco_entre}{celula_telefone2}"
            l_nome = f"{celula_nome1}{espaco_entre}{celula_nome2}"
            l_hora = f"{celula_hora1}{espaco_entre}{celula_hora2}"
            l_base = f"{base}{espaco_entre}{base}"
        else:
            l_topo = topo
            l_telefone   = celula_telefone1
            l_nome = celula_nome1
            l_hora = celula_hora1
            l_base = base
            tamanho = tamanho // 2 + 5

        print(f"{l_topo:^{tamanho}}")
        print(f"{l_nome:^{tamanho}}")
        print(f"{l_hora:^{tamanho}}")
        print(f"{l_telefone:^{tamanho}}")
        print(f"{l_base:^{tamanho}}")
        print() 

        num_opcao += 1