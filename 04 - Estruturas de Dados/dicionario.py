'''
Dicionários são estruturas de dados similares às listas, porém com propriedades de acesso diferentes.
Um dicionário consiste em um conjunto de chaves e valores.
Sintaxe:
dicionario ={'a':a,'b':b,...,'z':z}
dicionario = {chave:valor, chave:valor}

Assim como as listas, os dicionários são mutaveis, mas suas chaves devem ser de um tipo imutável
Para criar listas usamos colchetes "[]", para criar tuplas, usamos parênteses "()", para criar dicionários usamos 
chaves "{}"

'''

#Criando o dicionário
carros = {'marca': 'VW', 'modelo':'Gol', 'ano_modelo':2016}
#Acessando seus elementos
print (f'O ano do modelo do carro é: {carros["ano_modelo"]}')
print (f"A marca do carro é: {carros['marca']}")

# Para adicionar/alterar elementos ao dicionário usamos: 
# dicionario["chave"] = valor

carros['ano_modelo'] = 2017
print (f'O ano do modelo do carro é: {carros["ano_modelo"]}')


# Para apagar um elemento de um dicionario usamos: del dicionario["chave"]

del carros['modelo']
print (f'Removido o modelo: {carros}')


'''Para apagar todos os elementos do dicionario usamos:

dicionario.clear()

O dicionário continuará existindo, porém vazio

Para apagar todo o dicionario usamos:

del dicionario
'''

dicionario = {'teste1':1, 'teste2':2}
print (dicionario)
dicionario.clear()
print (dicionario)
del dicionario


''' 
Obtendo itens, chaves e valores de um dicionario:

key(), itens() e values retornam views ou visualizações, que são iteradores dos tipos
dict_keys, dict_items e dict_values, que devolvem um elemento de cada vez
'''

carros = {'marca':'VW', 'modelo':'Gol', 'ano_modelo':2016}
print (f'Itens do dicionário carros: {carros.items()}')
print (f'Chaves do dicionário carros: {carros.keys()}')
print (f'Valores do dicionário carros: {carros.values()}')

# Copiando um dicionario para outro

dic1 = {'nome':'Fulano', 'sobrenome':'De Tal'}
dic2 = dic1.copy()
print (f'dic1: {dic1}')
print (f'dic2: {dic2}')