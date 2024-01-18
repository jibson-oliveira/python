
## Listas

Listas são coleções de objetos que podem ser de qualquer tipo, inclusive outras listas
 * As listas em Python são mutaveis, podendo ser alteradas a qualquer momento
 * Listas podem ser fatiadas como strings
 * Os valores de uma lista podem ser acessados pelo seu indice
 * Uma lista pode conter zero ou mais elementos
 * o tamanho de uma lista é igual a sua quantidade de elementos


#### Criando uma lista com 3 inteiros
```
lista_numeros = [25, 78, 55]
print(lista_numeros)
print (lista_numeros[1])
```

```
# Alterando o valor do primeiro indice da lista anterior
lista_numeros[1] = 30
print(lista_numeros)
print (lista_numeros[1])
```

```
# Acessando os elementos para calcular a média
notas = [7.5, 5.6, 9.5 ,10]
media = (notas[0]+notas[1]+notas[2]+notas[3])/4
print (media)
```

Assim como no fatiamento de string, o ultimo elemento de uma lista pode ser acessado pelo índice -1.

```
print (notas[-1])
```
#### Incrementando valores a uma lista

Incrementando valores utilizando o sinal de soma
```
lista_numeros = [2]
print (lista_numeros)
lista_numeros = lista_numeros + [4, 6, 8, 10]
print(lista_numeros)
```
Podemos utilizar também o operador de atribuição "+=";
O operador de atribuição "+=" adiciona o operando direito ao operando esquerdo e atribui o resultado ao operando esquerdo
```
numeros = [1,2,33,10,1000]
numeros += [8,7,9]
print (numeros)
```

#### Adicionando um item a lista utilizando o método **append**
```
cidades = ["Salvador", "Recife", "Fortaleza"]
cidades.append ("São Paulo")
print (cidades)
```
#### Adicionando um item à lista definindo um índice específico utilizando o método **insert**
O método insert permite que possamos o item em uma posição específica
```
cidades = ["Salvador", "Recife", "Fortaleza"]
# Adicionando Palmas no indice 2
cidades.insert(2,"Palmas")
print (cidades)
```
#### Removendo um elemento da lista com o método **remove**
```
cidades = ["Salvador", "Recife", "Fortaleza","São Paulo"]
cidades.remove("São Paulo")
print (cidades)
```
#### Para ordenar os itens de uma lista, usamos o método **sort**
```
cidades = ["Salvador", "Recife", "Fortaleza","São Paulo"]
cidades.sort()
print (cidades)
```

#### Para inverter a ordem dos itens de uma lista, usamos o método **reverse**
```
cidades = ["Salvador", "Recife", "Fortaleza","São Paulo"]
cidades.reverse()
print (cidades)
```
#### Removendo o último elemento de uma lista com o método **pop**
```
cidades = ["Salvador", "Recife", "Fortaleza","São Paulo"]
excluida = cidades.pop()
print (cidades)
print (excluida)
```

#### Retornando a quantidade de ocorrências de um elemento com o método **count**
```
letras = ["a", "b", "c", "a", "e", "i"]
qtd_a = letras.count("a")
print (letras)
print (f"Quantidade de letras 'a': {qtd_a}")
```
#### Removendo elementos de uma lista com a função *del*
```
idiomas = ["inglês", "espanhol", "frances", "alemão","português","mandarim"]
print (idiomas)
del idiomas[3] # Removido o idioma 'alemão'
print (idiomas)
del idiomas[1:4] # removendo com fatiamento os idiomas espanhol, francês e português
print (idiomas)
```
#### Limpando uma lista inteira com o método **clear**
```
lista_livros = ['livro 1', 'livro 2', 'livro 3']
print (lista_livros)
lista_livros.clear()
print (lista_livros)
```

```
lista_livros = ['livro 1', 'livro 2', 'livro 3']
print (lista_livros)
lista_livros = []
print (lista_livros)
```
#### Usando uma lista dentro de outra lista
```
lista = [10, 13, 17, ["Maçã", "Banana","Limão"]]
print(lista)
# Resultado: [10, 13, 17, ["Maçã", "Banana","Limão"]]
frutas = lista[3]
print (frutas)
# Resultado: ["Maçã", "Banana","Limão"] ->  É impresso a lista como o indice 3
soma = lista [0] + lista [1] + lista [2]
print (soma)
# Resultado: 40
```
#### Obtendo o tamanho de uma lista

```
lista = [100,700,1000,4583,0]
tamanho = len(lista)
print (tamanho)
```

#### Obtendo o indice de um determinado elemento da lista
```
linguagens = ["Java", "Pyhton", "Ruby", "Go", "C#", "C++"]
print (linguagens.index("Python"))
```
#### Verificando a existência de um item na lista
```
linguagens = ["Java", "Pyhton", "Ruby", "Go", "C#", "C++"]
linguagem = input("Informe a linguagem: ")
if linguagem.upper() in linguagens:
    print (f"{linguagem.upper()} está na lista.)
else:
    print (f"{linguagem.upper()} não está na lista.) 
```

#### Adicionando elemento fornecidos pelo usuário à lista
```
lista = []
while True:
    numero = int(input("Digite um número inteiro (informe 0 para sair): "))
    if numero == 0:
        break
    lista.append(numero)

for num in lista:
    print(num)
```
#### Exemplos:
##### Separando Pares e Ímpares:
```
lista_pares = []
lista_impares = []

while True:
    numero = int (input("Digite um numero inteiro (informe 0 para sair): "))
    if numero == 0:
        break
    if numero % 2 == 0:
        lista_pares.append(numero)
    else
        lista_impares.append(numero)

lista_pares.sort()
lista_impares.sort()

print(f"Números pares: {lista_pares}")
print(f"Números ímpares: {lista_impares}")
```

#### Enumerate
O **enumerate** adiciona um contador a um objeto iterável. Uma lista é um objeto iterável

**Sintaxe:**
*enumerate(objeto_iterável,inicio)*

Se o início for omitido, será iniciado com zero

```
estacoes = ["Primavera", "Verão", "Outono", "Inverno"]
lista_estacoes = list(enumerate(estacoes))
print (lista_estacoes)
# Resultado: [(0,'Primavera),(1,'Verão'),(2,'Outono'),(3,'Inverno')]

lista_estacoes = list(enumerate(esacoes, start=5))
print(lista_estacoes)
# Resultado: 
[(5,'Primavera),(6,'Verão'),(7,'Outono'),(8,'Inverno)]
```


