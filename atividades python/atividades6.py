nome = input("Insira o nome: ")
idade = int(input("Insira a idade (anos completos): "))
while idade > 120 or idade < 0:
    idade = int((input("idade(anos completos - até 120)")))
    diasdevida = idade * 365
    print(f"{nome}, você ja viveu aproximadamente {diasdevida} dias.")
else:
    print("a idade digitada esta incorreta")