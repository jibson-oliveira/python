while True:
    numero = input ("Informe um numero ou digite 'sair' para sair: \n")
    if numero.lower() == "sair":
        print ("Sistema Finalizado")
        break
    else:
        if int(numero) % 2 == 0:
            print (f"O numero {numero} é par! ")
        elif int(numero) % 2 != 0:
            print (f"O numero {numero} é impar!")

