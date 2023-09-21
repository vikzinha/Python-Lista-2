valor_saque = int(input("Digite o valor do saque (entre 10 e 600 reais): "))

if valor_saque < 10 or valor_saque > 600:
    print("Valor de saque não permitido.")
else:
    notas_100 = 0
    notas_50 = 0
    notas_10 = 0
    notas_5 = 0
    notas_1 = 0

    while valor_saque > 0:
        if valor_saque >= 100:
            notas_100 += 1
            valor_saque -= 100
        elif valor_saque >= 50:
            notas_50 += 1
            valor_saque -= 50
        elif valor_saque >= 10:
            notas_10 += 1
            valor_saque -= 10
        elif valor_saque >= 5:
            notas_5 += 1
            valor_saque -= 5
        else:
            notas_1 += 1
            valor_saque -= 1

    print(f"Valor do saque solicitado: {valor_saque}")

    print(f"Notas fornecidas:")
    if notas_100 > 0:
        print(f"{notas_100} notas de 100 reais")
    if notas_50 > 0:
        print(f"{notas_50} notas de 50 reais")
    if notas_10 > 0:
        print(f"{notas_10} notas de 10 reais")
    if notas_5 > 0:
        print(f"{notas_5} notas de 5 reais")
    if notas_1 > 0:
        print(f"{notas_1} notas de 1 real")
