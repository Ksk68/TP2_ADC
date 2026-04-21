import os


# Erros default
ERRO_NUMERO = "Caracter invalido porfavor insira numeros"

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