lista_palavras = []

while True:
    palavra = input("Informe uma palavra (zero pra sair):")
    if palavra == "0" or palavra.upper() == "ZERO":
        break
    else: 
        lista_palavras.append (palavra)


validacao = input("Informe a palavra que deseja contar: ")
quantidade = lista_palavras.count(validacao)


print (f"Temos {quantidade} ocorrências da palavra {validacao}.")