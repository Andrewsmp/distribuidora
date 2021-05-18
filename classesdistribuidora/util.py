import json

def retornar_funcionarios():
    with open('classesdistribuidora/funcionario.json', 'r') as file:
        return json.load(file)

def inserir_funcionario(usuarios):
    with open('classesdistribuidora/funcionario.json', 'w') as file:
        json.dump(usuarios, file, indent=4)

def retornar_enderecos():
    with open('classesdistribuidora/endereco.json', 'r') as file:
        return json.load(file)

def inserir_endereco(enderecos):
    with open('classesdistribuidora/endereco.json', 'w') as file:
        json.dump(enderecos, file, indent=4)

def inserir_bebida(bebidas):
     with open('classesdistribuidora/bebida.json', 'w') as file:
        json.dump(bebidas, file, indent=4)

def retornar_bebidas():
    with open('classesdistribuidora/bebida.json', 'r') as file:
        return json.load(file)

def retornar_estoque():
    with open('classesdistribuidora/estoque.json', 'r') as file:
        return json.load(file)

def inserir_bebida_estoque(bebidas_estoque):
     with open('classesdistribuidora/estoque.json', 'w') as file:
        json.dump(bebidas_estoque, file, indent=4)

def retornar_cliente():
    with open('classesdistribuidora/cliente.json', 'r') as file:
        return json.load(file)

def inserir_cliente(clientes):
     with open('classesdistribuidora/cliente.json', 'w') as file:
        json.dump(clientes, file, indent=4)

def retornar_vendas():
    with open('classesdistribuidora/vendas.json', 'r') as file:
        return json.load(file)

def inserir_venda(vendas):
     with open('classesdistribuidora/vendas.json', 'w') as file:
        json.dump(vendas, file, indent=4)