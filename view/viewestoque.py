from controllerdistribuidora.controllerestoque import efetuar_compra, buscar_bebidas_estoque, listar_todos

def comprar():
    print('\nEfetuar compra')
    codigo = input('Informe o código da bebida: ')
    qtd = input('Informe a quantidade da compra: ')
    i = efetuar_compra(codigo, qtd)
    if i == 0:
        print('\nBebida não cadastrada')
    elif i == 1:
        print('\nInforme a quantidade corretamente')
    elif i == 2:
        print('\nCompra efetuada com sucesso')

def procurar_bebida_estoque():
    print('\nBuscar bebidas no estoque')
    codigo = input('Informe o código da bebida: ')
    if not buscar_bebidas_estoque(codigo):
        print('\nBebida não encontrada no estoque')

def estoque_menu():
    while True:
        print('\nMenu do estoque')
        entrada = input('1 - Efetuar compra\n2 - Buscar bebida no estoque\n3 - Ver todas bebidas no estoque\n0 - Voltar\n')
        if entrada == '0':
            break
        elif entrada == '1':
            comprar()
        elif entrada == '2':
            procurar_bebida_estoque()
        elif entrada == '3':
            print('\nLista de bebidas no estoque')
            listar_todos()
        else:
            print('\nInforme os dados corretamente')