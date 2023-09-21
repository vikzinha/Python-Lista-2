data = input("Digite uma data no formato dd/mm/aaaa: ")

dia, mes, ano = data.split('/')

dia = int(dia)
mes = int(mes)
ano = int(ano)

dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    dias_por_mes[2] = 29

if 1 <= mes <= 12 and 1 <= dia <= dias_por_mes[mes]:
    print("Data válida.")
else:
    print("Data inválida.")
