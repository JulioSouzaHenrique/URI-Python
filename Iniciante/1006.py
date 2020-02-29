# Entrada
# Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno (double)

# Cálculo
#  Calcule a média do aluno, sabendo que a nota A tem peso 2, a nota B tem peso 3 e a nota C tem peso 5

# Saída
# Imprima a variável MEDIA conforme exemplo abaixo, com 1 dígito após o ponto decimal e com um espaço em branco antes e depois da igualdade. 

# Code
a = float(input())
b = float(input())
c = float(input())

media = (a*2 + b*3 + c*5)/10 

print("MEDIA = " + "{:.1f}".format(media))