

valor_compra=float(input("Digite o valor da sua compra:"))
num_prestacoes=float(input("Digite a quantidades de prestações:"))

valor_prestacao = valor_compra / num_prestacoes
juros5 = compra+(compra/100)*5
juros12 = compra+(compra/100)*12.4
juros14 = compra+(compra/100)*15.3
avista = compra-(compra/100)*5

if juros5 > 4:
  print("Recebeu o juros de 5%")
elif juros5 <12.4:
  print("Recebeu o juros de 5%")
if juros12 > 12.3:
  print("Recebeu o juros de 12.4%")
elif juros12 <15.3:
  print("Recebeu o juros de 12.4%")
if juros14 > 15.2:
  print("Recebeu o juros de 15.3%")


valor=float(input("Digite o valor da parcela: "))

taxa=float(input("Digite o valor da taxa: "))

tempo=float(input("Digite o tempo: "))

prestacao=valor+(valor*(taxa/100)*tempo)

print("O valor da prestação é: ",prestacao)
