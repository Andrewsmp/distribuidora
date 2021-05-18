from classesdistribuidora.bebida import *
from classesdistribuidora import util
from view import viewbebidas

def gerar_codigo(tipo):
    bebidas_al = []
    bebidas_na = []
    j = []
    bebidas = util.retornar_bebidas()
    for bebida in bebidas:
        if bebida['codigo'][:3] == 'BNA':
            bebidas_na.append(bebida['codigo'])
        else:
            bebidas_al.append(bebida['codigo'])
    if tipo == '1':
        for i in bebidas_al:
            j.append(int(i[3:]))
        return 'BAA' + str(max(j) + 1)
    if tipo == '2':
        for i in bebidas_na:
            j.append(int(i[3:]))
        return 'BNA' + str(max(j) + 1)

def percorrer_bebidas(codigo, num):
    bebida = ''
    indice = ''
    nomes = []
    bebidas = util.retornar_bebidas()

    for i, item in enumerate(bebidas):
        nomes.append(item['nome'])
        if codigo == item['codigo']:
            if item['tipo'] == 'AL':
                bebida = BebidaAlcoolica()
                bebida.set_codigo(item['codigo'])
                bebida.set_nome(item['nome'])
                bebida.set_valor(item['valor'])
            else:
                bebida = BebidaNaoAlcoolica()
                bebida.set_codigo(item['codigo'])
                bebida.set_nome(item['nome'])
                bebida.set_valor(item['valor'])
            indice = i
    if num == 0:
        return bebida
    if num == 1:
        return indice
    if num == 2:
        return nomes
    if num == 3:
        return bebida, indice

def isfloat(num):
    try:
        float(num)
        return True
    except:
        return False

def validar_nome(nome):
    contador = 0
    for char in nome:
        if char.isalnum() or char == ' ' or char == '-':
            contador += 1
    if contador == len(nome):
        return True
    return False

def iniciar_objetos(nome, valor, tipo):
    bebidas = util.retornar_bebidas()
    if tipo == '1':
        bebida = BebidaAlcoolica()
        bebida.set_codigo(gerar_codigo(tipo))
        bebida.set_nome(nome)
        bebida.set_valor(float(valor))
    else:
        bebida = BebidaNaoAlcoolica()
        bebida.set_codigo(gerar_codigo(tipo))
        bebida.set_nome(nome)
        bebida.set_valor(float(valor))

    return bebida

def salvar_bebida(nome, valor, tipo, i=None):
    bebidas = util.retornar_bebidas()
    nomes = percorrer_bebidas(1, 2)
    if i:
        del(bebidas[i])
    if nome not in nomes:
        if validar_nome(nome) and isfloat(valor) and float(valor) > 0:
            bebida = iniciar_objetos(nome, valor, tipo)
            bebidas.append({'codigo': bebida.get_codigo(),
                                'nome': bebida.get_nome(),
                                'valor': bebida.get_valor(),
                                'tipo': bebida.get_tipo()})
            util.inserir_bebida(bebidas)
            return 2
        return 1
    return 0     
    
def atualizar_bebidas(codigo):
    i = percorrer_bebidas(codigo, 1)
    if i:
        viewbebidas.inserir_bebida(indice=i)
        return
    return 0

def buscar_bebidas(codigo):
    bebida = percorrer_bebidas(codigo, 0)
    if bebida:
        if bebida.get_tipo() == 'AL':
            tipo = 'Alcoólica'
        else:
            tipo = 'Não alcoólica'
        print('\nBebida encontrada')
        print('\nCódigo: {}. Nome: {}. Valor: R${:.2f}. Tipo: {}'
        .format(bebida.get_codigo(), bebida.get_nome(),
        bebida.get_valor(), tipo))
        return
    return 0

def listar_todos():
    bebidas = util.retornar_bebidas()
    for bebida in bebidas:
        if bebida['tipo'] == 'AL':
            tipo = 'Alcoólica'
        else:
            tipo = 'Não alcoólica'
        print('Código: {}. Nome: {}. Valor: R${:.2f}. Tipo: {}'
        .format(bebida['codigo'], bebida['nome'], bebida['valor'], tipo))

def deletar_bebida(codigo):
    bebida, i = percorrer_bebidas(codigo, 3)
    bebidas = util.retornar_bebidas()
    if bebida:
        del(bebidas[i])
        util.inserir_bebida(bebidas)
        return 1
    return 0