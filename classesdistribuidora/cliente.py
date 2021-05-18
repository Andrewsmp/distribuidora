class Cliente:
    def __init__(self):
        self.__cnpj = None
        self.__nome = None
        self.__estabelecimento = None

    def set_cnpj(self, cnpj):
        self.__cnpj = cnpj
    
    def set_nome(self, nome):
        self.__nome = nome
    
    def set_estab(self, estab):
        self.__estabelecimento = estab

    def get_cnpj(self):
        return self.__cnpj

    def get_nome(self):
        return self.__nome

    def get_estab(self):
        return self.__estabelecimento