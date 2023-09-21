numero = int(input("Digite um número inteiro menor que 1000: "))

if numero >= 1000:
    print("Número fora dos limites permitidos.")
else:
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    descricao_centenas = f"{centenas} centenas" if centenas > 0 else ""
    descricao_dezenas = f"{dezenas} dezenas" if dezenas > 0 else ""
    descricao_unidades = f"{unidades} unidades" if unidades > 0 else ""

    descricao = ", ".join(desc for desc in [descricao_centenas, descricao_dezenas, descricao_unidades] if desc)

    print(f"{numero} = {descricao}")
