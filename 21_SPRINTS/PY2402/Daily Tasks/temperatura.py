temperatura_normal = 37
while True:
    cliente = int(input("Qual a temperatura atual do cliente? \n"))
    if cliente == temperatura_normal:
        print("A temperatura está OK!\n")
    elif cliente > temperatura_normal:
        print("Estado Febril!\n")
    elif cliente < temperatura_normal:
        print("A temperatura está abaixo do normal(37°C)\n")

