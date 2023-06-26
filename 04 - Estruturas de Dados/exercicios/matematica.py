lista = []
soma = 0
multiplicacao = 1

while True:
    numero  = int (input("Digite um número inteiro (informe 0 para sair) :"))
    if numero == 0:
        break
    lista.append(numero)


if lista:
    for numero in lista:
        soma += numero
        multiplicacao *= numero

    lista.sort()
    menor = lista [0]
    maior = lista[len(lista)-1]

    print ("Soma :", soma)
    print ("Multiplicação: ", multiplicacao)
    print ("Maior: ", maior)
    print ("Menor: ", menor)
else:
    print ("Nenhum numero informado.")