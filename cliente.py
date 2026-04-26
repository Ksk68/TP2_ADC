class Cliente():

    def __init__(self, nome: str, password: str, marcacoes: list=None, morada: str=None, telefone: str=None):
        self.nome = nome
        self.password = password
        self.morada = morada
        self.telefone = telefone

        if marcacoes is None:
            self.marcacoes = []
        else:
            self.marcacoes = marcacoes

    def para_dicionario(self):
        return {
            "nome": self.nome,
            "password": self.password,
            "marcacoes": self.marcacoes,
            "morada": self.morada,
            "telefone": self.telefone
        }
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        if 3 <= len(nome.strip()) <= 20:
            self.__nome = nome.title().strip()
        else:
            print("O nome tem que ter no mínimo 3 caracteres e no maximo 20.")


    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if len(password.replace(" ", "")) >= 8:  #Não permite espaços
            self.__password = password

        else:
            print("A password tem que ter no mínimo 8 caracteres.")

    def verificador_password(self, password):
        if self.password == password:
            return True
        else:
            return False
        
    @property
    def morada(self):
        return self.__morada
    
    @morada.setter
    def morada(self, valor):
        valor = valor.strip()
        if 5 <= len(valor) <= 100:
            self.__morada = valor
        else:
            print("Morada tem que ter entre 5 a 100 caracteres.")

    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, valor):
        valor.replace(" ","") 
        if len(valor) == 9:
            self.__telefone = valor
        else:
            print("Insira um número de telemóvel com 9 caracteres.")


    def adicionar_marcacao(self, marcacao):
        self.marcacoes.append(marcacao)

    def eliminar_marcacao(self, marcacao):
        self.marcacoes.pop(marcacao)

    def editar_marcacao():
        pass
    