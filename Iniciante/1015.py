# Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) 
# e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:
# distancia = raizQuadrada( (x2 - x1)**2 + (y2 - y1)**2 ) (4 casas decimais após a vírgula)

# Entrada
# O arquivo de entrada contém duas linhas de dados. 
# A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.
# x1 y1 (float)
# x2 y2 (float)

# Calcular
# distancia = ( (x2 - x1)**2 + (y2 - y1)**2 ) ** 0.5 (4 casas decimais após a vírgula)
 
# Saída
# Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o ponto decimal.
# 4.4721

# Code
entrada1 = input().split()
entrada2 = input().split()
x1,y1 = float(entrada1[0]), float(entrada1[1])
x2,y2 = float(entrada2[0]), float(entrada2[1])

distancia = ( (x2 - x1)**2 + (y2 - y1)**2 ) ** 0.5

print("{:.4f}".format(distancia))