
#variavel pro nome
nome = input("Digite o seu nome: ")

#entrada
print("---------------------------------------------------".center(100))
#center(100) serve pra deixar oq esta escrito no meio, acho que não aprendemos isso com vc ainda, mas eu e o gui tava estudando em casa e aprendemos
print(f"Bem Vindo, {nome}".center(100))
print("---------------------------------------------------\n".center(100))

#pessoa que vai entrar no site
while True:
#while sempre precisa que tenha true do lado para rodar

#opção
    pessoa = float(input("Qual tipo de usuário você é?\n1- Membro\n2- Visitantes\n3- Saír\n\nQual opção deseja?: "))
#n\ serve para descer uma linha pra baixo entre as opções
    print()
#print() serve para deixar uma linha em branco, e separar as linhas

    if pessoa == 2:
#if vai estabelecer uma condição para algo acontecer
        tempo = float(input("Digite quantas horas você quer ficar logado(a) (tempo maximo: 4 horas): "))
#float vai permmitir que a variavel possua números quebrados
        print()
        if tempo <= 4:
            print(f"Olá, {nome}, você entrou no sistema!")
#"f" na frente do texto inserido serve para colocar uma variável dentro do texto
            break
#break vai fazer com que o while seja interrompido 

#se o tempo de uso for maior que 4 horas      
        if tempo > 4:
            print("Acesso negado! Quantidade de horas ultrapassadas.\n")
            tentativas = input("Tentar novamente?\n1- Sim\n2- Não\n\nEscolha: ")
            if tentativas == 1:
                continue
#o continue vai fazer o contrario do break, vai continuar rodando o while
            elif tentativas == 2:
#elif é o outrocaso do portugol, onde estabelece como se fosse um segundo "if" dentro de um
                print("Saíndo!")
                break



    if pessoa == 1:
        print("Seja Muito Bem Vindo!!!, tempo de acesso: 9h da manhã, até as 18h da tarde.")
        break

    if pessoa == 3:
        print("Saindo do sistema!!!")
#print serve pra mostrar o textinho quando executar o programa
        break

