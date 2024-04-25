# Calculadora

a=float(input("Informe o número A: "))

if a==0:
 print('Tu tá de brincadeira rapaz executa o código certo aí')
 exit()

'''1. adição
2. subtração
3. multiplicação
4. divisão '''

c=float(input("digite o número da operação que você deseja fazer: "))

if c==1:
 b=float(input('Informe o número B que você deseja adicionar somar: '))
elif c==2:
 b=float(input('Informe o número B que você deseja subtrair: '))
elif c==3:
 b=float(input('Informe o número B que você deseja multiplicar: '))
elif c==4:
 b=float(input('Informe o número B que você deseja dividir: '))
else:
  print("Tu tá de brincadeira rapaz executa o código certo aí")
exit()

if c==1:
 print("O resultado de A+B é: ",a+b)
elif c==2:
  print("O resultado de A-B é: ",a-b)
elif c==3:
  print("O resultado de A*B é: ",a*b)
elif c==4:
  print("O resultado de A/B é: ",a/b)

# Calculadora com as funções soma, sobtração divisão e multiplicação


from random import randint

print(randint(0, 1000))

numero1 = randint(0, 1000)
numero2 = randint(0, 1000)
print(numero1)
print(numero2)

#apenas anotando os resultados
resultado_soma = (numero1 + numero2)
print("O resultado da soma é:", resultado_soma, "\n")
resultado_sub = (numero1 - numero2)
print("O resultado da subtração é:", resultado_sub, "\n")
resultado_div = (numero1 / numero2)
print("O resultado da divisão é:", resultado_div, "\n")
resultado_mul = (numero1 * numero2)
print("O resultado da multiplicação é:", resultado_mul, "\n")

print("Resolva as quatro operações: \n")
#soma--------------------------------------------
print("Quanto é", numero1,"+",numero2, "?")
resultado = int(input())
if resultado == (numero1 + numero2) :
  print("Certa resposta!\n")
else:
  print("Resposta errada!\n")
#------------------------------------------------

#subtração---------------------------------------
print("Quanto é", numero1, "-", numero2, "?")
resultado = int(input())
if resultado == (numero1 - numero2):
  print("Certa resposta!\n")
else:
  print("Resposta errada!\n")
#------------------------------------------------

#divisão-----------------------------------------
print("Quanto é", numero1, "÷", numero2, "?")
resultado = int(input())
if resultado == (numero1 / numero2):
  print("Certa resposta!\n")
else:
  print("Resposta errada!\n")
#------------------------------------------------


#multiplicação-----------------------------------
print("Quanto é", numero1, "*", numero2, "?")
resultado = int(input())
if resultado == (numero1 * numero2):
  print("Certa resposta!")
else:
  print("Resposta errada!")
#------------------------------------------------

