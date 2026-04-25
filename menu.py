from time import sleep
from cliente import Cliente
from layout import criar_menu, limpar, perguntar, publicidade, titulo
from login_sign_in import criar_user, verificar_user
from save_load import carregar_save
from random import randint

ENTER = "   \nPressione ENTER para continuar..."

cliente_logado = None
lista_clientes = carregar_save(caminho="cliente", obj=Cliente)
lista_estabelecimentos = carregar_save(caminho="estabelecimento", obj=Cliente)

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

def menu_app():
    limpar()
    print(titulo("D A S H"))
    print(titulo("1 - Cliente | 2 - Estabelecimento | 0 - Sair", sem_linha=True))

    print()
    estabelecimentos = [ # para testes porque ainda nao se tem a class estabelecimento
        {"nome": "Taberna do Zé", "horario": "12:00 - 23:00", "telefone": "123-456-789"},
        {"nome": "Farmácia Central", "horario": "08:00 - 20:00", "telefone": "987-654-321"},
        {"nome": "Gym Fit", "horario": "07:00 - 22:00", "telefone": "555-555-555"},
        {"nome": "Gym Fit", "horario": "07:00 - 22:00", "telefone": "555-555-555"},
        {"nome": "Taberna do Zé", "horario": "12:00 - 23:00", "telefone": "123-456-789"},
        {"nome": "Farmácia Central", "horario": "08:00 - 20:00", "telefone": "987-654-321"},
        {"nome": "Gym Fit", "horario": "07:00 - 22:00", "telefone": "555-555-555"},
        {"nome": "Gym Fit", "horario": "07:00 - 22:00", "telefone": "555-555-555"},
        {"nome": "Taberna do Zé", "horario": "12:00 - 23:00", "telefone": "123-456-789"},
        {"nome": "Farmácia Central", "horario": "08:00 - 20:00", "telefone": "987-654-321"},
        {"nome": "Gym Fit", "horario": "07:00 - 22:00", "telefone": "555-555-555"},
    ]
    for est in range(1, len(estabelecimentos), 4):
        publicidade(estabelecimentos[est:est+4]) 
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

def menu_cliente(): # user profile
    pass

def menu_estabelecimento(): # para ver o estabelecimento e poder fazer a marcação
    pass

def menu_adicionar_estabelecimento(): # para criar um estabelimento
    pass


if __name__ == "__main__":
    menu_app()