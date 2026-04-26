from cliente import Cliente
from estabelecimento import Estabelecimento

from time import sleep
from random import randint

from layout import criar_menu, limpar, mostra_info, perguntar, publicidade, titulo

from login_sign_in import criar_user, verificar_user

from save_load import carregar_save, guardar_dados



ENTER = "   \nPressione ENTER para continuar..."
ENTER_VOLTAR = "   \nPressione ENTER para voltar ao menu..."

cliente_logado = None
lista_clientes = carregar_save(caminho="cliente", obj=Cliente)
lista_estabelecimentos = carregar_save(caminho="estabelecimento", obj=Estabelecimento)

mostrar_menu = 0

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

        resposta, obj = verificar_user(nome=resultados[0], password=resultados[1], lista_clientes=lista_clientes)

        if resposta:
            cliente_logado = obj
            print("Login bem sucedido!")
            sleep(1.5) 
            menu_app()
            break
        print(resposta)
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
            menu_app()
            break
        input(ENTER)

def menu_app():
    global mostrar_menu
    while True:
        if mostrar_menu == 0:
            limpar()
            print(titulo("D A S H"))
            print(titulo("1 - Cliente | 2 - Estabelecimento | 3 - Adicionar Estabelecimento | 0 - Sair", sem_linha=True))

            print()
            if lista_estabelecimentos:
                for est in range(1, len(lista_estabelecimentos), 4):
                    publicidade(lista_estabelecimentos[est:est+4]) 
                    i = randint(0, 3)

                    if i == 0:   
                        a = titulo("💸 10% DE DESCONTO PARA NOVOS CLIENTES", sem_linha=True)
                        b =titulo("USE O CÓDIGO: DASH2026", sem_linha=True)
                        print(titulo( a + "\n" +b, tipo_linha="-"))
                        
                    elif i == 1:
                        a = titulo("⭐ TORNA-TE MEMBRO PREMIUM ⭐", sem_linha=True)
                        b =titulo("ACESSOS EXCLUSIVOS E TAXA DE ENTREGA GRÁTIS", sem_linha=True)
                        print(titulo( a + "\n" +b, tipo_linha="-"))
                    
                    elif i == 2:
                        a = titulo("📢 QUER VER O SEU NEGÓCIO AQUI?", sem_linha=True)
                        b =titulo("CONTACTE-NOS EM DASH.SUPPORT@EMAIL.COM", sem_linha=True)
                        print(titulo( a + "\n" +b, tipo_linha="-"))
                    
                    elif i == 3:
                        a = titulo("🍕 NOITE DE PIZZA? 🍕", sem_linha=True)
                        b =titulo("PEÇA JÁ E GANHE UMA BEBIDA DE OFERTA", sem_linha=True)
                        print(titulo( a + "\n" +b, tipo_linha="-"))
            
            else:
                print(titulo("Nenhum estabelecimento disponível no momento.", sem_linha=True))
                print(titulo("Volte mais tarde para descobrir as nossas ofertas!", sem_linha=True))
                print(titulo("Ou adicione o seu estabelecimento para aparecer aqui!", sem_linha=True))

        
        mostrar_menu = 1
        res = perguntar([["  Escolha uma opção", 0, 3]], tipo=int, titulo="D A S H")

        if res[0] == 1:
            menu_cliente()
        elif res[0] == 2:
            menu_estabelecimento()
        elif res[0] == 3:
            menu_adicionar_estabelecimento()
        elif res[0] == 0:
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

def menu_cliente(): # user profile
    global mostrar_menu
    while True:
        limpar()
        config = [
            {
                "sub": "P R O F I L E",
                "opcoes": [
                    "Ver perfil",
                    "Editar perfil",
                ],
            },
            {
                "sub": "M A R C A Ç Ã O",
                "opcoes": [
                    "Ver marcações"
                ],
            }
        ]
        
        res = criar_menu(menu_config=config)

        if res == 1:
            menu_profile()
        elif res == 2:
            res = perguntar([["  Novo nome", 3, 20], ["  Nova password", 8, 20]], tipo=str, titulo="E D I T A R  P R O F I L E", vazio=True)
            if res[0]:
                cliente_logado.nome = res[0]
            if res[1]:
                cliente_logado.password = res[1]
            
            guardar_dados(caminho="cliente", lista=lista_clientes)
            print("Perfil atualizado com sucesso!")
            input(ENTER)
        elif res == 3:
            pass # Ver marcações
        elif res == 0:
            mostrar_menu = 0
            break
        else:
            print("Opção inválida, tente novamente.")

def menu_estabelecimento(): # para ver o estabelecimento e poder fazer a marcação
    pass

def menu_adicionar_estabelecimento(): # para criar um estabelimento
    pass

def menu_profile():
    texto = f"""
    NOME: {cliente_logado.nome}
    """
    mostra_info(texto)
    input(ENTER_VOLTAR)

if __name__ == "__main__":
    menu()