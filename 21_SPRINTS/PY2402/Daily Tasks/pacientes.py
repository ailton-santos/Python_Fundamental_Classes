#no final mostre a quantidade de pessoas analisadas e a média de temperatura.
temperatura = int(input("Qual a temperatura do paciente?\n"))
for girafas in range(temperatura):
    temperatura = int(input("Qual a temperatura do paciente?\n"))
    if temperatura <= 37 and temperatura >= 36:
        print("A temperatura está OK!\n")
    elif temperatura <= 35:
        print("O paciente está com hipotenusa.\n")
    elif temperatura <= 38 and temperatura >= 37.2:
        print("O paciente está febril.\n")
    elif temperatura <= 39 and temperatura >= 38:
        print("O paciente está com febre.\n")
    elif temperatura >= 39 and temperatura <= 42:
        print("O paciente está com febre.\n")
    elif temperatura >= 42:
        print("O paciente está em estado de urgência.\n")
        
quantidade_pacientes = int(input("Quantos pacientes foram atendidos?"))

    
