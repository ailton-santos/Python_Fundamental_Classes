# Lista para armazenar os números
numeros = []

# Loop para ler 10 números inteiros
for i in range(10):
    numero = int(input(f"Digite o {i}º número inteiro: "))
    numeros.append(numero)

# Exibindo os números lidos
print("\nOs números digitados foram:")
for numero in numeros:
    print(numero,"\n")

#maiores e menores valores:
maior_valor = max(numeros)
print(f"O maior valor escolhido foi: {maior_valor}")
menor_valor = min(numeros)
print(f"O menor valor escolhido foi: {menor_valor}")

soma = sum(numeros)
media_valores = soma / len(numeros)
print(f"A média é: {media_valores}")