# Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de combustível gasto (em litros).
# distanciaTotalPercorrida (Km) (int)
# totalCombustivel (l) (float)

# Entrada
# O arquivo de entrada contém dois valores: um valor inteiro X representando a distância total percorrida (em Km), 
#e um valor real Y representando o total de combustível gasto, com um dígito após o ponto decimal.

# Calcular
# consumoMedio = distanciaTotalPercorrida / totalCombustivel  (3 casas decimais, depois da vírgula)

# Saída
# Apresente o valor que representa o consumo médio do automóvel com 3 casas após a vírgula, seguido da mensagem "km/l".
# 14.286 km/l

# Code
distanciaTotalPercorrida = int(input())
totalCombustivel = float(input())

consumoMedio = distanciaTotalPercorrida / totalCombustivel

print("{:.3f}".format(consumoMedio) + " km/l")
