par = []
impar = []
numeros = []


while True:
    numero = int(input("Informe um número (zero para sair): "))
    if numero == 0:
        break
    numeros.append(numero)
    
    
for numero in numeros:
    if numero % 2 == 0:
        par.append(numero)
    elif numero %2 == 1:
        impar.append(numero)


print("Pares: ", par)
print("Ímpares: ", impar)