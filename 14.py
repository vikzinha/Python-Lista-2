n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1 + n2) / 2

if 9.0 <= media <= 10.0:
    conceito = "A"
elif 7.5 <= media < 9.0:
    conceito = "B"
elif 6.0 <= media < 7.5:
    conceito = "C"
elif 4.0 <= media < 6.0:
    conceito = "D"
else:
    conceito = "E"

print(f"Nota 1: {n1}")
print(f"Nota 2: {n2}")
print(f"Média: {media:.2f}")
print(f"Conceito: {conceito}")

if conceito in ("A", "B", "C"):
    print("APROVADO")
else:
    print("REPROVADO")
