from time import sleep
from cliente import Cliente
from layout import criar_menu, limpar, perguntar
from login_sign_in import criar_user, verificar_user
from save_load import carregar_save

ENTER = "   \nPressione ENTER para continuar..."

cliente_logado = None
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
    global cliente_logado
    while True:
        limpar()

        config = [
            ["  Nome", 3, 20],             # Min 3, Max 20 caracteres
            ["  Password", 8, 20],         # Min 8, Max 20 (valor)
        ]

        resultados = perguntar(config, tipo=str, titulo="L O G I N")

        resposta = verificar_user(resultados[0], resultados[1])

        if resposta is object:
            cliente_logado = resposta
            print("Login bem sucedido!")
            sleep(1.5) 
            break
        input(ENTER)

def menu_criar_conta():
    while True:
        limpar()
        config = [
            ["  Nome", 3, 20],             # Min 3, Max 20 caracteres
            ["  Password", 8, 20],         # Min 8, Max 20 (valor)
        ]

        resultados = perguntar(config, tipo=str, titulo="S I G N  -  I N")

        resultado = criar_user(lista_clientes=lista_clientes, nome=resultados[0], password=resultados[1])
        
        if resultado:
            print(" Conta criada com sucesso!")
            sleep(1.5)  
            break
        input(ENTER)

if __name__ == "__main__":
    menu()