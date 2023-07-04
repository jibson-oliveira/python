lista = []

while True:
    palavra = input("Informe uma palavra (digite 0 para sair): ")
    if palavra == "0":
        print ("Saindo do loop...")
        break
    else:
        lista.append(palavra)

conjunto = set(lista)
print(conjunto)