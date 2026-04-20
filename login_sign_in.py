from cliente import Cliente
from save_load import guardar_dados, carregar_save 

def criar_user(lista_clientes: list):
    while True:
        print("LOGIN")
        nome = input("Nome: ").title().strip()

        if nome > 20 or nome < 3:
            print("Nome tem de ser entre 3-20 caracteres")
            continue

        password = input("Password: ").replace(" ", "")

        if password > 25 or password < 8:
            print("Nome tem de ser entre 8-25 caracteres")
            continue
        
        novo_user = Cliente(nome=nome, password=password)
        lista_clientes.append(novo_user)
        guardar_dados(tipo="cliente", obj=lista_clientes)

        
def verificar_user(nome: str, password: str):
    users = carregar_save(tipo="cliente", obj=Cliente)

    for i in users:
        if i.nome == nome and i.verificador_password(password):
            print("Login bem sucedido")
            return i

    print("Login falhado")
    return False


