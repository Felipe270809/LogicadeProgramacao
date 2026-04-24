"""
Calculos e manipulação de variaveis
"""

nome=input("digite o seu nome: ")
idade=int(input("digite sua idade"))
peso=input("Digite seu peso: ")
altura=input("digite a sua altura: ")
#tratamento de exceção
try:
    idade=int(idade)
    peso=float(peso)
    altura=float(peso)

except ValueError as e:
 print(e)
imc= peso/(altura**2)
print("Seu IMC é: ", imc)