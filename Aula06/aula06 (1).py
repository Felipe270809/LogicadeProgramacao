lista=["gomes",10,True,10.5]
#imprimindo valor especifico da lista


#imprimindo ultimo indice
print(lista [-1])

#imprimir intervalo
print(lista[2:4])

#ordernar essa lista
#lista.sort()

#inserindo na posição especifica
lista.insert(2,"joao")

#inserindo varios valores
lista.extend({"ana", "beatriz", "Roberto", "cicrano"})
numeros=[]
#adicionando valores de forma dinamica
# for i in range(10):

#     numeros.append (i*2)
#print(numeros)
#removendo item da lista

print(f"Lista antes de remover {lista}")
#pop remove pelo indice
lista.pop(0)
#removendo o utimo
lista.pop()

#removendo pelo valor (remove pa primeira ocorrencia)
lista.remove("cicrano")
lista_numeros=[n for n in range(11)]

print(f"Lista depois de remover {lista}")

#removendo intervalo de valores
print(f"lista antes de remover {lista_numeros}")
del lista[2:4]
print(f"lista depois de remover {lista_numeros}")
#adicionando na lista
# lista.append("karython")
# for i in range(len(lista)):
#     print(f"{i+1}° nome da lista: {lista}")

listanomes=["gomes","fulano","cicrano","beltrano","maria", "pedro"]
listanomes[1]="Lucas"
print(listanomes)

numeros=[1,2,3,4,5,6,7,8,9,10]
for i in range (len(numeros)):
    if numeros [i]>5:
        numeros[i]=numeros[i]*2
print(numeros)




#list compreheision
numeros=[n*2 if n>20 else n for n in numeros]
print(numeros)
