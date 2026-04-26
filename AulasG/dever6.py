sal=float(input("Qual o sálario do funcionário?: "))
if sal>=1250:
    print(f"O funcionário receberá 10% de aumento , agora o salário dele é de {sal*1.10:.2f}")
else:
    print(f"o sálario do funcionario receberá 15% de aumento! O salário atual dele será de {sal*1.15:.2f}")