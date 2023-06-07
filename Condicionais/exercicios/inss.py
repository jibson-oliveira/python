print ("*"*17+" TABELA INSS 2017 "+"*"*17)
print ("* Salário de Contribuição (R$)  - Aliquota do INSS *")
print ("* até 1.659,38                  -         8%       *")
print ("* de 1.659,38 até 2.765,66      -         9%       *")
print ("* de 2.765,67 até 5.531,31      -        11%       *")
print ("*"*53)

salario_informado = float (input("Informe o salário de contribuição: "))
salario_contribuicao = salario_informado
if (salario_contribuicao <= 1659.38):
    aliquota_inss=8
elif (salario_contribuicao <= 2765.66):
    aliquota_inss=9
elif (salario_contribuicao  <= 5531.31):
    aliquota_inss=11
else:
    salario_contribuicao = 5531.31
    aliquota_inss=11

valor_inss = (salario_contribuicao *(aliquota_inss/100))
salario_liquido = salario_informado - valor_inss

print(f"O salário contribuição é : R${salario_contribuicao:.2f}. \n"
      f"A alíquota de INSS é de: {aliquota_inss:.1f}%. \n"
      f"Será descontado R$ {valor_inss:.2f}. \n"
      f"O salário líquido será de: R$ {salario_liquido:.2f}.")
