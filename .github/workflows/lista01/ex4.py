#Analisando uma resolucao de Geometria Analitica, distancia entre 2 pontos distintos:
#De os valores de entrada das coordenadas cartesianas:
x1 = float(input("Digite x1 do ponto P1: "))
y1 = float(input("Digite y1 do ponto P1: "))
x2 = float(input("Digite x2 do ponto P2: "))
y2 = float(input("Digite y2 do ponto P2: "))
#Apos entrada, o modelamento numero para o calculo segue a seguinte equacao:
distancia = ((x1 - x2) ** 2 + (y1 - y2)**2)** 0.5
print("A distancia entre os pontos P1 e P2 é: {:.4f}".format(distancia))
