class Estoque:
    def __init__(self):
        self.__cod_produto = None
        self.__nome_produto = None
        self.__qtd = None

    def set_cod_produto(self, cod_produto):
        self.__cod_produto = cod_produto

    def set_nome_produto(self, nome_produto):
        self.__nome_produto = nome_produto

    def set_qtd(self, qtd):
        self.__qtd = qtd

    def get_cod_produtp(self):
        return self.__cod_produto

    def get_nome_produto(self):
        return self.__nome_produto

    def get_qtd(self):
        return self.__qtd