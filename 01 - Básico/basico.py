print ("O resultado de 10 + 25 é: ", 10+25)
print ("O resultado de 20 - 15 é: ", 20-15)
print ("O resultado de 18 X 2 é: ", 18*2)
print ("O resultado de 58 / 3 é: ", 58/3)
print ("O resultado de 58 // 3 é: ", 58//3)



#Concatenação

texto1 = "Olá, "
texto2 = "tudo bem ?"
texto_concatenado = texto1 + texto2
print (texto_concatenado)

#Multiplicando strings
alimento = "pão "
multiplica = alimento * 10
print (multiplica)

''' Composição ou Interpolação

%s -> String
%d -> Inteiro
%f -> float ou real
%% -> simbolo porcento '''

nome = "Jibson"
idade = 35
filhos = 1
frase = "O %s tem %d anos de idade e tem %d filhos." %(nome, idade, filhos)
print(frase)

valor_unitario = 165.78
quantidade = 5
valor_total = valor_unitario*quantidade
frase = "O produto custa R$ %.2f. Eu comprei %d unidades. Paguei um valor de R$ %.2f " % (valor_unitario, quantidade, valor_total)
print (frase)

# Utilizando format

nome = "Danilo"
idade = 33
filhos = 2
frase = "O {} tem {} anos de idade e tem {} filhos." .format(nome, idade, filhos)
print(frase)

frase = "Olá. Iremos viajar de {3}". format('carro', 'ônibus', 'trem' , 'avião',)
print (frase)

#Fatiamento

endereco = "www.python.org"
fatia = endereco[4:10]
print (fatia)
salto_de_2 = endereco[::2]
print (salto_de_2)
salto_menos_1 = endereco[::-1]
print (salto_menos_1)
comeco = endereco[:10]
fim = endereco[10:]
print (comeco)
print (fim)
fatia2 = endereco[-10:-4]
print (fatia2)


# Index e Split

email = "cilvioster@gmail.com"
usuario, dominio = email.split("@")
print ("O nome de usuario é %s." %usuario)
print (f"O dominio do e-mail é {dominio}." )
ponto = dominio.index(".")
provedor = dominio[0:ponto]
print ("O provedor do e-mail é {}" .format(provedor))