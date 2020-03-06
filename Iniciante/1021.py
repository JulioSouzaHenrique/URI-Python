# Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. 
# A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. 
# As notas consideradas são de 100, 50, 20, 10, 5, 2. 
# As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. 
# A seguir mostre a relação de notas necessárias.

# Entrada
# valor - (float)

# Saída
#NOTAS:
#5 nota(s) de R$ 100.00
#1 nota(s) de R$ 50.00
#1 nota(s) de R$ 20.00
#0 nota(s) de R$ 10.00
#1 nota(s) de R$ 5.00
#0 nota(s) de R$ 2.00
#MOEDAS:
#1 moeda(s) de R$ 1.00
#1 moeda(s) de R$ 0.50
#0 moeda(s) de R$ 0.25
#2 moeda(s) de R$ 0.10
#0 moeda(s) de R$ 0.05
#3 moeda(s) de R$ 0.01


# Code
notasListas = [100,50,20,10,5,2]
moedasListas = [50,25,10,5,1]

#Lendo
valor = input().split(".")
parteInteira, parteDecimal = int(valor[0]), int(valor[1])

print("NOTAS:")
for nota in notasListas:
    quantidade = parteInteira // nota 
    parteInteira %= nota
    print(quantidade, "nota(s) de R$ " + "{:.2f}".format( float(nota) ))

print("MOEDAS:")
print(parteInteira, "moeda(s) de R$ 1.00")
for moeda in moedasListas:
    quantidade = parteDecimal // moeda
    parteDecimal %= moeda
    print(quantidade, "moeda(s) de R$ " + "{:.2f}".format( (moeda/100) ))