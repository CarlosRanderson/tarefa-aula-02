# 8.Faça um algoritmo que pergunte o preço de três produtos e
# informe qual produto você deve comprar, sabendo que a decisão
# é sempre pelo mais barato.

produto1 = float(input("Digite o primeiro produto: "))
produto2 = float(input("Digite o segundo produto: "))
produto3 = float(input("Digite o terceiro produto: "))

#verificando é o menor numero
barato = produto1
if produto2 < produto1 and produto2 < produto3:
    barato = produto2
if produto3 < produto1 and produto3 < produto2:
    barato = produto3

print("O produto mais barato é:", barato)
