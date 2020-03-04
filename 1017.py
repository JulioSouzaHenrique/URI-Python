# Entrada
# O arquivo de entrada contém dois inteiros. O primeiro é o tempo gasto na viagem (em horas) e o segundo é a velocidade média durante a mesma (em km/h).
# tempoGasto(horas) , velocidadeMedia(km/h) -> ints
# 12 KM/L

# Saída
# Imprima a quantidade de litros necessária para realizar a viagem, com três dígitos após o ponto decimal
# litrosNecessarios (3 casas após o ponto decimal)
# Ex: 70.833

# Code
tempoGasto = int(input())
velocidadeMedia = int(input())

#v = d/t
distancia = velocidadeMedia * tempoGasto  #km
litrosNecessarios = distancia / 12 #litros

print("{:.3f}".format(litrosNecessarios))