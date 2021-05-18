from controllerdistribuidora.controllervendas import *
from controllerdistribuidora.controllerestoque import buscar_bebidas_estoque
from controllerdistribuidora.controllerbebida import buscar_bebidas

def vender():
    print('\nEfetuando venda')
    codigo = input('Informe o código do produto: ')
    qtd = input('Informe a quantidade a ser vendida: ')
    cnpj = input('Informe o CNPJ do cliente(somente números): ')
    login = input('Informe o login do vendedor: ')
    i = efetuar_venda(qtd, codigo, cnpj, login)
    if i == 0:
        print('\nInforme os dados corretamente')
    if i == 1:
        print('\nVerifique se tem essa quantidade do produto no estoque')
    if i == 2:
        print('\nVenda efetuada com sucesso')

def consultar_estoque():
    print('\nConsultar quantas bebidas no estoque')
    codigo = input('Informe o código da bebida: ')
    if not buscar_bebidas_estoque(codigo):
        print('\nBebida não encontrada no estoque')

def consultar_valor():
    print('\nConsultar valor da bebida')
    codigo = input('Informe o código da bebida: ')
    i = buscar_bebidas(codigo)
    if i == 0:
        print('\nBebida não existe')

def relatorio_dia():
    print('\nRlatório de vendas por dia')
    dia = input('Informe o dia do mês de 1 até 31: ')
    mes = input('Informe o mês do ano de 1 até 12: ') 
    ano = input('Informe o ano da venda: ')
    vendas_dia = gerar_relatorio_dia(dia, mes, ano)
    if vendas_dia:
        total = 0
        print('\nVendas do dia {}\n'.format(vendas_dia[0]['data']))
        for venda in vendas_dia:
            print('Quantidade vendida: {}. Valor da venda: R${}. Código do produto: {}. CNPJ do cliente: {}. Nome do vendedor: {}'
            .format(venda['qtd'], venda['valor'], venda['cod'], venda['cnpj'], venda['vendedor']))
            total += venda['valor']
        print('\nO total vendido nesse dia é: R${}'.format(total))
    else:
        print('\nNão existe vendas nesse dia')

def relatorio_vendedor():
    print('\nRelatório de vendas por vendedor')
    login = input('Informe o login do vendedor: ')
    vendas, vendedor = gerar_relatorio_vendedor(login)
    if vendas == 0:
        print('\nNão existe esse vendedor')
    elif vendas == 1:
        print('\nVendedor não possue vendas')
    else:
        print('\nAs vendas de {} foram\n'.format(vendedor.get_nome()))
        total = 0
        for venda in vendas:
            print('Data: {}. Quantidade: {}. Valor: R${}. Produto: {}. Cliente: {}'
            .format(venda['data'], venda['qtd'], venda['valor'], venda['cod'], venda['cnpj']))
            total += venda['valor']
        print('\nO total vendido por {} é: R${}'.format(vendedor.get_nome(), total))

def relatorio_produto():
    print('\nRelatório de vendas por produto')
    codigo = input('Informe o código do produto: ')
    vendas, bebida = gerar_relatorio_produto(codigo)
    if vendas == 0:
        print('\nNão existe produto com esse código')
    elif vendas == 1:
        print('\nNão esxiste vendas desse produto')
    else:
        print('\nAs vendas de {} foram: \n')
        total = 0
        for venda in vendas:
            print('Data: {}. Quantidade: {}. Valor: R${}. Cliente: {}. Vendedor: {}'
            .format(venda['data'], venda['qtd'], venda['valor'], venda['cnpj'], venda['vendedor']))
            total += venda['valor']
        print('\nO total de vendas de {} foram: R${}'.format(bebida.get_nome(), total))

def relatorio_cliente():
    print('\nRelatório de vendas por cliente')
    cnpj = input('Informe o CNPJ do cliente: ')
    vendas, cliente = gerar_relatorio_cliente(cnpj)
    if vendas == 0:
        print('\nNão existe cliente com esse CNPJ')
    elif vendas == 1:
        print('\nEsse cliente não efetuou nenhuma compra')
    else:
        total = 0
        print('\nVendas efetuadas pelo cliente: {}'.format(cliente.get_nome()))
        for venda in vendas:
            print('Data: {}. Quantidade vendida: {}. Valor da venda: R${}. Código do produto: {}. Nome do vendedor: {}'
            .format(venda['data'], venda['qtd'], venda['valor'], venda['cod'], venda['vendedor']))
            total += venda['valor']
        print('\nO total comprado por esse cliente é: R${}'.format(total))

def consultar_relatorios():
    while True:
        print('\nRelatírios de vendas')
        entrada = input('1 - Relatório por dia\n2 - Relatório por vendedor\n3 - Relatório por produto\n4 - Relatório por cliente\n0 - Voltar\n')
        if entrada == '0':
            break
        elif entrada == '1':
            relatorio_dia()
        elif entrada == '2':
            relatorio_vendedor()
        elif entrada == '3':
            relatorio_produto()
        elif entrada == '4':
            relatorio_cliente()

def venda_menu():
    while True:
        print('\nMenu vendas')
        entrada = input('1 - Vender\n2 - Consultar estoque\n3 - Consultar valores\n4 - Relatórios\n0 - Voltar\n')
        if entrada == '0':
            break
        elif entrada == '1':
            vender()
        elif entrada == '2':
            consultar_estoque()
        elif entrada == '3':
            consultar_valor()
        elif entrada == '4':
            consultar_relatorios()
        else:
            print('\nInforme os dados corretamente')
        