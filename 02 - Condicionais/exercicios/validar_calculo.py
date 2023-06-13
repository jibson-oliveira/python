numero1 = float(input("informe o primeiro numero: "))
numero2 = float(input("informe o segundo numero: "))

mais = numero1 + numero2
menos = numero1 - numero2
vezes = numero1 * numero2
dividido = numero1 / numero2

soma = float(input(f"Informe o resultado da operação {numero1} + {numero2}: "))
if mais == soma:
    print ("Você acertou !!!")
else:
    print (f"Você errou. O resultado da operação {numero1} + {numero2} é {mais}")
subtracao = float(input(f"Informe o resultado da operação {numero1} - {numero2}: "))
if menos == subtracao: 
    print ("Você acertou !!!")
else:
    print (f"Você errou. O resultado da operação {numero1} - {numero2} é {menos}")
multiplicacao = float(input(f"Informe o resultado da operação {numero1} x {numero2}: "))
if multiplicacao == vezes: 
    print ("Você acertou !!!")
else:
    print (f"Você errou. O resultado da operação {numero1} x {numero2} é {vezes}")
divisao = float(input(f"Informe o resultado da operação {numero1} / {numero2}: "))
if divisao == dividido:
    print ("Você acertou !!!")
else:
    print (f"Você errou. O resultado da operação {numero1} / {numero2} é {dividido}")
