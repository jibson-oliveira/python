## Tuplas

* São semelhantes às listas, porém, são imutáveis. 
* Não podemos acrescentar, apagar ou fazer atribuições aos seus itens.
* As tuplas são criadas usando se parênteses em vez de colchetes, porém, os parênteses não são obrigatórios.

**Sintaxe**
*tupla =(a, b,..., z) ou tupla = a, b, ..., z'''*

#### Veja a criação de tuplas com e sem parênteses:
```
linguagens = (" Assembly", " Cobol", " C", "C++")
print (linguagens)

linguagens = " Python", " Java", " Go", "C#"
print (linguagens)
```

#### É possível criar uma tupla vazia.
```
vazio = ()
print (vazio)
```

#### Tuplas com um único elemento
Para criar uma tupla com um único elemento, devemos colocar a virgula. Caso contrario, o Python entende que você está criando uma variavel
**Maneira incorreta**
```
tupla1 = (1) 
print (tupla1) # o Python entende que você criou uma variavel chamada tupla1 e deu o valor de 1 para ela
```

**Maneira correta**
```
tupla1 = (1,)
print (tupla1)
```

Podemos acessar os elementos da tupla pelo índice e usar fatiamento
```
paises = "Brasil", "Paraguai", "Uruguai", "México"
pais = paises[0]
print (pais)
fatia = paises[1:3]
print (fatia)
```

Se tentarmos alterar um item da tupla, é gerado o erro “O objeto não suporta a atribuição de itens”
```
paises = "Brasil","Paraguai "," Uruguai","Mexico"
paises [1] = "Colômbia"
Traceback (most recent call last):
File “ “.../tupla.py", line 2 , in <module>
paises[1] = Colômbia
TypeError: 'tuple' object does not support item assignment
```

Podemos imprimir os elementos de uma tupla usando o comando for '''
```
for pais in paises:
    print (pais)
```

#### Podemos também converter uma lista em uma tupla.
```
lista_carros = ["Gol","Corolla","Ranger","Kadett","Fusca","Clio"]
tupla_carros = tuple(lista_carros)
print (f"Tupla Carros: {tupla_carros}")
```

#### Também podemos converter uma tupla em lista

```
lista_carros = list(tupla_carros)
print(f"Lista carros: {lista_carros}")
```

#### Desempacotando elementos da tupla

```
tupla_carros = "Golf", "Civic", "HB20"
carro1, carro2, carro3 = tupla_carros
print(f"Carro 1: {carro1}")
print(f"Carro 2: {carro2}")
print(f"Carro 3: {carro3}")
```

#### Desempacotando vários elementos para uma lista usando atribuição múltipla

```
tupla_carros = "Golf", "Corolla", "Civic", "Opala", "Tucson", "Elantra"
carro1, *carros = tupla_carros
print (f"Carro 1: {carro1}")
print (f"Carros: {carros}")
```
Ao utilizarmos a atribuição multipla, nós transformamos a tupla em uma lista


#### Uma lista como elemento de uma tupla
```
>>> tupla = ("Python", 10.25, 36, ["Ônibus", "Avião", "Navio", "Carro"])
>>> tupla[0]
'Python'
>>> tupla[1]
10.25
>>> tupla[2]
36
>>> tupla[3]
['Ônibus', 'Avião', 'Navio', 'Carro']
>>> lista = tupla[3]
>>> lista
['Ônibus', 'Avião', 'Navio', 'Carro']
>>> 

```

