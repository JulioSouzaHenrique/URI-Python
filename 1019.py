# Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, 
#e informe-o expresso no formato horas:minutos:segundos.

# Entrada
# tempo (segundos), int

# Saída 
#horas:minutos:segundos

# Code
tempoTotal = int(input())

horas = tempoTotal // 3600
tempoTotal -= horas * 3600
minutos = tempoTotal // 60
tempoTotal -= minutos * 60
segundos = tempoTotal

print(str(horas)+ ":" + str(minutos) + ":" + str(segundos))