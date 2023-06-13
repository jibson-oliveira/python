print ("*"*28+"CALCULO DO IMC"+"*"*28)
print ("Condição                     IMC em Mulheres             IMC em Homens")
print ("abaixo do peso                   <19,1                       <20,7")
print ("peso normal                   19,1 - 25,8                 20,7 - 26,4")
print ("marginalmente acima do peso   25,8 - 27,3                 26,4 - 27,8")
print ("acima do peso ideal           27,3 - 32,3                 27,8 - 31,1")
print ("obeso                            >32,3                       > 31,1")

nome = input ("Informe o seu nome: \n")
sexo = input ("Informe o seu sexo: (M para Masculino e F para Feminino): \n")
peso = float (input("Informe o seu peso em Kg: \n"))
altura = float (input ("Informe sua altura em metros: \n"))

imc = peso / (altura * altura)

if sexo == "M":
    if imc < 20.7:
        condicao = "abaixo do peso"
        print (f"{nome}, com base no peso e altura informados, o IMC é {imc:.1f} e a condição é {condicao} \n")
    elif 20.7 < imc < 26.4:
        condicao = "peso normal"
        print (f"{nome}, com base no peso e altura informados, o IMC é {imc:.1f} e a condição é {condicao} \n")
    elif 26.4 < imc < 27.8:
        condicao = "marginalmente acima do peso"
        print (f"{nome}, com base no peso e altura informados, o IMC é {imc:.1f} e a condição é {condicao} \n")
    elif 27.8 < imc < 31.1:
        condicao = "acima do peso ideal"
        print (f"{nome}, com base no peso e altura informados, o IMC é {imc:.1f} e a condição é {condicao} \n")
    elif imc > 31.1:
        condicao = "obeso"
        print (f"{nome}, com base no peso e altura informados, o IMC é {imc:.1f} e a condição é {condicao} \n")
    
if sexo == "F":
    if imc < 19.1:
        condicao = "abaixo do peso"
        print (f"{nome}, com base no peso e altura informados, o IMC é {imc:.1f} e a condição é {condicao} \n")
    elif 19.1 < imc < 25.8:
        condicao = "peso normal"
        print (f"{nome}, com base no peso e altura informados, o IMC é {imc:.1f} e a condição é {condicao} \n")
    elif 25.8 < imc < 27.3:
        condicao = "marginalmente acima do peso"
        print (f"{nome}, com base no peso e altura informados, o IMC é {imc:.1f} e a condição é {condicao} \n")
    elif 27.3 < imc < 32.3:
        condicao = "acima do peso ideal"
        print (f"{nome}, com base no peso e altura informados, o IMC é {imc:.1f} e a condição é {condicao} \n")
    elif imc > 32.3:
        condicao = "obeso"
        print (f"{nome}, com base no peso e altura informados, o IMC é {imc:.1f} e a condição é {condicao} \n")
    