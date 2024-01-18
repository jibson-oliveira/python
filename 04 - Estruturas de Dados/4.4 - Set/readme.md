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