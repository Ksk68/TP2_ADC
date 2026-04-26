import re

class Estabelecimento():

    def __init__(self, nome: str, morada: str, telefone: str, horario_funcionamento: str):
        self.nome = nome
        self.morada = morada
        self.telefone = telefone
        self.horario_funcionamento = horario_funcionamento # ex: "09:00-18:00"

    def para_dicionario(self):
        return {
            "nome": self.nome,
            "morada": self.morada,
            "telefone": self.telefone,
            "horario_funcionamento": self.horario_funcionamento
        }

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, valor):
        valor = valor.strip() # remove espaços da frente e de trás
        if 3 <= len(valor) <= 50:
            valor = valor.title()
            self.__nome = valor
        else:
            print("Nome tem que ter entre 3 a 50 caracteres.")


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
        valor.replace(" ","") # remove todos os espaços
        if len(valor) == 9:
            self.__telefone = valor
        else:
            print("Insira um número de telemóvel com 9 caracteres.")

    
    @property
    def horario_funcionamento(self):
        return self.__horario_funcionamento
    
    @horario_funcionamento.setter
    def horario_funcionamento(self, valor):

        padrao = r"^(\d{2}):(\d{2})-(\d{2}):(\d{2})$"
        match = re.match(padrao, valor)
        
        if not match:
            raise ValueError(f"Formato '{valor}' inválido! Use HH:MM-HH:MM")

        hora_abertura, min_abertura, hora_fecho, min_fecho = map(int, match.groups())

        if not (0 <= hora_abertura <= 23 and 0 <= min_abertura <= 59 and 
                0 <= hora_fecho <= 23 and 0 <= min_fecho <= 59):
            raise ValueError(f"Horário impossível detetado: '{valor}'")


        minutos_totais_abertura = hora_abertura * 60 + min_abertura # conversão para mins totais
        minutos_totais_fecho = hora_fecho * 60 + min_fecho

        if minutos_totais_abertura >= minutos_totais_fecho:
            abertura_formatada = f"{hora_abertura:02d}:{min_abertura:02d}" # :02d para dois digitos
            fecho_formatado = f"{hora_fecho:02d}:{min_fecho:02d}"
            
            raise ValueError(
                f"Conflito de horário: A abertura ({abertura_formatada}) "
                f"não pode ser posterior ou igual ao fecho ({fecho_formatado})!"
            )

        self.__horario_funcionamento = valor
