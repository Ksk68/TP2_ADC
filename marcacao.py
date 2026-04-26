class Marcacao():

    def __init__(self, estabeleciemento: object, hora_marcacao: str, quantidade_pessoas: int):

        # estabelecimento
        self.estabelecimento_nome = estabeleciemento.nome
        self.estabelecimento = estabeleciemento
        self.estabelecimento_horario = estabeleciemento.horario_funcionamento

        # da class
        self.hora_marcacao = hora_marcacao
        self.quantidade_pessoas = quantidade_pessoas