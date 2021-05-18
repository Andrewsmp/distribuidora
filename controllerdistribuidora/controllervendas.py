from classesdistribuidora import util
from classesdistribuidora.venda import Venda
from datetime import datetime
from controllerdistribuidora.controllerbebida import percorrer_bebidas
from controllerdistribuidora.controllercliente import percorrer_cliente, cnpj_generator
from controllerdistribuidora.controllerfuncionario import percorrer_funcionario
from controllerdistribuidora.controllerestoque import percorrer_estoque

def gerar_data():
    hoje = datetime.now()
    return '{}/{}/{}'.format(hoje.day, hoje.month, hoje.year)

def gerar_id():
    ids = []
    vendas = util.retornar_vendas()
    for venda in vendas:
        ids.append(venda['id'])
    return max(ids) + 1

def efetuar_venda(qtd, codigo, cnpj, login):
    cliente, ic = percorrer_cliente(cnpj)
    bebida, ib = percorrer_bebidas(codigo, 3)
    vendedor = percorrer_funcionario(login, 1)
    estoque, ie = percorrer_estoque(codigo)
    if cliente and bebida and vendedor:
        if qtd.isdigit() and int(qtd) > 0 and estoque.get_qtd() >= int(qtd):
            cnpj = cnpj_generator(cnpj)
            bebidas_estoque = util.retornar_estoque()
            bebidas_estoque[ie]['qtd'] -= int(qtd)
            util.inserir_bebida_estoque(bebidas_estoque)

            vendas = util.retornar_vendas()
            vendas.append({'id': gerar_id(),
                           'data': gerar_data(),
                           'qtd': int(qtd),
                           'valor': int(qtd) * bebida.get_valor(),
                           'cod': codigo,
                           'cnpj': cnpj,
                           'vendedor': login})
            util.inserir_venda(vendas)
            return 2
        return 1
    return 0

def gerar_relatorio_dia(dia, mes, ano):
    if len(dia) == 2 and dia[0] == '0':
        dia = dia.replace('0', '')
    if len(mes) == 2 and mes[0] == '0':
        mes = mes.replace('0', '')
    if len(ano) == 2:
        ano = '{}{}'.format('20', ano)
    data = '{}/{}/{}'.format(dia, mes, ano)
    vendas = util.retornar_vendas()
    vendas_dia = list(filter(lambda v: v['data'] == data, vendas))
    if len(vendas_dia) > 0:
        return vendas_dia
    return ''

def gerar_relatorio_cliente(cnpj):
    cliente, i = percorrer_cliente(cnpj)
    if cliente:
        cnpj = cnpj_generator(cnpj)
        vendas = util.retornar_vendas()
        vendas_cliente = list(filter(lambda v: v['cnpj'] == cnpj, vendas))
        if len(vendas_cliente) > 0:
            return vendas_cliente, cliente
        return 1, None
    return 0, None

def gerar_relatorio_vendedor(login):
    vendedor = percorrer_funcionario(login, 1)
    if vendedor:
        vendas = util.retornar_vendas()
        vendas_vendedor = list(filter(lambda v: v['vendedor'] == login, vendas))

        if len(vendas_vendedor) > 0:
            return vendas_vendedor, vendedor
        return 1, None
    return 0, None

def gerar_relatorio_produto(codigo):
    bebida = percorrer_bebidas(codigo, 0)
    if bebida:
        vendas = util.retornar_vendas()
        vendas_bebida = list(filter(lambda v: v['cod'] == codigo, vendas))
        if len(vendas_bebida) > 0:
            return vendas_bebida, bebida
        return 1, None
    return 0, None