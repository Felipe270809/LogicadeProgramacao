#Metodo usando condições
#v1=int(input("Primeiro valor: "))
#v2=int(input("Segundo valor: "))
#v3=int(input("Terceiro valor: "))
#Para saber quem é o menor
#if v1<v2 and v1<v3:
 #   print(f"{v1}é o menor valor")
#if v2<v1 and v2<v3:
  #  print(f"{v2} é o menor valor")
#if v3<v1 and v3<v2:
   # print(f"{v3} é o menor valor")
#Para saber quem é o maior
#if v1>v2 and v1>v3:
   # print(f"{v1} é o maior valor")
#if v2>v3 and v2>v1:
   # print(f"{v2} é o maior valor")
#if v3>v2 and v3>v1:
 #   print(f"{v3} é o maior valor")
#Método usando lista e funções max e min(também funciona)
#lista=[v1, v2,v3]
#menor=min(lista)
#maior=max(lista)
#print(f"O maior valor digitado foi {maior}, e o menor {menor}")

#Mais um método mas agora usando lista infinita e o usuário escolhe quantos valores terá
import os
os.system("cls")
print("Fale um valor e direi qual é o maior e o menor entre eles")
valores=[]
while True:
    valor=float(input("Qual o valor que deseja colocar?: "))
    valores.append(valor)
    print(valores)
    opção=input("Deseja continuar? (Sim=s |Não=n) ")
    if opção == "n":
        break
menor=min(valores)
maior=max(valores)
os.system("cls")
print(30*"=" , "Resultado", 30*"=")
print(f"O maior valor é {maior} e o menor valor é {menor}")