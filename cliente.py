class Cliente():

    def __init__(self, nome: str, password: str, marcacoes: list=None):
        self.nome = nome
        self.password = password

        if marcacoes is None:
            self.marcacoes = []
        else:
            self.marcacoes = marcacoes

    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        if 3 <= nome.strip() <= 20:
            self.__nome = nome.title().strip()
        else:
            print("O nome tem que ter no mínimo 3 caracteres e no maximo 20.")


    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if password.replace(" ", "") >= 8:  #Não permite espaços
            self.__password = password

        else:
            print("A password tem que ter no mínimo 8 caracteres.")

    def verificador_password():
        pass

    def adicionar_marcacao():
        pass

    def eliminar_marcacao():
        pass

    def editar_marcacao():
        pass