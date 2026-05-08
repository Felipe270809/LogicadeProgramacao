"""
1.Crie um programa que o usuario possa digitar quantos números quiser e ao terminar imprima a lista em ordem crescente.

2.crie um programa que o usuario possa digitar a quantidade desejada de notas de um determinado aluno (nota mínimaa 0 e maximo 10) e o programa calcula a media do aluno e o final imprima se o aluno ta aprovado>= ,recuperação<=5 ou reprovado >=5)
"""
# lista=[]
# print("Seja bem vindo!")

# while True:
#     n=int(input("Qual o número que deseja usar?: "))
#     lista.append(n)
#     op=input("Deseja continuar? (sim=s|não=n)")
#     if op=="n":
#         break
# lista.sort()
# print("A lista em ordem crescente é:" ,lista)
print("Seja bem vindo!")
notas=[]
while True:
    nota=int(input("Qual a nota que você tirou?: "))
    op=input("Deseja continuar? (sim=s|não=n)")
    notas.append(nota)
    if op=="n":
         break
media=sum(notas) / len(notas)
if media >=7:
     print("Você passou!")
elif media >=5:
    print("Você está de recuperação")
else:
     print("Você está reprovado!")
print("Sua media foi:",media)
