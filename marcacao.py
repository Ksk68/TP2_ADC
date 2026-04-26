from estabelecimento import Estabelecimento
import re

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
    
    @property
    def quantidade_pessoas(self):
        return self.__quantidade_pessoas
    
    @quantidade_pessoas.setter
    def quantidade_pessoas(self, value):
        if isinstance(value, int) and 1 <= value <= 15:
            self.__quantidade_pessoas = value
        else:
            raise ValueError("A quantidade de pessoas deve ser um número inteiro entre 1 e 15.")
        

    @property
    def hora_marcacao(self):
        return self.__hora_marcacao 
    
    @hora_marcacao.setter
    def hora_marcacao(self, value):
        # Verificar se a hora está no formato HH:MM
        if not re.match(r'^\d{2}:\d{2}$', value):
            raise ValueError("A hora da marcação deve estar no formato HH:MM.")
        
        value_hora, value_minuto = map(int, value.split(':'))
        if not (0 <= value_hora < 24 and 0 <= value_minuto < 60):
            raise ValueError("A hora deve ser válida (00:00 a 23:59).")
        
        if self.estabelecimento_horario:
            abertura, fechamento = self.estabelecimento_horario.split('-')
            abertura_hora, abertura_minuto = map(int, abertura.split(':'))
            fechamento_hora, fechamento_minuto = map(int, fechamento.split(':'))
            
            hora_atual = value_hora * 60 + value_minuto
            hora_abertura = abertura_hora * 60 + abertura_minuto
            hora_fechamento = fechamento_hora * 60 + fechamento_minuto
            
            if not (hora_abertura <= hora_atual <= hora_fechamento):
                raise ValueError("A hora deve estar dentro do horário de funcionamento.")
        
        self.__hora_marcacao = value