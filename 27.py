preco_morango_ate_5kg = 2.50
preco_morango_acima_5kg = 2.20
preco_maca_ate_5kg = 1.80
preco_maca_acima_5kg = 1.50

quantidade_morangos = float(input("Digite a quantidade de morangos em Kg: "))
quantidade_macas = float(input("Digite a quantidade de maçãs em Kg: "))

if quantidade_morangos <= 5:
    preco_total_morangos = quantidade_morangos * preco_morango_ate_5kg
else:
    preco_total_morangos = quantidade_morangos * preco_morango_acima_5kg

if quantidade_macas <= 5:
    preco_total_macas = quantidade_macas * preco_maca_ate_5kg
else:
    preco_total_macas = quantidade_macas * preco_maca_acima_5kg

preco_total = preco_total_morangos + preco_total_macas

if quantidade_morangos + quantidade_macas > 8 or preco_total > 25.00:
    desconto = preco_total * 0.10
else:
    desconto = 0

valor_a_pagar = preco_total - desconto

print(f"Valor a ser pago pelo cliente: R$ {valor_a_pagar:.2f}")
