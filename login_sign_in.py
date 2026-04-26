from cliente import Cliente
from save_load import guardar_dados 

def criar_user(lista_clientes: list, nome: str, password: str, morada: str=None, telefone: str=None):
    novo_user = Cliente(nome=nome, password=password, morada=morada, telefone=telefone)

    for cliente in lista_clientes:
        if cliente.nome == novo_user.nome:
            print(" Já existe um usuário com esse nome. Tente outro nome.")
            return False

    lista_clientes.append(novo_user)
    
    guardar_dados(caminho="cliente", lista=lista_clientes)

    return True


def verificar_user(nome: str, password: str, lista_clientes: list):
    nome_procurado = nome.strip().title()

    for i in lista_clientes:
        if i.nome == nome_procurado and i.verificador_password(password):
            return True, i

    return "Login falhado: Nome ou Password incorretos", None


