# Entrada 
# O arquivo de entrada contém 2 valores com uma casa decimal cada um.

# Calcular
#  a média do aluno, sabendo que a nota A tem peso 3.5 e a nota B tem peso 7.5

# Saída
#  imprima a variável MEDIA conforme exemplo abaixo, com 5 dígitos após o ponto decimal e com um espaço em branco antes e depois da igualdade

# Código
a = float(input())
b = float(input())
print("MEDIA = " + "{:.5f}".format( (3.5*a + 7.5*b)/11 ))