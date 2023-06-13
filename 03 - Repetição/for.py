''' Estruturas de Repetição

São utilizadas executar a mesma parte de um programa várias vezes 

Estrutura: 
for 'referencia' in 'sequencia' : 
    bloco de código
'''

numeros = [0, 18, 56, 77, 95]
for numero in numeros:
    print (numero)


for letras in "Python":
    print (letras)
else:
    print ("Acabou!")


for numero in range (10000):
    print (numero)
    if numero == 4:
        break # comando 'break' serve pra sair da estrutura do for
print ("Até mais !")

# Quando o 'break' é usado, o conteudo do else não é executado

numeros = [1, 2, 3, 10, 12]
for numero in numeros:
    if numero == 10:
        break
    print (f"Número: {numero}")
else:
    print ("Acabou")

# Para passar para a próxima iteração podemos usar o 'continue'.

for x in [1, 10, 20, 30, 40, 50]:
    if x == 30:
        continue
    print (x)


''' Range é uma função que gera uma lista de numeros.

Sintaxe : range(inicio, fim, salto)

Inicio e salto são opcionais, se não for informado o inicio, será considerado o inicio em zero, se não 
for informado o salto, será incrementado em 1

Exemplo:
range (3), resulta em [0,1,2]
range (0,10,2) resulta em [0,2,4,6,8]: Inicia em zero e salta de 2 em 2 até 9 pois é um intervalo aberto'''

for num in range (5,30,5):
    print (num)