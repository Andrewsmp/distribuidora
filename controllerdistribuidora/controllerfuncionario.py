from classesdistribuidora.funcionario import FuncionarioComum, FuncionarioMaster
from classesdistribuidora.endereco import Endereco
from classesdistribuidora import util
from view.viewfuncionario import inserir_funcionario

def percorrer_funcionario(login, num):
    funcionario = ''
    indice = ''
    funcionarios = util.retornar_funcionarios()

    for i, item in enumerate(funcionarios):
        if login == item['login']:
            if item['status'] == 'Master':
                funcionario = FuncionarioMaster()
                funcionario.set_login(item['login'])
                funcionario.set_nome(item['nome'])
                funcionario.set_senha(item['senha'])
                funcionario.set_id_endereco(item['id_endereco'])
            else:
                funcionario = FuncionarioComum()
                funcionario.set_login(item['login'])
                funcionario.set_nome(item['nome'])
                funcionario.set_senha(item['senha'])
                funcionario.set_id_endereco(item['id_endereco'])
            indice = i
    if num == 0:
        return funcionario, indice
    return funcionario

def percorrer_endereco(id, num):
    enderecos = util.retornar_enderecos()
    indice = ''
    endereco = ''

    for i, item in enumerate(enderecos):
        if id == item['id']:
            endereco = Endereco()
            endereco.set_id(item['id'])
            endereco.set_rua(item['rua'])
            endereco.set_bairro(item['bairro'])
            endereco.set_cidade(item['cidade'])
            endereco.set_estado(item['estado'])
            endereco.set_numero(item['numero'])
            indice = i
    if num == 0:
        return indice
    return endereco

def gerar_id_endereco():
    ids = []
    enderecos = util.retornar_enderecos()
    for endereco in enderecos:
        ids.append(endereco['id'])
    return max(ids) + 1

def validar_dados(nome, login, senha, rua, numero, bairro, cidade, estado):
    nome_contador = 0; login_contador = 0; senha_contador = 0; rua_contador = 0
    numero_contador = 0; bairro_contador = 0; cidade_contador = 0; estado_contador = 0

    for char in nome:
        if char.isalpha() or char == ' ':
            nome_contador += 1
    for char in login:
        if char.isalnum():
            login_contador += 1    
    for char in senha:
        if char.isalnum():
            senha_contador += 1
    for char in rua:
        if char.isalnum() or char == ' ':
            rua_contador += 1
    for char in numero:
        if char.isdigit():
            numero_contador += 1
    for char in bairro:
        if char.isalnum() or char == ' ':
            bairro_contador += 1
    for char in cidade:
        if char.isalpha() or char == ' ':
            cidade_contador += 1
    for char in estado:
        if char.isalpha() or char == ' ':
            estado_contador += 1

    condicoes = [nome_contador == len(nome), login_contador == len(login),
                 senha_contador == len(senha), rua_contador == len(rua),
                 numero_contador == len(numero), bairro_contador == len(bairro),
                 cidade_contador == len(cidade), estado_contador == len(estado),
                 len(senha) > 7, nome[0].isalpha()]
    if all(condicoes):
        return True
    return False

def iniciar_objetos(nome, login, senha, rua, numero, bairro, cidade, estado):
    id = gerar_id_endereco()

    funcionario = FuncionarioComum()
    funcionario.set_login(login)
    funcionario.set_nome(nome.title())
    funcionario.set_senha(senha)
    funcionario.set_id_endereco(id)
    endereco = Endereco()
    endereco.set_id(id)
    endereco.set_rua(rua.title())
    endereco.set_numero(numero)
    endereco.set_bairro(bairro.title())
    endereco.set_cidade(cidade.title())
    endereco.set_estado(estado.title())

    return funcionario, endereco

def verificar_funcionario(login):
    funcionario = percorrer_funcionario(login, 1)
    if funcionario and funcionario.get_tipo() == 'Comum':
        return 0
    elif funcionario and funcionario.get_tipo() == 'Master':
        return 1
    else:
        return 2

def salvar_funcionario(nome, login, senha, rua, numero, bairro, cidade, estado, i=None):
    funcionarios = util.retornar_funcionarios()
    enderecos = util.retornar_enderecos()
    
    if i:
        j = percorrer_endereco(funcionarios[i]['id_endereco'], 0)
        del(funcionarios[i])
        del(enderecos[j])

    if validar_dados(nome, login, senha, rua, numero, bairro, cidade, estado):
        funcionario, endereco = iniciar_objetos(nome, login, senha, rua, numero, bairro, cidade, estado)
        funcionarios.append({'login': funcionario.get_login(),
                                'nome': funcionario.get_nome(),
                                'senha': funcionario.get_senha(),
                                'id_endereco': funcionario.get_id_endereco(),
                                'status': funcionario.get_tipo()})
            
        enderecos.append({'id': endereco.get_id(),
                            'rua': endereco.get_rua(),
                            'numero': endereco.get_numero(),
                            'cidade': endereco.get_cidade(),
                            'estado': endereco.get_estado(),
                            'bairro': endereco.get_bairro()})
        util.inserir_funcionario(funcionarios)
        util.inserir_endereco(enderecos)
        return 1
    return 0

def atualizar_funcionario(login):
    funcionario, i = percorrer_funcionario(login, 0)
    if funcionario:
        inserir_funcionario(indice=i)
        return
    return 0

def listar_todos():
    funcionarios = util.retornar_funcionarios()
    for funcionario in funcionarios:
        print('Login: {}. Nome: {}. Status: {}'
        .format(funcionario['login'], funcionario['nome'], funcionario['status']))

def buscar_funcionario(login):
    funcionario = percorrer_funcionario(login, 1)

    if funcionario:
        endereco = percorrer_endereco(funcionario.get_id_endereco(), 1)
        print('\nFuncionário encontrado')
        print('Nome: {}\nLogin: {}\nStatus: {}\nRua: {}\nNúmero: {}\nBairro: {}\nCidade: {}\nEstado: {}'
        .format(funcionario.get_nome(), funcionario.get_login(), funcionario.get_tipo(),
        endereco.get_rua(), endereco.get_numero(), endereco.get_bairro(), endereco.get_cidade(),
        endereco.get_estado()))
        return True
    return False

def deletar_funcionario(login):
    funcionario, i = percorrer_funcionario(login, 0)
    if funcionario and funcionario.get_tipo() == 'Comum':
        j = percorrer_endereco(funcionario.get_id_endereco(), 0)
        funcionarios = util.retornar_funcionarios()
        enderecos = util.retornar_enderecos()
        del(funcionarios[i])
        del(enderecos[i])
        util.inserir_funcionario(funcionarios)
        util.inserir_endereco(enderecos)
        return 1
    return 0

def logar(login, senha):
    funcionario = percorrer_funcionario(login, 1)
    if funcionario and senha == funcionario.get_senha():
       if funcionario.get_tipo() == 'Master':
           return 2
       return 1
    return 0
