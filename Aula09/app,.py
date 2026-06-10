import os
import json
import time

ARQUIVO = "carros.json"


# Função para salvar
def salvar():
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(carros, arquivo, indent=4, ensure_ascii=False)


# Carregar arquivo
if os.path.exists(ARQUIVO):
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            carros = json.load(arquivo)
    except json.JSONDecodeError:
        carros = []
else:
    carros = []
    salvar()


# Próximo ID
if carros:
    proximo_id = max(carro["id"] for carro in carros) + 1
else:
    proximo_id = 1


while True:

    os.system("cls")

    print("=" * 30)
    print("    SISTEMA DE CARROS")
    print("=" * 30)
    print("1 - Cadastrar carro")
    print("2 - Listar carros")
    print("3 - Atualizar carro")
    print("4 - Deletar carro")
    print("0 - Sair")
    print("=" * 30)

    op = input("Escolha uma opção: ")

    # CADASTRAR
    if op == "1":

        modelo = input("Digite o modelo: ")
        preco = float(input("Digite o preço: "))
        marca = input("Digite a marca: ").title()

        carro = {
            "id": proximo_id,
            "modelo": modelo,
            "preco": preco,
            "marca": marca
        }

        carros.append(carro)
        salvar()

        proximo_id += 1

        print("\nCarro cadastrado com sucesso!")

    # LISTAR
    elif op == "2":

        if not carros:
            print("\nNenhum carro cadastrado.")
        else:
            print("\nLISTA DE CARROS\n")

            for carro in carros:
                print(
                    f'ID: {carro["id"]} | '
                    f'Modelo: {carro["modelo"]} | '
                    f'Preço: R$ {carro["preco"]:.2f} | '
                    f'Marca: {carro["marca"]}'
                )

    # ATUALIZAR
    elif op == "3":

        if not carros:
            print("\nNenhum carro cadastrado.")
        else:

            for carro in carros:
                print(
                    f'ID: {carro["id"]} | '
                    f'Modelo: {carro["modelo"]} | '
                    f'Preço: R$ {carro["preco"]:.2f} | '
                    f'Marca: {carro["marca"]}'
                )

            id_busca = int(input("\nDigite o ID do carro: "))

            encontrado = False

            for carro in carros:
                if carro["id"] == id_busca:

                    carro["modelo"] = input("Novo modelo: ")
                    carro["preco"] = float(input("Novo preço: "))
                    carro["marca"] = input("Nova marca: ").title()

                    salvar()

                    print("\nCarro atualizado com sucesso!")
                    encontrado = True
                    break

            if not encontrado:
                print("\nCarro não encontrado.")

    # DELETAR
    elif op == "4":

        if not carros:
            print("\nNenhum carro cadastrado.")
        else:

            for carro in carros:
                print(
                    f'ID: {carro["id"]} | '
                    f'Modelo: {carro["modelo"]} | '
                    f'Preço: R$ {carro["preco"]:.2f} | '
                    f'Marca: {carro["marca"]}'
                )

            id_busca = int(input("\nDigite o ID do carro: "))

            encontrado = False

            for carro in carros:
                if carro["id"] == id_busca:
                    carros.remove(carro)
                    salvar()
                    print("\nCarro deletado com sucesso!")
                    encontrado = True
                    break

            if not encontrado:
                print("\nCarro não encontrado.")

    # SAIR
    elif op == "0":

        print("\nSaindo do sistema...")

        total = 10

        for i in range(1, total + 1):
            porcentagem = int(i / total * 100)
            barra = "🟩" * i
            vazio = "-" * (total - i)

            print(f"\r[{barra}{vazio}] {porcentagem}%", end="")

            time.sleep(0.2)

        print("\nPrograma encerrado.")
        break

    else:
        print("\nOpção inválida!")

    input("\nPressione ENTER para continuar...")
