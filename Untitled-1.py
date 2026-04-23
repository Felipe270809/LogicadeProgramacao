#NOTE: Boletim Escolar
import os
os.system("cls")
nome=input("digite o nome do aluno: ").title()
turma=input("Digite o  nome da turma:").upper()
nota1=float(input("Digite a primeira nota do aluno:"))
nota2=float(input("Digite a segunda nota:")) 
nota3=float(input("Digite a terceira nota:")) 
nota4=float(input("Digite a quarta nota:")) 
nota5=float(input("Digite a quinta nota:" )) 
media=(nota1+nota2+nota3+nota4+nota5)/5 
resultado= None
if media>=7:
    resultado= "Aprovado"
elif media >=5:
 resultado="Recuperação"
else:
   resultado="Reprovado"
       
os.system("cls")
print(30*"=","Boletim Escolar",30*"==")
print("nome do aluno:" ,nome,"    Turma:",turma)
print(f"Nota 2:{nota2}")
print(f"Nota 3:{nota3}")
print(f"Nota 4:{nota4}")
print(f"Nota 5:{nota5}")
print(70*"=")
print("Media" ,media)
print(f"Situação: {resultado}")