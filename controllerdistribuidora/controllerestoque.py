from controllerdistribuidora.controllerbebida import percorrer_bebidas
from classesdistribuidora.estoque import Estoque
from classesdistribuidora import util

def percorrer_estoque(codigo):
    bebidas_estoque = util.retornar_estoque()
    indice = ''
    estoque = ''
    for i, item in enumerate(bebidas_estoque):
        if codigo == item['codigo']:
            estoque = Estoque()
            estoque.set_cod_produto(item['codigo'])
            estoque.set_nome_produto(item['nome'])
            estoque.set_qtd(item['qtd'])
            indice = i
    return estoque, indice

def efetuar_compra(codigo, qtd):
    bebida = percorrer_bebidas(codigo, 0)
    estoque, i = percorrer_estoque(codigo)
    bebidas_estoque = util.retornar_estoque()

    if bebida:
        if qtd.isdigit() and int(qtd) > 0:
            if estoque:
                bebidas_estoque[i]['qtd'] += int(qtd)
            else:
                bebidas_estoque.append({'codigo': bebida.get_codigo(),
                                        'nome': bebida.get_nome(),
                                        'qtd': int(qtd)})
            util.inserir_bebida_estoque(bebidas_estoque)
            return 2
        return 1  
    return 0

def listar_todos():
    bebidas_estoque = util.retornar_estoque()
    for bebida_estoque in bebidas_estoque:
        print('Código: {}. Nome: {}. Quantidade: {}'
        .format(bebida_estoque['codigo'], bebida_estoque['nome'],
        bebida_estoque['qtd']))

def buscar_bebidas_estoque(codigo):
    bebida_estoque, i = percorrer_estoque(codigo)
    if bebida_estoque:
        print('\nBebida encontrada')
        print('Código: {}. Nome: {}. Quantidade: {} unidades'
        .format(bebida_estoque.get_cod_produtp(), bebida_estoque.get_nome_produto(),
        bebida_estoque.get_qtd()))
        return True
    return False

def enviar_bebida():
    bebidas_estoque = util.retornar_estoque()

    return list(filter(lambda b: b['qtd']<10000, bebidas_estoque))

