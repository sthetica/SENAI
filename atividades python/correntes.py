maior_15 = float()
alerta = 0
soma = 0
acima_20 = float()


for cont in range (8):
    corrente = float(input(f"Digite a {cont + 1}° corrente elétrica: "))
    soma += corrente

    if corrente > maior_15:
       maior_15 = corrente


    if corrente > 20:
      acima_20 += 1 

      if corrente > 200:
         alerta += 1

    media = soma / 10

print(f"{maior_15} correntes foram maiores que 15.")
print(f"Houve {acima_20} sobrecargas")
print(f"A média das correntes é {media}")
print(f"ALERTA! A corrente ultrapassou 200A {alerta} vezes.")
