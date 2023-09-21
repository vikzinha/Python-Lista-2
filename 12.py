valor_hora = float(input())
horas_trabalhadas = float(input())

salario_bruto = valor_hora * horas_trabalhadas
fgts = 0.11 * salario_bruto

    if salario_bruto <= 900:
        ir_percentual = 0
    elif salario_bruto <= 1500:
        ir_percentual = 0.05
    elif salario_bruto <= 2500:
        ir_percentual = 0.1
    else:
        ir_percentual = 0.2

desconto_ir = ir_percentual * salario_bruto
desconto_inss = 0.1 * salario_bruto
total_descontos = desconto_ir + desconto_inss
salario_liquido = salario_bruto - total_descontos

print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"IR ({ir_percentual * 100}%): R$ {desconto_ir:.2f}")
print(f"INSS: R$ {desconto_inss:.2f}")
print(f"FGTS: R$ {fgts:.2f}")
print(f"Total de descontos: R$ {total_descontos:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")
