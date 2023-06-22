numeros = []
lista_repetidos = []
lista_unica = []

while True:
    numero = int (input("Informe um numero (zero para sair): \n"))
    if numero == 0:
        print ("Saindo do loop ... ")
        break
    else:
        numeros.append(numero)

for x in numeros:
    if x not in lista_unica:
        lista_unica.append(x)
    else:
        if x not in lista_repetidos:
            lista_repetidos.append(x)

if numeros:
    print ("Numeros informados: ", numeros)
    print ("Numeros sem repetição: ", lista_unica)
    print ("Somente números que não se repetiram: ", lista_repetidos)
else:
    print ("Nenhum número informado.")