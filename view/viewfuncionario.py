from controllerdistribuidora import controllerfuncionario

def inserir_funcionario(indice=None):
    if indice:
        print('\nModificar funcionário')
    else:
        print('\nInserir novo usuario')
    print('(a senha tem que ter mais de 7 caracteres, e aceita letras e números)')
    print('(o login aceita letras e números mas tem que começar com letras)')
    login = input('\nInforme o login: ')
    i = controllerfuncionario.verificar_funcionario(login)
    if i == 2:
        nome = input('Informe o nome: ')
        senha = input('Informe a senha: ')
        rua = input('Informe a rua onde mora: ')
        numero = input('Informe o número da rua: ')
        bairro = input('Informe o bairro: ')
        cidade = input('Informe a cidade: ')
        estado = input('Informe o estado: ')
        j = controllerfuncionario.salvar_funcionario(nome, login, senha, rua, numero, bairro, cidade, estado, indice)
        if j == 0:
            print('\nInforme os dados corretamente')
        if j == 1:
            if indice:
                print('\nFuncionário modificado com sucesso')
            else:
                print('\nUsuário cadastrado com sucesso')
    elif i in [1, 0]:
        print('\nUsuário é master ou já existe')

def modificar_funcionario():
    print('\nModificar funcionário')
    login = input('\nInforme o login do funcionário que deseja modificar: ')
    i = controllerfuncionario.atualizar_funcionario(login)
    if i == 0:
        print('\nFincionário não existe')

def procurar_funcionario():
    print('\nBusca de funcionário')
    login = input('Informe o login que deseja buscar: ')
    if not controllerfuncionario.buscar_funcionario(login):
        print('\nFuncionário não existe')

def excluir_funcionario():
    print('\nDeletar funcionário')
    login = input('Informe o login do funcionário: ')
    i = controllerfuncionario.deletar_funcionario(login)
    if i == 1:
        print('\nFuncionário deletado com sucesso')
    else:
        print('\nFuncionário não existe ou é Master')

def funcionario_menu():
    while True:
        print('\nMenu de usuário')
        entrada = input('1 - Inserir\n2 - Buscar todos \n3 - Buscar \n4 - Modificar\n5 - Excluir \n0 - Voltar\n')
        if entrada == '0':
            break
        if entrada == '1':
            inserir_funcionario()
        elif entrada == '2':
            print('\nLista com todos funcionários\n')
            controllerfuncionario.listar_todos()
        elif entrada == '3':
            procurar_funcionario()
        elif entrada == '4':
            modificar_funcionario()
        elif entrada == '5':
            excluir_funcionario()
        else:
            print('Informe os dados corretamente')