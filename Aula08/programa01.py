import modulo as ma

def main():
    while True:
        print("\nCalculadora")
        print("1. Somar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Sair")

        op = input("Digite a opção desejada: ")

        match op:
            case "1":
                print("------- SOMA --------")
                n1 = int(input("Digite um número para somar: "))
                n2 = int(input("Digite outro número para somar: "))
                r = ma.soma(n1, n2)
                print("Resultado:", r)

            case "2":
                print("------- SUBTRAÇÃO --------")
                n1 = int(input("Digite um número para subtrair: "))
                n2 = int(input("Digite outro número para subtrair: "))
                r = ma.sub(n1, n2)
                print("Resultado:", r)

            case "3":
                print("------- MULTIPLICAÇÃO --------")
                n1 = int(input("Digite um número para multiplicar: "))
                n2 = int(input("Digite outro número para multiplicar: "))
                r = ma.mult(n1, n2)
                print("Resultado:", r)

            case "4":
                print("------- DIVISÃO --------")
                n1 = int(input("Digite um número para dividir: "))
                n2 = int(input("Digite outro número para dividir: "))
                r = ma.div(n1, n2)
                print("Resultado:", r)

            case "5":
                print("Encerrando...")
                break

            case _:
                print("Opção inválida!")

if __name__ == "__main__":
    main()