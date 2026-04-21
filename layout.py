import os


# Erros default
ERRO_NUMERO = "Caracter invalido porfavor insira numeros"
ERRO_FLOAT = "Insira um número decimal (ex: 10.50)"

TITULO = 'D A S H'

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
                dado = len(res) if tipo is str else valor_convertido
                termo = "caracteres" if tipo is str else "valor"

                if min_v is not None and dado < min_v:
                    print(f"Erro: Mínimo de {min_v} {termo}.")
                    continue
                if max_v is not None and dado > max_v:
                    print(f"Erro: Máximo de {max_v} {termo}.")
                    continue

                respostas_finais.append(valor_convertido)
                break # Sai do while e vai para a próxima pergunta do for

            except ValueError:
                print(f"Erro: Entrada inválida. Esperado {tipo.__name__}.")

    return respostas_finais