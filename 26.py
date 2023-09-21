preco_gasolina = 2.50
preco_alcool = 1.90

litros_vendidos = float(input("Digite o número de litros vendidos: "))
tipo_combustivel = input("Digite o tipo de combustível (A para álcool, G para gasolina): ").strip().upper()

if tipo_combustivel == "A":
    if litros_vendidos <= 20:
        valor_a_pagar = litros_vendidos * (preco_alcool - (preco_alcool * 0.03))
    else:
        valor_a_pagar = litros_vendidos * (preco_alcool - (preco_alcool * 0.05))
elif tipo_combustivel == "G":
    if litros_vendidos <= 20:
        valor_a_pagar = litros_vendidos * (preco_gasolina - (preco_gasolina * 0.04))
    else:
        valor_a_pagar = litros_vendidos * (preco_gasolina - (preco_gasolina * 0.06))
else:
    print("Tipo de combustível inválido.")
    valor_a_pagar = 0

print(f"Valor a ser pago pelo cliente: R$ {valor_a_pagar:.2f}")
