cpf = input("Informe o CPF com pontos e traçoes: \n")

antes_hifen, depois_hifen = cpf.split("-")
print ("Antes do hifen: ", antes_hifen)
print ("Depois do hifen: ",depois_hifen)
ponto1 = antes_hifen.index(".")
parte1 = antes_hifen[0:ponto1]
print ("Parte 1: ", parte1)
resto_parte1 = antes_hifen[ponto1+1:]
ponto2 = resto_parte1.index(".")
parte2 = resto_parte1[0:ponto2]
parte3 = resto_parte1[ponto2+1:]
print ("Parte 2: ", parte2)
print ("Parte 3: ", parte3)