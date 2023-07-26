area = float(input("Qual é a medida em metros quadrados para ser pintado: "))
litrosNecessario = area/3

latas = round(litrosNecessario/18)
valorLatas = round(latas * 80)

print("Você precisará de", latas , "e irá pagar: R$",valorLatas)