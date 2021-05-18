from controllerdistribuidora.controllerfuncionario import logar
from view.viewfuncionario import funcionario_menu
from view.viewbebidas import bebida_menu
from view.viewestoque import estoque_menu
from controllerdistribuidora.controllerestoque import enviar_bebida
from view.viewcliente import cliente_menu
from view.viewvendas import venda_menu

def menu_comum():
    bebidas = enviar_bebida()
    print('\nAlerta!')
    for bebida in bebidas:
        print('{} tem {} unidades no estoque'.format(bebida['nome'], bebida['qtd']))
    while True:
        print('\nBem vindo escolha uma opção no menu')
        entrada = input('1 - Menu bebidas\n2 - Menu cliente\n3 - Menu vendas\n4 - Menu estoque\n0 - Voltar \n')
        if entrada == '0':
            break
        if entrada == '1':
            bebida_menu()
        elif entrada == '2':
            cliente_menu()
        elif entrada == '3':
            venda_menu()
        elif entrada == '4':
            estoque_menu()
        else:
            print('Informe o comando corretamente')

def menu_master():
    bebidas = enviar_bebida()
    print('\nAlerta!')
    for bebida in bebidas:
        print('{} tem {} unidades no estoque'.format(bebida['nome'], bebida['qtd']))
    while True:
        print('\nBem vindo escolha uma opção no menu')
        entrada = input('1 - Menu usuário\n2 - Menu bebidas\n3 - Menu cliente\n4 - Menu vendas\n5 - Menu estoque\n0 - Voltar\n')
        if entrada == '0':
            break
        elif entrada == '1':
            funcionario_menu()
        elif entrada == '2':
            bebida_menu()
        elif entrada == '3':
            cliente_menu()
        elif entrada == '4':
            venda_menu()
        elif entrada == '5':
            estoque_menu()
        else:
            print('Informe o comando corretamente')

def login():
    login = input('Informe seu login: ')
    senha = input('Informe sua senha: ')
    i = logar(login, senha)
    if i == 0:
        print('\nUsuário ou senha inválida')
    elif i == 1:
        menu_comum()
    elif i == 2:
        menu_master()

while True:
    print('Bem vindo escolha uma opção')
    entrada = input('1 - login\n0 - Sair\n')

    if entrada == '0':
        break
    elif entrada == '1':
        login()
    else:
        print('\nInforme os dados corretamente')

    