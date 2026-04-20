class Cliente():

    def __init__(self, nome: str, password, marcacoes: list=None):
        self.nome = nome
        self.password = password

        if marcacoes is None:
            self.marcacoes = []
        else:
            self.marcacoes = marcacoes

    
    @property
    def nome(self):
        pass
    
    @nome.setter
    def nome(self, nome):
        pass

    @property
    def password(self):
        pass  
      
    @password.setter
    def password(self, password):
        pass

    def verificador_password():
        pass

    def adicionar_marcacao():
        pass

    def eliminar_marcacao():
        pass

    def editar_marcacao():
        pass