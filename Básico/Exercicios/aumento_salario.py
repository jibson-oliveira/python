salario_atual = float(input("Informe o valor do seu salario atual: \n"))
percentual = float(input("Informe o percentual de aumento: \n"))

salario_novo = salario_atual+(salario_atual*(percentual/100))

print ("O valor do salário com aumento é R$ %.2f " %salario_novo)