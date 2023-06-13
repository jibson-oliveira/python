usuario = "admin"
senha = "asdfqwer"

usuario_informado = input("Digite o usuario: \n")
senha_informada = input("Digite a senha: \n")

if usuario_informado == usuario and senha_informada == senha:
    print ("Acesso Autorizado.")
else: 
    print ("Acesso Negado.")