# 6.Faça um algoritmo que leia três números e mostre o maior deles.
numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))
numero3 = float(input("Digite o terceiro numero: "))

if numero1 > numero2 and numero1 > numero3:
    print("O primeiro número é maior.")
elif numero2 > numero3:
    print("O segundo número é maior.")
else:
    print("O terceiro número é maior.")