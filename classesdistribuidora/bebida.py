class Bebida:
    def __init__(self):
        self.__codigo = None
        self.__nome = None
        self.__valor = None

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def set_nome(self, nome):
        self.__nome = nome

    def set_valor(self, valor):
        self.__valor = valor

    def get_codigo(self):
        return self.__codigo

    def get_nome(self):
        return self.__nome

    def get_valor(self):
        return self.__valor

class BebidaAlcoolica(Bebida):
    def __init__(self):
        super().__init__()
        self.__tipo = 'AL'

    def get_tipo(self):
        return self.__tipo

class BebidaNaoAlcoolica(Bebida):
    def __init__(self):
        super().__init__()
        self.__tipo = 'NA'

    def get_tipo(self):
        return self.__tipo