# Entrada
# Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. 
# a,b,c (float)

# Calcular
# Em seguida, calcule e mostre:
#a) a área do triângulo retângulo que tem A por base e C por altura.
#b) a área do círculo de raio C. (pi = 3.14159)
#c) a área do trapézio que tem A e B por bases e C por altura.
#d) a área do quadrado que tem lado B.
#e) a área do retângulo que tem lados A e B.

# Saída
# O arquivo de saída deverá conter 5 linhas de dados
# Cada linha corresponde a uma das áreas descritas acima, sempre com mensagem correspondente e um espaço entre os dois pontos e o valor. 
# O valor calculado deve ser apresentado com 3 dígitos após o ponto decimal.
#TRIANGULO: 7.800
#CIRCULO: 84.949
#TRAPEZIO: 18.200
#QUADRADO: 16.000
#RETANGULO: 12.000

# Code
entrada = input().split()
a = float(entrada[0])
b = float(entrada[1])
c = float(entrada[2])

triangulo = (a * c) / 2
circulo = 3.14159 * c ** 2
trapezio = ( (a + b) * c ) / 2
quadrado = b ** 2
retangulo = a * b 

print("TRIANGULO: " + "{:.3f}".format(triangulo))
print("CIRCULO: " + "{:.3f}".format(circulo))
print("TRAPEZIO: " + "{:.3f}".format(trapezio))
print("QUADRADO: " + "{:.3f}".format(quadrado))
print("RETANGULO: " + "{:.3f}".format(retangulo))