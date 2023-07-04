'''
Set (conjunto) é uma sequencia mutável não ordenada e que não possui elementos duplicados.
Os sets suportam operações matemáticas como união, interseção e diferença

Sintaxe:
variavel = {a, b, ..., z}
set()

'''

# Criando um conjunto com valores
conjunto_numeros = {10,20,30,40,50,60}

''' Para criar um conjunto vazio não podemos usar:
conjunto = {} -> Chaves vazias criam um dicionário
'''

#Forma correta de criar um conjunto vazio.
conjunto = set()

# Os valores do set não se repetem.
conjunto_numeros = {10,30,40,10,42,42,56}
print ("conjunto_numeros: ",conjunto_numeros)

#Uma lista pode ser convertida em um conjunto

lista_frutas = ["Abacaxi", "Abacaxi", "Laranja", "Maçã", "Abacaxi"]
conjunto_frutas = set(lista_frutas)
print ("Conjunto_frutas: ", conjunto_frutas)

#União

conjunto_uniao = conjunto_frutas.union(conjunto_numeros)
print ("conjunto_uniao: ",conjunto_uniao)


#Diferença

conjunto_diferenca = conjunto_uniao.difference(conjunto_numeros)
print ("conjunto_diferenca: ", conjunto_diferenca)


# Interseção

conjunto1 = {10,42,50, "Python", "Programação"}
conjunto2 = {10, "Python", 42, "Java", "Bicileta", "Carro"}
conjunto_intersecao = conjunto1.intersection(conjunto2)
print(f"conjunto_interseção:{conjunto_intersecao} ")

# Testando se um set inclui outro set

linguagens = {"Python", "Java", "C++"}
linguagem = {"Python"}

if linguagens.issuperset(linguagem):
    print ("O conjunto de linguagens possui o conjunto linguagem.")
else:
    print("O conjunto de linguagens não possui o conjunto liguagem")

linguagem = {"Ruby"}
if linguagens.issuperset(linguagem):
    print ("O conjunto de linguagens possui o conjunto linguagem.")
else:
    print("O conjunto de linguagens não possui o conjunto liguagem")



# Testando se um set está incluso em outro set

linguagem = {"Python"}
if linguagem.issubset(linguagens):
    print ("O conjunto linguagem está no conjunto de linguagens.")
else:
    print("O conjunto liguagem não está no conjunto de linguagens")


linguagem = {"Ruby"}
if linguagem.issubset(linguagens):
    print ("O conjunto linguagem está no conjunto de linguagens.")
else:
    print("O conjunto liguagem não está no conjunto de linguagens")


#Verificando se um set não possui elementos comuns a outros set
linguagens1 = {"Python", "C++", "Assembly"}
linguagens2 = {"Pascal","Ruby","C"}
if linguagens1.isdisjoint(linguagens2):
    print ("Os conjuntos não possuem elementos em comum")
else:
    print ("Os conjuntos possuem elementos em comum")


linguagens2 = {"Pascal","Ruby","C", "Python"}
if linguagens1.isdisjoint(linguagens2):
    print ("Os conjuntos não possuem elementos em comum")
else:
    print ("Os conjuntos possuem elementos em comum")