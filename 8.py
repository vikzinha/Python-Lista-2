preco1 = float(input("Digite o preço do primeiro produto: "))
preco2 = float(input("Digite o preço do segundo produto: "))
preco3 = float(input("Digite o preço do terceiro produto: "))

produto_mais_barato = min(preco1, preco2, preco3)

if produto_mais_barato == preco1:
    print("Você deve comprar o primeiro produto.")
elif produto_mais_barato == preco2:
    print("Você deve comprar o segundo produto.")
else:
    print("Você deve comprar o terceiro produto.")
