while True:
    num1 = int(input("Digite o número que deseja saber a tabuada: \n"))
    for i in range (1,11):
        resultado = num1 * i
        print(f"a tabuada do número {num1} X {i} é: \n {resultado}")
        