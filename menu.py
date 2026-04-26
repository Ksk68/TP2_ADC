from cliente import Cliente
from estabelecimento import Estabelecimento
from marcacao import Marcacao

from time import sleep
from random import randint

from layout import criar_menu, limpar, mostra_info, perguntar, publicidade, titulo, lista_opcoes

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
    global cliente_logado, lista_clientes
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
            sleep(1) 
            menu_app()
            break
        print(obj)
        input(ENTER)

def menu_criar_conta():
    while True:
        limpar()
        config = [
            ["  Nome", 3, 20],             # Min 3, Max 20 caracteres
            ["  Password", 8, 20],         # Min 8, Max 20 (valor)
            ["  Morada", 5, 100],           # Min 5, Max 100 caracteres
            ["  Telefone", 9, 9]            # Min 9, Max 9 caracteres
        ]

        resultados = perguntar(config, tipo=str, titulo="S I G N  -  I N")

        resultado, cliente_logado = criar_user(lista_clientes=lista_clientes, nome=resultados[0], password=resultados[1], morada=resultados[2], telefone=resultados[3])
        
        if resultado:
            print(" Conta criada com sucesso!")
            sleep(1.5)  
            menu_app()
            break
        input(ENTER)

def menu_app():
    global mostrar_menu, lista_opcoes
    
    while True:
        if mostrar_menu == 0:
            limpar()
            print(titulo("D A S H"))
            print(titulo("1 - Cliente | 2 - Adicionar Estabelecimento | 0 - Sair", sem_linha=True))

            print()
            if lista_estabelecimentos:
                
                for est in range(0, len(lista_estabelecimentos), 4):
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
        res = perguntar([["  Escolha uma opção"]], tipo=int, titulo="D A S H")

        if res[0] == 1:
            menu_cliente()
        elif res[0] == 2:
            menu_adicionar_estabelecimento()
        elif res[0] == 0:
            print("Saindo...")
            break
        else:
            if res[0] in lista_opcoes:
                menu_estabelecimento(lista_estabelecimentos[res[0] - 4])
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
            res = perguntar([["  Novo nome", 3, 20], ["  Nova password", 8, 20], ["  Nova morada", 5, 100], ["  Novo telefone", 9, 9]], tipo=str, titulo="E D I T A R  P R O F I L E", vazio=True)
            if res[0]:
                cliente_logado.nome = res[0]
            if res[1]:
                cliente_logado.password = res[1]
            if res[2]:
                cliente_logado.morada = res[2]
            if res[3]:
                cliente_logado.telefone = res[3]

            guardar_dados(caminho="cliente", lista=lista_clientes)
            print("Perfil atualizado com sucesso!")
            input(ENTER)
        elif res == 3:
            menu_marcacoes()
        elif res == 0:
            mostrar_menu = 0
            break
        else:
            print("Opção inválida, tente novamente.")

def menu_estabelecimento(estabelecimento: object): # para ver o estabelecimento e poder fazer a marcação
    global mostrar_menu

    texto = f"""
    NOME: {estabelecimento.nome}
    MORADA: {estabelecimento.morada}
    TELEFONE: {estabelecimento.telefone}
    HORÁRIO DE FUNCIONAMENTO: {estabelecimento.horario_funcionamento}
    """
    mostra_info(texto)

    res = input("Deseja fazer uma marcação? (s/n): ").strip().lower()
    if res == 's':
        criar_marcacao(estabelecimento)
    else:
        print("Voltando ao menu...")
        sleep(1)

    mostrar_menu = 0

