# 4.Faça um algoritmo que verifique se uma letra digitada é vogal ou consoante.

caractere = input("Digite uma letra: ")
letra = caractere.upper()

if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
    print("É uma vogal.")
else:
    print("É uma consoante.")