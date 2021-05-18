class Funcionario:
    def __init__(self):
        self.__login = None
        self.__nome = None
        self.__senha = None
        self.__id_endereco = None
    
    def set_login(self, login):
        self.__login = login

    def set_nome(self, nome):
        self.__nome = nome
    
    def set_senha(self, senha):
        self.__senha = senha
    
    def set_id_endereco(self, id_endereco):
        self.__id_endereco = id_endereco

    def get_login(self):
        return self.__login

    def get_nome(self):
        return self.__nome

    def get_senha(self):
        return self.__senha

    def get_id_endereco(self):
        return self.__id_endereco

class FuncionarioMaster(Funcionario):
    def __init__(self):
        super().__init__()
        self.__tipo = 'Master'

    def get_tipo(self):
        return self.__tipo

class FuncionarioComum(Funcionario):
    def __init__(self):
        super().__init__()
        self.__tipo = 'Comum'

    def get_tipo(self):
        return self.__tipo

