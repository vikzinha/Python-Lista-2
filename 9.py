n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

numeros = [n1, n2, n3]
numeros.sort(reverse=True)

print("Números em ordem decrescente:", numeros)
