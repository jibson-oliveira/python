# Funções

Funções são blocos de códigos que possuem um nome e podem ou não receber parâmetros.
Para criar uma função usamos a instrução def

Sintaxe:
**def nome(*parâmetros*):**
    **bloco de código**

O bloco de código da função não é executado enquando a mesma não for chamada.



#### Criando uma função:
~~~python
def soma ():
    numero1 = 10
    numero2 = 25
    total = numero1+numero2
    print (f'Numero total é igual a : {total}')

soma ()
~~~

#### Passando parâmetros
~~~python
def soma (numero1,numero2):
    total = numero1+numero2
    print (f'Numero total é igual a : {total}')

soma (10,20)
~~~


#### Indicando um valor de retorno usando return.
~~~
def soma (numero1,numero2):
    resultado = numero1+numero2
    return resultado


total = soma (30,40)
print (f'Resultado: {total}')
~~~

#### Uma função que chama outra função
~~~python
def maior_valor (valores):
    return max(valores)

def capturar_numeros():
    lista_numeros = []
    while True:
        numero = int(input("Informe um número inteiro ou zero para sair: "))
        if numero == 0:
            break
        lista_numeros.append(numero)
    return maior_valor(lista_numeros)

print (f'Maior valor = {capturar_numeros()}')
~~~
## Variáveis locais e globais


***Variavel local***, declarada dentro de uma função, existe apenas dentro desta função, sendo inicializada a cada 
chamada à função.
Desta forma, ela não é visivel fora da função.
***Variável global*** é definida fora de uma função, podendo ser vista por todas as funções do módulo
e por todos os módulos que importam o módulo que a definiu

~~~python
valor = 100.00 # Variável global
def calculo():
    valor = 50.00 # Variável local
    print (f'Valor dentro da função (local): {valor}')

print (f'Valor fora da função (global): {valor}')
calculo()
print (f'Valor fora da função (global): {valor}')


valor = 100.00 # Variável global
def calculo():
    global valor # Variável global
    valor = 50.00
    print (f'Valor dentro da função (local): {valor}')

print (f'Valor fora da função (global): {valor}')
calculo()
print (f'Valor fora da função (global): {valor}')
~~~

O escopo de nomes em Python é mantido por meio de namespaces, que são dicionários que relacionam os nomes dos objetos (referências) e os objetos em si.
Os nomes ficam definidos em dois dicionários que podem ser consultados utilizando-se as funções **locals()** e **globals()**. Estes dicionários são atualizados em tempo de execução

Variáveis globais devem ser utilizadas o mínimo possível, pois dificultam a leitura e violam o encapsulamento da função.
A dificuldade de leitura se dá pelo fato de que devemos ficar procurando as variáveis e conteúdos fora da função.
A variável global pode ter seu conteúdo alterado por qualquer função, desta forma fica difícil saber qual função alterou.
O encapsulamento é comprometido porque a função precisa de uma variável externa. Uma variável que não é declarada dentro da função e não é recebida por parâmetro.

Um bom uso de variáveis globais é utilizando as mesmas como constantes. Sempre que várias funções precisem de uma informação que é fixa, podemos criar constantes globais. Por boas práticas, normalmente criamos constantes em maiúsculas


```python
TAXA_JUROS = 1.2 / 100

def calculo1 (num1, num2):
    total = num1 + num2
    total += total * TAXA_JUROS
    print (f"Calculo1: {total}")

def calculo2 (num1):
    total = 0
    for numero in num1:
        total += numero
    total += total * TAXA_JUROS
    print (f"Calculo2: {total}")

calculo1 (10,35)
valores = [10, 58.74, 65.41, 80]
calculo2(valores)
```


## Parâmetros de Funções

Parâmetros ou argumentos de funções são essenciais para que possamos chamar funções informando valores.
Desta forma, tornamos as funções flexíveis, recebendo valores diferentes a cada execução

Funções sem parâmetros não são flexiveis.
Ex: 
~~~python
def soma(): 
    valor1 = 10
    valor2 = 25
    return valor1 + valor2

total = soma()
print(f"O total é: {total})
~~~
Toda vez que a soma anterior for executada, retornará o mesmo valor de 35

#### Função com parâmetros opcionais
~~~python
def soma(valor1, valor2, imprime = False): # valor1 e valor2 são obrigatórios, imprime é opcional por que foi definida como falso
    resultado = valor1 + valor2
    if imprime:
        print(f"Soma: {resultado}")
    return resultado

total = soma(10,84) # resultado 94 não será impresso
total = soma(11,84,True) # resultado 95 será impresso
~~~

Parametros opcionais não podem estar no início caso seja combinado com parâmetros obrigatórios 

#### Nomeando Parâmetros.
Quando informamos o nome do parâmetro, não importa a ordem em que passamos os mesmos
```python
def retangulo (largura, altura, caractere="*"):
    linha = caractere * largura
    for i in range(altura):
        print(linha)

retangulo(caractere="&", altura = 5, largura = 15)
```

#### Funções como parâmetros
```python
def soma(valor1, valor2):
    return valor1+valor2

def multiplicacao(valor1,valor2):
    return valor1*valor2

def calcular(funcao, num1, num2):
    return funcao(num1,num2)

total = calcular(soma, 10, 25)
print(f"Soma: {total}")

total = calcular(multiplicacao, 10, 100)
print(f"Mutiplicacao: {total}")
```

#### Parâmetros empacotados em listas
```python
 
lista = [10,20,True]

def soma(valor1, valor2, imprime = False): 
    resultado = valor1 + valor2
    if imprime:
        print(f"Soma: {resultado}")
    return valor1 + valor2

soma(*lista) # O asterisco indica que estamos desempacotando a lista utilizando seus valores como parâmetros da função
```

#### Desempacotamento de parâmetros
```python
def soma (imprime, *valores):
    total = 0
    for valor in valores:
        total += valor
    if imprime:
        print(f"Soma: {total}")
    return total

soma(True, 10,20,30,78)
soma(False, 10, 50)
```
