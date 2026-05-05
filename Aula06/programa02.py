"""
desenvolva um sistema de gerenciamento de carros com realização CRUD


"""
import os
import time

carros = []
proximo_id = 1

while True:
    os.system("cls")

    print("1 - Cadastrar carro")
    print("2 - Listar carros")
    print("3 - Atualizar carros")
    print("4 - Deletar carros")
    print("0 - Sair")

    op = input("Escolha uma opção: ")

    # CREATE
    if op == "1":
        modelo = input("Digite o modelo do carro: ")
        preco = float(input("Digite o preço: "))
        marca = input("Digite a marca: ").title()

        carro = {
            "id": proximo_id,
            "modelo": modelo,
            "preco": preco,
            "marca": marca,
        }

        carros.append(carro) 
        proximo_id += 1
        print("Carro cadastrado com sucesso!")

    # READ
    elif op == "2":
        if not carros:
            print("Nenhum carro cadastrado")
        else:
            print("\nLista de carros:")
            for carro in carros:
                print(f'ID: {carro["id"]} | Modelo: {carro["modelo"]} | Preço: {carro["preco"]} | Marca: {carro["marca"]}')

    # UPDATE
    elif op == "3":
        if not carros:
            print("Nenhum carro cadastrado")
        else:
            for carro in carros:
                print(f'ID: {carro["id"]} | Modelo: {carro["modelo"]} | Preço: {carro["preco"]} | Marca: {carro["marca"]}')

            id_busca = int(input("Digite o id do carro para atualizar: "))
            encontrado = False

            for carro in carros:
                if carro["id"] == id_busca:
                    carro["modelo"] = input("Novo modelo: ")
                    carro["preco"] = float(input("Novo preço: "))
                    carro["marca"] = input("Nova marca: ").title()
                    print("Carro atualizado com sucesso")
                    encontrado = True
                    break

            if not encontrado:
                print("Carro não encontrado")

    # DELETE
    elif op == "4":
        if not carros:
            print("Nenhum carro cadastrado")
        else:
            print("\nLista de carros:")
            for carro in carros:
                print(f'ID: {carro["id"]} | Modelo: {carro["modelo"]} | Preço: {carro["preco"]} | Marca: {carro["marca"]}')

            id_busca = int(input("Digite o id do carro para deletar: "))
            encontrado = False

            for carro in carros:
                if carro["id"] == id_busca:
                    carros.remove(carro)
                    print("Carro deletado com sucesso!")
                    encontrado = True
                    break

            if not encontrado:
                print("Carro não encontrado")

    # SAIR
    elif op == "0":
        print("Saindo do sistema...")
        total = 10
        for i in range(1, total + 1):
            porcentagem = int((i / total) * 100)
            barra = "🟩" * i
            vazio = "-" * (total - i)
            print(f"\r[{barra}{vazio}] {porcentagem}%", end="")
            time.sleep(0.2)
        break

    else:
        print("Opção inválida")

    input("\nPressione ENTER para continuar...")