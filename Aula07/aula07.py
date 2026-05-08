"""
Manipulação de ariquivos: percorrer os meu diretorios, encontrar o arquivo passar o comando de abertura de arquivo ,passar comando de  ação.

modos de ação:
    - " :leitura do arquivo
    -"w": escrita(sobrescreve o conteudo antigo)
    -"a":adiciona conteudo
    -"X": adiciona conteudo
    -"b" arquivos binarios
    -"t":texto
arquivo=open("arquivo.txt", "modo")
"""
arquivo=open("primeiro_arquivo.txt", "w")
arquivo.write("ola mundo!Meu primeiro arquivo")
arquivo.close()
#lendo arquivo
arquivo=open("primeiro_arquivo.txt", "r")
conteudo=arquivo.read()
print(conteudo)
arquivo.close()
#aplicando boa pratica
with open("primeiro_arquivo.txt", "r") as arquivo:
    conteudo=arquivo.read()
    print(conteudo)

#arquivo com multiplas escritas
with open("alunos.txt","a") as arquivo:
    arquivo.write("Ana\n")
    arquivo.write("Ana\n")
    arquivo.write("João\n")
    arquivo.write("Lucas\n")
    arquivo.write("Karython\n")
    arquivo.write("Gomess\n")

#lendo linha a linha
with open ("alunos.txt","r")as arquivo:
    for linha in arquivo:
        print(linha)
frutas=["pera", "abacaxi", "melancia", "manga", "caju"]
with open("frutas.txt","w")as arquivo:
    for f in frutas:
        arquivo.write(f+ "\n")
#converter um arquivo em lista
with open("frutas.txt","r")as arquivo:
    linhas=arquivo.readlines()

print(type(linhas))
print (linhas)
#saida ["pera\n" ,"abacaxi\n" ...]
#limpar a quebra de linha
with open("frutas.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())
#exemplo para cadastro
while True:
    nome=input("digite seu nome: ").title()

    with open("cadastro.txt","a" ) as arquivo:
        arquivo.write(nome +"\n")
    sair=input("deseja sair do sistema? s/n").lower()
    if sair =="s":
        break
