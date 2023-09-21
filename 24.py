n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

operacao = input("Escolha a operação (+ para soma, - para subtração, * para multiplicação, / para divisão): ")

if operacao == '+':
    resultado = n1 + n2
    operacao_texto = "soma"
elif operacao == '-':
    resultado = n1 - n2
    operacao_texto = "subtração"
elif operacao == '*':
    resultado = n1 * n2
    operacao_texto = "multiplicação"
elif operacao == '/':
    if n2 != 0:
        resultado = n1 / n2
        operacao_texto = "divisão"
    else:
        print("Erro! Divisão por zero não é permitida.")
        resultado = None
        operacao_texto = ""
else:
    print("Operação inválida.")
    resultado = None
    operacao_texto = ""

par_ou_impar = "par" if resultado % 2 == 0 else "ímpar"
positivo_ou_negativo = "positivo" if resultado >= 0 else "negativo"
inteiro_ou_decimal = "inteiro" if resultado.is_integer() else "decimal"

if resultado is not None:
    print(f"O resultado da {operacao_texto} é: {resultado}")
    print(f"O resultado é {par_ou_impar}, {positivo_ou_negativo} e {inteiro_ou_decimal}.")
