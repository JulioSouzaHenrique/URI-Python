# Entrada
# ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1
# o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. 
# codPeca1, numPeca1, valorUnitarioPeca1 (int, int, float)
# codPeca1, numPeca1, valorUnitarioPeca1 (int, int, float)

# Cálculo
# calcule e mostre o valor a ser pago.
# valorPagar = numPeca1 * valorUnitarioPeca1 + numPeca2 * valorUnitarioPeca2 (duas casas decimais depois da vírgula)

# Saída
# VALOR A PAGAR: R$ 15.50 - > VALOR A PAGAR: R$

# Code

# codPeca1, numPeca1, valorUnitarioPeca1 (int, int, float)
# codPeca1, numPeca1, valorUnitarioPeca1 (int, int, float)
entrada1 = input().split() #entrada1, entrada2 - list
entrada2 = input().split()

valorPagar = int(entrada1[1]) * float(entrada1[2]) + int(entrada2[1]) * float(entrada2[2])

print("VALOR A PAGAR: R$ " + "{:.2f}".format(valorPagar))


