pesoPeixe = int(input("Coloque o peso do peixe: "))
valorExcedente = 4

if pesoPeixe > 50:
    excesso = pesoPeixe - 50
    multa = excesso * valorExcedente
    print("O excesso de kilos além do permitido é", excesso , "\n e você pagará", multa , "de multa")

if pesoPeixe <= 50:
    print("Você não pagará multa, o peso do peixe é:", pesoPeixe)
