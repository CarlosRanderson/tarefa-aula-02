# 3.Faça um algoritmo que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F -Feminino, M -Masculino, Sexo Inválido.

letra = input("Qual o seu sexo? Digite 'F' para feminino e 'M' para masculino: ")
sexo = letra.upper()

if sexo == 'F':
    print("F - Feminino.")
elif sexo == 'M':
    print("M - Masculino.")
else:
    print("Sexo Inválido.")

