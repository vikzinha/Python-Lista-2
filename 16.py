a = float(input("Digite o valor de a: "))

if a == 0:
    print("A equação não é do segundo grau. Encerrando o programa.")
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    delta = b**2 - 4*a*c

    if delta < 0:
        print("A equação não possui raízes reais. Encerrando o programa.")
    elif delta == 0:
        raiz = -b / (2*a)
        print(f"A equação possui uma raiz real: {raiz:.2f}")
    else:
        raiz1 = (-b + delta**0.5) / (2*a)
        raiz2 = (-b - delta**0.5) / (2*a)
        print(f"A equação possui duas raízes reais: {raiz1:.2f} e {raiz2:.2f}")
