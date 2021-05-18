from controllerdistribuidora.controllercliente import salvar_cliente, atualizar_cliente, buscar_cliente, listar_todos, deletar_cliente

def inserir_cliente(i=None):
    if i:
        print('\nModificar cliente')
    else:
        print('\nInserir clientes')
    cnpj = input('Informe o CNPJ: ')
    nome = input('Informe o nome: ')
    estab = input('Informe o estabelecimento: ')
    j = salvar_cliente(cnpj, nome, estab, indice=i)
    if j == 0:
        print('\nCliente já existe')
    if j == 1:
        print('\nInforme os dados corretamente')
    if j == 2:
        if i:
            print('\nCliente modificado com sucesso')
        else:
            print('\nCliente inserido com sucesso')

def procurar_cliente():
    print('\nBuscar cliente')
    cnpj = input('Informe o CNPJ: ')
    if not buscar_cliente(cnpj):
        print('\nCliente não esxiste')
    

def modificar_cliente():
    cnpj = input('\nInforme o CNPJ do cliente que deseja modificar: ')
    i = atualizar_cliente(cnpj)
    if i == 0:
        print('\nCliente não existe')

def excluir_cliente():
    print('\nExcluir cliente')
    cnpj = input('Informe o CNPJ: ')
    i = deletar_cliente(cnpj)
    if i == 0:
        print('\nCliente não existe')
    elif i == 1:
        print('\nCliente excluido com sucesso')

def cliente_menu():
    while True:
        print('\nMenu cliente')
        entrada = input('1 - Inserir\n2 - Buscar todos\n3 - Buscar\n4 - Modificar cliente\n5 - Excluir\n0 - Voltar\n')
        if entrada == '0':
            break
        elif entrada == '1':
            inserir_cliente()
        elif entrada == '2':
            print('\nLista com todos os clientes')
            listar_todos()
        elif entrada == '3':
            procurar_cliente()
        elif entrada  == '4':
            modificar_cliente()
        elif entrada == '5':
            excluir_cliente()
        else:
            print('\nInsira os dados corretamente')
