## Set

Set (conjunto) é uma sequência mutável não ordenada e que não possui elementos duplicados.
Os sets suportam operações matemáticas como união, interseção e diferença.

**Sintaxe**
***variavel = {a,b,..,z}***
***set ()***

#### Criando o conjunto
Criando um conjunto com valores
```conjunto_numeros = {10, 20, 30, 40, 50, 60}```

**Obs:** Para criar um conjunto vazio não podemos usar:
```conjunto = {}```
Chaves vazias criam um dicionário

**Forma correta de criar um conjunto vazio.
```conjunto = set()```

Os valores do set não se repetem.
```
conjunto_numeros = {10,30,40,20,10,15,30,0}
print("conjunto_numeros: ", conjunto_numeros)
conjunto_numeros:  {0, 20, 40, 10, 30, 15}
```

#### Uma lista pode ser convertida em um conjunto.
```
lista_frutas = ["Abacaxi", "Abacaxi", "Laranja", "Maçã", "Abacaxi"]
conjunto_frutas = set(lista_frutas)
print("conjunto_frutas: ", conjunto_frutas)
```

#### União
```
conjunto_cores = {"Azul", "Azul", "Amarelo", "Verde", "Vermelho", "Branco", "Verde"}
conjunto_carros = {"Gol", "Celta", "Clio", "Uno", "Uno", "Palio"}
conjunto_uniao = conjunto_cores.union(conjunto_carros)
print (conjunto_uniao)
```

#### Diferença
```
conjunto_diferenca = conjunto_uniao.difference(conjunto_carros)
print(conjunto_diferenca)
```

#### Interseção
```
conjunto_pares = {2,4,6,8,10,12,14,16,18,20}
conjunto_multiplos_5 = {5,10,15,20}
conjunto_intersecao = conjunto_pares.intersection(conjunto_multiplos_5)
print (conjunto_intersecao)
```

#### Testando se um **set** inclui outro **set**

```
linguagens = {"Python", "Java", "C++"}
linguagem = {"Python"}
if linguagens.issuperset(linguagem):
    print("O conjunto de linguagens inclui o conjunto linguagem.")
else:
    print ("O conjunto de linguagens não inclui o conjunto linguagem.")

linguagem = {"Ruby"}
if linguagens.issuperset(linguagem):
    print("O conjunto de linguagens inclui o conjunto linguagem.")
else:
    print ("O conjunto de linguagens não inclui o conjunto linguagem.")
```

#### Testando se um **set** está incluso em outro **set**

```
linguagens = {"Python", "Java", "C++"}
linguagem = {"Python"}
if linguagem.issubset(linguagens):
    print("O conjunto de linguagens está incluso no conjunto linguagem.")
else:
    print ("O conjunto de linguagens não está incluso no conjunto linguagem.")

linguagem = {"Ruby"}
if linguagem.issubset(linguagens):
    print("O conjunto de linguagens está incluso no conjunto linguagem.")
else:
    print ("O conjunto de linguagens não está incluso no conjunto linguagem.")
```

