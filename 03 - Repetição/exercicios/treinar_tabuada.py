i = 1
y=0
z=0
numero = int(input("Informe o numero para o qual deseja treinar a tabuada: "))
while i <= 10:
    x = numero * i
    resposta = int(input(f"Qual o valor de {numero} x {i} ? "))
    if resposta == x:
        print ("Correto")
        y = y+1
    else:
        print (f"Que pena. Você errou! O valor correto é {x}. ")
        z = z +1
    i= i+1

print (f"Total de acertos: {y} \n"
       f"Total de erros: {z} \n"
       )