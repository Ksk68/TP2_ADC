class Estabelecimento():

    def __init__(self, nome: str, morada: str, telefone: str, horario_funcionamento: str):
        self.nome = nome
        self.morada = morada
        self.telefone = telefone
        self.horario_funcionamento = horario_funcionamento # ex: "09:00-18:00"