"""""
Aula 09/04/26-tipos de dados e saidas

str int bool float
"""
#variavel com valor definido

nome=("Felipe")
idade=(16)
altura=(1,80)
aluno= True
print("nome: " ,nome)
print("idade: ",idade)
print("altura: ",altura)
print("Aluno: " ,aluno)

#entrada de dados
nome1=input("digite seu nome: ")
print("nome", nome)
print("Novo nome: " ,nome1)

nome=input("Qual o seu nome?:")
data=float(input("Qual sua data de nascimento?: "))
peso=float(input("Qual seu peso?: "))
alt=float(input("Qual sua altura?: "))
print(f"Olá {nome} ,seja bem-vindo ao sistema Python\nAqui estão as suas informações:\nData de nascimento: {data}\nAltura:{alt}\nPeso: {peso}")
print(type(nome))
