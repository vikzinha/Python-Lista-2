# Preços das carnes por Kg
preco_file_duplo = 4.90
preco_alcatra = 5.90
preco_picanha = 6.90

tipo_carne = input("Digite o tipo de carne (File Duplo, Alcatra ou Picanha): ").strip().title()
quantidade = float(input("Digite a quantidade em Kg: "))

if tipo_carne == "File Duplo":
    if quantidade <= 5:
        preco_total = quantidade * preco_file_duplo
    else:
        preco_total = quantidade * 5.80
elif tipo_carne == "Alcatra":
    if quantidade <= 5:
        preco_total = quantidade * preco_alcatra
    else:
        preco_total = quantidade * 6.80
elif tipo_carne == "Picanha":
    if quantidade <= 5:
        preco_total = quantidade * preco_picanha
    else:
        preco_total = quantidade * 7.80
else:
    print("Tipo de carne inválido.")
    preco_total = 0

print("\nOpções de pagamento:")
print("1 - Cartão Tabajara")
print("2 - Dinheiro")
print("3 - Cartão de Crédito")
print("4 - Cartão de Débito")
print("5 - Pix")
opcao_pagamento = input("Escolha a forma de pagamento (1/2/3/4/5): ").strip()

if opcao_pagamento == "1":
    pagamento = "Cartão Tabajara"
    desconto = preco_total * 0.05
elif opcao_pagamento == "2":
    pagamento = "Dinheiro"
    desconto = 0
elif opcao_pagamento == "3":
    pagamento = "Cartão de Crédito"
    desconto = 0
elif opcao_pagamento == "4":
    pagamento = "Cartão de Débito"
    desconto = 0
elif opcao_pagamento == "5":
    pagamento = "Pix"
    desconto = 0
else:
    print("Opção de pagamento inválida.")
    pagamento = "Desconhecido"
    desconto = 0

valor_a_pagar = preco_total - desconto

print("\nCUPOM FISCAL")
print(f"Tipo de carne: {tipo_carne}")
print(f"Quantidade: {quantidade} Kg")
print(f"Preço total: R$ {preco_total:.2f}")
print(f"Tipo de pagamento: {pagamento}")
print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Valor a pagar: R$ {valor_a_pagar:.2f}")
