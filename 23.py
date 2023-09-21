numero = float(input("Digite um número: "))
numero_arredondado = round(numero)

if numero == numero_arredondado:
    print(f"O número {numero} é um número inteiro.")
else:
    print(f"O número {numero} é um número decimal.")
