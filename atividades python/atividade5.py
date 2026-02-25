contador=0
soma=0
while contador < 4:
 contador+= 1
 nota= float(input(f"Insira a {contador} nota"))
soma+=nota

media= nota/contador
print ("média das notas: ", media)
if media >= 7:
    print("aluno aprovado")
else:
   print ("aluno reprovado")

   