# Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:
# maiorAB = (a + b + abs(a-b)) / 2

# Entrada
# O arquivo de entrada contém três valores inteiros.

# Saída
# Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".
#valor eh o maior

# Code
entrada = input().split()
a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])

maiorAB = (a + b + abs(a - b)) // 2
maiorABC = (maiorAB + c + abs(maiorAB - c)) // 2

print(maiorABC, "eh o maior")