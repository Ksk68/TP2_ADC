# from cliente import Cliente

def criar_user():
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
        
        # novo_user = Cliente(nome=nome, password=password)
        # guardar(tipo="cliente", novo_user)
        

        
def verificar_user():
    pass

