estoque = {}

#Bem Vindo

print ("bem vindo ao sistema de gestao desenvolvido por Sthefany")

#Menu


while True:
    operacao = input ("deseja registrar a estrada e saida de produto? (digite 'entrada' ou 'saida')ou sair"). lower()
    if operacao == 'sair':
        break
    produto = input("nome do produto:"). strip()
    qtd = int(input("quantidade:"))

#Invalida/Erro

    if operacao not in ['entrada', 'saida']:
        print("operacao inválida.")
        continue

    if operacao == 'entrada':
        estoque[produto] = estoque.get(produto, 0) + qtd
    elif operacao == 'saída':
        if estoque.get(produto, 0) >= qtd:
            estoque[produto] -= qtd
        else:
            print("Erro:produto inexistente ou estoque insuficiente")

#Estoque final

print("/n ---Estoque Final ---")
for p, q in estoque.items():
    print(f"{p}: {q}")


    """While = Loopar a operação, para que ela não acabe no primeiro break"""
    """if = Operador de comparação"""
    """Dicionario = Uma 'gaveta' que agrupa varias variaveis"""