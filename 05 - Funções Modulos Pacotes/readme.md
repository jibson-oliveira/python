# Funções

Funções são blocos de códigos que possuem um nome e podem ou não receber parâmetros.
Para criar uma função usamos a instrução def

Sintaxe:
def nome(parâmetros):
    bloco de código

O bloco de código da função não é executado enquando a mesma não for chamada.



### Criando uma função:
~~~python
def soma ():
    numero1 = 10
    numero2 = 25
    total = numero1+numero2
    print (f'Numero total é igual a : {total}')

soma ()
~~~

### Passando parâmetros
~~~python
def soma (numero1,numero2):
    total = numero1+numero2
    print (f'Numero total é igual a : {total}')

soma (10,20)
~~~


### Indicando um valor de retorno usando return.
~~~
def soma (numero1,numero2):
    resultado = numero1+numero2
    return resultado


total = soma (30,40)
print (f'Resultado: {total}')
~~~

### Uma função que chama outra função
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



Variavel local, declarada dentro de uma função, existe apenas dentro desta função, sendo inicializada a cada 
chamada à função.
Desta forma, ela não é visivel fora da função.
Uma variável global é definida fora de uma função, podendo ser vista por todas as funções do módulo
e por todos os módulos que importam o módulo que a definiu

~~~python
valor = 100.00
def calculo():
    valor = 50.00
    print (f'Valor dentro da função (local): {valor}')

print (f'Valor fora da função (global): {valor}')
calculo()
print (f'Valor fora da função (global): {valor}')


valor = 100.00
def calculo():
    global valor
    valor = 50.00
    print (f'Valor dentro da função (local): {valor}')

print (f'Valor fora da função (global): {valor}')
calculo()
print (f'Valor fora da função (global): {valor}')
~~~