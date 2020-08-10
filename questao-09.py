# 9.Faça um algoritmo que leia três números e mostre-os em ordem decrescente.

numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
numero3 = int(input("Digite o terceiro numero: "))

if numero1 < numero3:
    numero1, numero3 = numero3, numero1

if numero1 < numero2:
    numero1, numero2 = numero2, numero1

if numero2 < numero3:
    numero2, numero3 = numero3, numero2

print("A ordem decrescente é", numero1, ",", numero2, ", e ", numero3)