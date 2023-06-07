aluno = input ("Informe o nome do aluno: \n")
nota1 = int (input("Informe o valor da nota do primeiro bimestre: "))
nota2 = int (input("Informe o valor da nota do segundo bimestre: "))
nota3 = int (input("Informe o valor da nota do terceiro bimestre: "))
nota4 = int (input("Informe o valor da nota do quarto bimestre: "))

media = (nota1+nota2+nota3+nota4)/4

if media < 5:
    resultado = ("reprovado")
    print (f"O aluno {aluno} está {resultado}. Sua média foi {media}")

elif media >= 5 and media <= 7:
    resultado = ("em recuperação")
    print (f"O aluno {aluno} está {resultado}. Sua média foi {media}")

else: 
    resultado = ("aprovado")
    print (f"O aluno {aluno} está {resultado}. Sua média foi {media}")