def menu_adicionar_estabelecimento(): # para criar um estabelimento
    global mostrar_menu, lista_estabelecimentos
    while True:
        try:
            limpar()
            res = perguntar([["  Nome do estabelecimento", 3, 50],
                ["  Morada", 3, 30], 
                ["  Telefone", 9, 9],
                ["  Horário de funcionamento (HH:MM-HH:MM)", 11, 11]],              
                    tipo=str, titulo="A D I C I O N A R  E S T A B E L E C I M E N T O")
        
            lista_estabelecimentos.append(Estabelecimento(nome=res[0], morada=res[1], telefone=res[2], horario_funcionamento=res[3]))
            guardar_dados(caminho="estabelecimento", lista=lista_estabelecimentos)
            print("Estabelecimento adicionado com sucesso!")
            input(ENTER)
            mostrar_menu = 0
            break
        except ValueError as e:
            print(f"Erro: {e}")
            input(ENTER)

def menu_profile():
    texto = f"""
    NOME: {cliente_logado.nome}
    MORADA: {cliente_logado.morada}
    TELEFONE: {cliente_logado.telefone}
    """
    mostra_info(texto)
    input(ENTER_VOLTAR)

def menu_marcacoes():
    global cliente_logado
    while True:
        if cliente_logado.marcacoes:
            texto = ""
            for marcacao in cliente_logado.marcacoes:
                texto += f"""
        NUMERO DA MARCAÇÃO: {cliente_logado.marcacoes.index(marcacao) + 1}
        ESTABELECIMENTO: {marcacao['estabelecimento_nome']}
        HORA DA MARCAÇÃO: {marcacao['hora_marcacao']}
        QUANTIDADE DE PESSOAS: {marcacao['quantidade_pessoas']}
        ----------------------------------------
                """
            texto += "0 - Voltar ao menu"
            mostra_info(texto)
            res = input("Escolha uma marcação para editar ou 0 para voltar: ").strip()
            if res == '0':
                break
            elif res.isdigit() and 1 <= int(res) <= len(cliente_logado.marcacoes):
                marcacao_selecionada = cliente_logado.marcacoes[int(res) - 1]
                indice_marcacao = int(res) 
                res = criar_menu(menu_config=[{"sub": "O QUE DESEJA FAZER?", "opcoes": ["Editar marcação", "Eliminar marcação"]}])
                if res == 1:
                    menu_editar_marcacao(marcacao_selecionada)
                elif res == 2:
                    cliente_logado.eliminar_marcacao(indice_marcacao - 1)
                    guardar_dados(caminho="cliente", lista=lista_clientes)
                    print("Marcação eliminada com sucesso!")
                    input(ENTER)
            else:
                print("Opção inválida, voltando ao menu...")
                sleep(1)
        else:
            mostra_info("Não tem marcações no momento.")
            input(ENTER_VOLTAR)
            break

def criar_marcacao(estabelecimento: object): 
    global cliente_logado, lista_clientes
    while True:
        try:
            res = perguntar([["  Hora da marcação (HH:MM)", 5, 5], ["  Quantidade de pessoas", 1, 2]], tipo=str, titulo="C R I A R  M A R C A Ç Ã O")
            nova_marcacao = Marcacao(estabeleciemento=estabelecimento, hora_marcacao=res[0], quantidade_pessoas=int(res[1]))
            cliente_logado.adicionar_marcacao(nova_marcacao.para_dicionario())
            guardar_dados(caminho="cliente", lista=lista_clientes)
            print("Marcação criada com sucesso!")
            input(ENTER)
            break
        except ValueError as e:
            print(f"Erro: {e}")
            input(ENTER)

def menu_editar_marcacao(marcacao: dict):
    while True:
        try:
            res = perguntar([["  Nova hora da marcação (HH:MM)", 5, 5], ["  Nova quantidade de pessoas", 1, 2]], tipo=str, titulo="E D I T A R  M A R C A Ç Ã O", vazio=True)
            if res[0]:
                marcacao['hora_marcacao'] = res[0]
            if res[1]:
                marcacao['quantidade_pessoas'] = int(res[1])
            guardar_dados(caminho="cliente", lista=lista_clientes)
            print("Marcação editada com sucesso!")
            input(ENTER)
            break
        except ValueError as e:
            print(f"Erro: {e}")
            input(ENTER)

if __name__ == "__main__":
    menu()