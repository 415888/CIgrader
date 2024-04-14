#Calculo da DDP:
diferenca_potencial = float(input("Digite a diferenca de potencial (em Volts): "))
resistencia= float(input("Digite a resistencia (em Ohms): "))
#Calculo basico entre as funções (R/DDP):
corrente =diferenca_potencial / resistencia
print("A corrente eletrica é: {:.2f} A".format(corrente))
