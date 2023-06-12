'''
While normalmente é utilizado quando vocÊ quer repetir um bloco de código enquanto uma expressão for verdadeira.
O while usado indevidamente pode fazer com o que o sistema entre em um loop infinito

Sintaxe: 
while 'condição':
    bloco de código

bloco de código é executado enquanto a condição for verdadeira ou ela for interrompida com um break

'''

x = 1
while x < 10:
    print (x)
    x = x + 1


notas = 0
quant_notas_informadas = 0

while True:
    nota = float (input("Informe a nota (-1 para finalizar): "))
    if nota == -1:
        break
    notas = notas + nota
    quant_notas_informadas = quant_notas_informadas + 1

if quant_notas_informadas > 0:
    media = notas / quant_notas_informadas
    print(f"Quantidade de notas informadas é: {quant_notas_informadas}")
    print(f"Média: {media}")
else:
    print("Nenhuma nota informada. ")