from cliente import Cliente
from save_load import guardar_dados, carregar_save 

def criar_user(lista_clientes: list, nome: str, password: str):
    novo_user = Cliente(nome=nome, password=password)
    
    lista_clientes.append(novo_user)
    
    guardar_dados(caminho="cliente", lista=lista_clientes)

        
def verificar_user(nome: str, password: str):
    users = carregar_save(caminho="cliente", obj=Cliente)

    for i in users:
        if i.nome == nome.strip().title() and i.verificador_password(password):
            print("Login bem sucedido")
            return i

    print("Login falhado")
    return False


