texto1 = input ("Informe o primeiro texto: ")
texto2 = input ("Informe o segundo texto: ")

print (texto1)
print (texto2)

print ("A quantidade de caracteres de %s é %d ." %(texto1, len(texto1)) )
print ("A quantidade de caracteres de %s é %d ." %(texto2, len(texto2)) )

print ("As strings possuem a mesma quantidade de caracteres ?", len(texto1)==len(texto2))
print ("As strings são iguais ?", texto1==texto2)