# π = 3.14159

# Entrada
# A entrada contém um valor de ponto flutuante (dupla precisão), no caso, a variável raio.

# Saída
# Apresentar a mensagem "A=" seguido pelo valor da variável area, conforme exemplo abaixo, com 4 casas após o ponto decimal. 

# Código
pi = 3.14159
raio = float(input())
print("A=" + "{:.4f}".format(pi * raio**2))