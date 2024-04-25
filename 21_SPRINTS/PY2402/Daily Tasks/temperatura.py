
temperatura_normal = 37
while True:
    cliente = int(input("Qual a temperatura atual do cliente? \n"))
    if cliente == temperatura_normal:
        print("A temperatura está OK!\n")
    elif cliente > temperatura_normal:
        print("Estado Febril!\n")
    elif cliente < temperatura_normal:
        print("A temperatura está abaixo do normal(37°C)\n")



# Programa que solicita um número de pacientes e sua temperatura. Classificando em: Temperatura normal, febril,com febre e Febre alta


p=int(input('Número de pacientes'))

soma=float()
for pacientes in range(0,p):
  temperatura=float(input('Digite a temperatura:'))
  if temperatura < 37.2:
    print('Temperatura normal')
  elif temperatura < 38.0:
    print('Febril')
  elif temperatura <39:
    print('Com febre')
  elif temperatura >=39:
    print('Febre alta')
  soma+=temperatura

print('\nmédia:',soma/(float(p)))
