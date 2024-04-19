
a=float(input("Informe o número A: "))

if a==0:
 print('Tu tá de brincadeira rapaz executa o código certo aí')
 exit()

"""1. adição
2. subtração
3. multiplicação
4. divisão
"""

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
=======
# Calculadora com as funções soma, sobtração divisão e multiplicação

val1,operacao,val2=input('operação:').split()

print(val1,operacao,val2)

val1=int(val1)

val2 = int(val2)

resultado=[]

if operacao == '+':
  resultado = val1+val2

elif operacao == '-':
  resultado = val1-val2

elif operacao == '*' or operacao=='x':
  resultado = val1*val2

elif operacao == '/':
  resultado = val1 / val2



print(resultado)


