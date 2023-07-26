ganhoHora = float(input("Quanto que você ganha por hora: "))
horasTrabalhadasMes = float(input("Quantas horas você trabalhou no mês: "))

salarioBruto = ganhoHora * horasTrabalhadasMes
impostoRenda = salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05

descontoTotal = impostoRenda + inss + sindicato

salarioLiquido = salarioBruto - impostoRenda - inss - sindicato

print("\n Salário Bruto:", salarioBruto, 
      "\n Inposto de Renda:", impostoRenda, "\n INSS:", inss, "\n Sindicato:", sindicato,
      "\n Desconto total pago:", descontoTotal, "\n Salário Liquido:", salarioLiquido,)