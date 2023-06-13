''' - Listas são coleções de objetos que podem ser de qualquer tipo, inclusive outras listas
 - As listas em Python são mutaveis
 - Listas podem ser fatiadas como strings
 - Os valores de uma lista podem ser acessados pelo seu indice
 - Uma lista pode conter zero ou mais elementos
 - o tamanho de uma lista é igual a sua quantidade de elementos

'''
# Criando uma lista com 3 inteiros
lista_numeros = [25, 78, 55]
print(lista_numeros)
print (lista_numeros[1])

lista_numeros[1] = 30
print(lista_numeros)
print (lista_numeros[1])

notas = [7.5, 5.6, 9.5 ,10]
media = (notas[0]+notas[1]+notas[2]+notas[3])/4
print (media)

print (notas[-1])


lista_numeros = [2]
print (lista_numeros)
lista_numeros = lista_numeros + [4, 6, 8, 10]
print(lista_numeros)


cidades = ["Salvador", "Recife", "Fortaleza"]
cidades.append ("São Paulo")
print (cidades)

cidades.insert(2,"Palmas")
print (cidades)

cidades.remove("São Paulo")
print (cidades)

cidades.sort()
print (cidades)

cidades.reverse()
print (cidades)

excluida = cidades.pop()
print (cidades)
print (excluida)


letras = ["a", "b", "c", "a", "e", "i"]
qtd_a = letras.count("a")
print (letras)
print (f"Quantidade de letras 'a': {qtd_a}")



idiomas = ["inglês", "espanhol", "frances", "alemão","português","mandarim"]
print (idiomas)
del idiomas[3]
print (idiomas)
del idiomas[1:4]
print (idiomas)