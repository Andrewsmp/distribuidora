class Venda:
    def __init__(self):
        self.__id = None
        self.__data = None
        self.__qtd = None
        self.__valor = None
        self.__cod_produto = None
        self.__cnpj_cliente = None
        self.__login_vendedor = None

    def set_id(self, id):
        self.__id = id

    def set_data(self, data):
        self.__data = data

    def set_qtd(self, qtd):
        self.__qtd = qtd

    def set_valor(self, valor):
        self.__valor = valor
    
    def set_nome_produto(self, nome_produto):
        self.__cod_produto = nome_produto

    def set_nome_cliente(self, nome_cliente):
        self.__cnpj_cliente = nome_cliente

    def set_login_vendedor(self, login_vendedor):
        self.__login_vendedor = login_vendedor

    def get_id(self):
        return self.__id

    def get_data(self):
        return self.__data

    def get_qtd(self):
        return self.__qtd

    def get_valor(self):
        return self.__valor

    def get_nome_produto(self):
        return self.__cod_produto

    def get_nome_cliente(self):
        return self.__cnpj_cliente

    def get_login_vendedor(self):
        return self.__login_vendedor