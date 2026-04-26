from estabelecimento import Estabelecimento


class Marcacao():

    def __init__(self, estabeleciemento: object, hora_marcacao: str, quantidade_pessoas: int):

        # estabelecimento
        self.estabelecimento_nome = estabeleciemento.nome
        self.estabelecimento = estabeleciemento
        self.estabelecimento_horario = estabeleciemento.horario_funcionamento

        # da class
        self.hora_marcacao = hora_marcacao
        self.quantidade_pessoas = quantidade_pessoas

    def para_dicionario(self):
        return {
            "estabelecimento_nome": self.estabelecimento_nome,
            "hora_marcacao": self.hora_marcacao,
            "quantidade_pessoas": self.quantidade_pessoas
        }

    @property
    def estabelecimento(self):
        return self.__estabelecimento
    
    @estabelecimento.setter
    def estabelecimento(self, valor):   
        if isinstance(valor, Estabelecimento):
            self.__estabelecimento = valor.nome
        else:
            raise ValueError("O estabelecimento deve ser um objeto do tipo Estabelecimento.")   
    