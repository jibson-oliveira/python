palavra = input("Digite a palavra: \n")

a = 0
e = 0
i = 0
o = 0
u = 0

for letra in palavra:
    if letra == "a":
        a = a + 1
    elif letra == "e":
        e = e + 1
    elif letra == "i":
        i = i + 1
    elif letra == "o":
        o = o + 1
    elif letra == "u":
        u = u + 1

print (f"Quantidade de letras 'a' na palavra : {a} \n"
       f"Quantidade de letras 'e' na palavra : {e} \n"
       f"Quantidade de letras 'i' na palavra : {i} \n"
       f"Quantidade de letras 'o' na palavra : {o} \n"
       f"Quantidade de letras 'u' na palavra : {u} \n"
    )