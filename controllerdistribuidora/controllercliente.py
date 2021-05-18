from classesdistribuidora.cliente import Cliente
from classesdistribuidora import util
from view import viewcliente

def percorrer_cliente(cnpj):
    clientes = util.retornar_cliente()
    indice = ''
    cliente = ''
    cnpj = cnpj_generator(cnpj)
    for i, item in enumerate(clientes):
        if cnpj == item['cnpj']:
            cliente = Cliente()
            cliente.set_cnpj(item['cnpj'])
            cliente.set_nome(item['nome'])
            cliente.set_estab(item['estab'])
            indice = i
    return cliente, indice

def cnpj_generator(cnpj):
    cnpj = (cnpj[:2] + '.' + cnpj[2:5] + '.' +
            cnpj[5:8] + '/' + cnpj[8:12] + '-' + cnpj[12:])
    return cnpj

def validar_dados(cnpj, nome, estab):
    nome_contador = 0; estab_contador = 0

    for char in nome:
        if char.isalpha() or char == ' ':
            nome_contador += 1

    for char in estab:
        if char.isalpha() or char == ' ':
            estab_contador += 1
    condicoes = [nome_contador == len(nome),
                estab_contador == len(estab),
                cnpj.isdigit(), len(cnpj) == 14 ]
    if all(condicoes):
        return True
    return False

def salvar_cliente(cnpj, nome, estab, indice=None):
    cliente, i = percorrer_cliente(cnpj)
    clientes = util.retornar_cliente()
    if indice:
        del(clientes[indice])
    if not cliente:
        if validar_dados(cnpj, nome, estab):
            cliente = Cliente()
            cnpj = cnpj_generator(cnpj)
            cliente.set_cnpj(cnpj)
            cliente.set_nome(nome.title())
            cliente.set_estab(estab.title())
            clientes.append({'cnpj': cliente.get_cnpj(),
                             'nome': cliente.get_nome(),
                             'estab': cliente.get_estab()})
            util.inserir_cliente(clientes)
            return 2
        return 1
    return 0

def atualizar_cliente(cnpj):
    cliente, indice = percorrer_cliente(cnpj)

    if cliente:
        viewcliente.inserir_cliente(i=indice)
        return
    return 0

def buscar_cliente(cnpj):
    cliente, i = percorrer_cliente(cnpj)
    if cliente:
        print('\nCliente encontrado')
        print('CNPJ: {}. Nome: {}. Estabelecimento: {}'
        .format(cliente.get_cnpj(), cliente.get_nome(), cliente.get_estab()))
        return True
    return False

def listar_todos():
    clientes = util.retornar_cliente()
    for cliente in clientes:
        print('CNPJ: {}. Nome: {}. Estabelecimento: {}'
        .format(cliente['cnpj'], cliente['nome'], cliente['estab']))

def deletar_cliente(cnpj):
    cliente, i= percorrer_cliente(cnpj)
    if cliente:
        clientes = util.retornar_cliente()
        del(clientes[i])
        util.inserir_cliente(clientes)
        return 1
    return 0