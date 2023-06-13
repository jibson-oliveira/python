nome = input("Informe o nome do aluno: \n")

nota1 = float(input("Informe a nota do primeiro bimestre: \n"))
nota2 = float(input("Informe a nota do segundo bimestre: \n"))
nota3 = float(input("Informe a nota do terceiro bimestre: \n"))
nota4 = float(input("Informe a nota do quarto bimestre: \n"))

media = (nota1+nota2+nota3+nota4)/4

print ("A média do aluno %s é de %.1f" %(nome, media))