from controllerdistribuidora.controllerbebida import *

def inserir_bebida(indice=None):
    if indice:
        print('\nModificar bebidas')
    else:
        print('\nInserir bebidas')
    nome = input('Informe o nome da bebida: ')
    valor = input('Informe o valor: ')
    tipo = input('Informe o tipo\n1 - Alcoólica\n2 - Não alcoóloica\n')
    if tipo in ['1', '2']:
        i = salvar_bebida(nome, valor, tipo, i=indice)
        if i == 1:
            print('\nInforme os dados corretamente')
        elif i == 2:
            if indice:
                print('\nBebida modificada com sucesso')
            else:
                print('\nBebida inserida com sucesso')
        elif i == 0:
            print('\nJá existe uma bebida com esse nome')
    else:
        print('\nInforme os dados corretamente')  

def modificar_bebida():
    codigo = input('\nInforme o código da bebida que deseja modificar: ')
    i = atualizar_bebidas(codigo)
    if i == 0:
        print('\nBebida não existe')

def procurar_bebidas():
    print('\nBuscar bebidas')
    codigo = input('Informe o código da bebida: ')
    i = buscar_bebidas(codigo)
    if i == 0:
        print('\nBebida não existe')

def excluir_bebida():
    print('\nExcluir bebidas')
    codigo = input('Informe o código  da bebida que deseja excluir: ')
    i = deletar_bebida(codigo)
    if i == 0:
        print('\nBebida não existe')
    elif i == 1:
        print('\nBebida excluida com sucesso')

def bebida_menu():
    while True:
        print('\nMenu de bebidas')
        entrada = input('1 - Inserir\n2 - Buscar todos\n3 - Buscar\n4 - Modificar\n5 - Excluir\n0 - Voltar\n')
        if entrada == '0':
            break
        if entrada == '1':
            inserir_bebida()
        elif entrada == '2':
            print('\nLista de todos as bebidas\n')
            listar_todos()
        elif entrada == '3':
            procurar_bebidas()
        elif entrada == '4':
            modificar_bebida()
        elif entrada == '5':
            excluir_bebida()
        else:
            print('Informe os dados corretamente.')