respostas_positivas = 0

print("Responda as seguintes perguntas com 'Sim' ou 'Não':")
P1 = input("1. Telefonou para a vítima? ").strip().lower()
if P1 == "sim":
    respostas_positivas += 1

P2 = input("2. Esteve no local do crime? ").strip().lower()
if P2 == "sim":
    respostas_positivas += 1

P3 = input("3. Mora perto da vítima? ").strip().lower()
if P3 == "sim":
    respostas_positivas += 1

P4 = input("4. Devia para a vítima? ").strip().lower()
if P4 == "sim":
    respostas_positivas += 1

P5 = input("5. Já trabalhou com a vítima? ").strip().lower()
if P5 == "sim":
    respostas_positivas += 1

if respostas_positivas == 2:
    print("Você é classificado como 'Suspeita'.")
elif 3 <= respostas_positivas <= 4:
    print("Você é classificado como 'Cúmplice'.")
elif respostas_positivas == 5:
    print("Você é classificado como 'Assassino'.")
else:
    print("Você é classificado como 'Inocente'.")
