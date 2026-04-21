from cliente import Cliente
from layout import criar_menu, limpar, perguntar
from login_sign_in import criar_user, verificar_user
from save_load import carregar_save

ENTER = "\nPressione ENTER para continuar..."


lista_clientes = carregar_save(caminho="cliente", obj=Cliente)

def menu():
    while True:

        config = [
            {
                "sub": "L O G I N",
                "opcoes": [
                    "Fazer login",
                    "Criar conta",
                ],
            }
        ]
        
        res = criar_menu(menu_config=config)

        if res == 1:
            menu_login()
        elif res == 2:
            menu_criar_conta()
        elif res == 0:
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

def menu_login():
    limpar()

    config = [
        ["  Nome", 3, 20],             # Min 3, Max 20 caracteres
        ["  Password", 8, 20],         # Min 8, Max 20 (valor)
    ]

    resultados = perguntar(config, tipo=str, titulo="L O G I N")

    verificar_user(resultados[0], resultados[1])
    input(ENTER)

def menu_criar_conta():
    limpar()
    
    config = [
        ["  Nome", 3, 20],             # Min 3, Max 20 caracteres
        ["  Password", 8, 20],         # Min 8, Max 20 (valor)
    ]

    resultados = perguntar(config, tipo=str, titulo="S I G N  -  I N")

    criar_user(lista_clientes=lista_clientes, nome=resultados[0], password=resultados[1])

if __name__ == "__main__":
    menu()