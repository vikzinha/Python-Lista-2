
l1 = float(input("Digite o primeiro lado do triângulo: "))
l2 = float(input("Digite o segundo lado do triângulo: "))
l3 = float(input("Digite o terceiro lado do triângulo: "))

if (l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1):

    if l1 == l2 == l3:
        tipo = "Equilátero"
    elif l1 == l2 or l1 == l3 or l2 == l3:
        tipo = "Isósceles"
    else:
        tipo = "Escaleno"
    
    print(f"Os lados formam um triângulo {tipo}.")
else:
    print("Os lados não formam um triângulo.")
