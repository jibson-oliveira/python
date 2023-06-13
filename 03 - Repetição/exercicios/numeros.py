total = 0
quant_numeros = int(input("Informe a quantidade de numeros a serem digitados: (de 1 a 9)\n"))
if quant_numeros > 9 or quant_numeros < 1:
    print ("Quantidade de números invalida!")
else:
    x = 1
    while x <= quant_numeros:
        numero = int(input(f"Informe o {x}º numero: "))
        produto = numero * x
        total = total + produto
        x = x + 1

print (f"Total: {total}")