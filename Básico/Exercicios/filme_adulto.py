ano_nascimento = int  (input("Informe o ano do seu nascimento: \n"))
idade = 2023 - ano_nascimento
pode_assistir = idade >= 18

print(f"Você tem {idade} anos e a resposta é: "f" {pode_assistir}.")