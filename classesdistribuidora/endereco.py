class Endereco:
    def __init__(self):
        self.__id = None
        self.__rua = None
        self.__numero = None
        self.__cidade = None
        self.__estado = None
        self.__bairro = None

    def set_id(self, id):
        self.__id = id

    def set_rua(self, rua):
        self.__rua = rua

    def set_numero(self, numero):
        self.__numero = numero

    def set_cidade(self, cidade):
        self.__cidade = cidade

    def set_estado(self, estado):
        self.__estado = estado

    def set_bairro(self, bairro):
        self.__bairro = bairro

    def get_id(self):
        return self.__id
    
    def get_rua(self):
        return self.__rua

    def get_numero(self):
        return self.__numero

    def get_cidade(self):
        return self.__cidade

    def get_estado(self):
        return self.__estado

    def get_bairro(self):
        return self.__bairro
