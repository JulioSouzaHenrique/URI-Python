# Leia 4 valores inteiros A, B, C e D.
#  A seguir, 
#1) se B for maior do que C 
#2) e se D for maior do que A, 
#3) e a soma de C com D for maior que a soma de A e B 
#4) e se C e D, ambos, forem positivos 
#5) e se a variável A for par 
#escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".

# Entrada
# Quatro números inteiros A, B, C e D.

# Saída
# Mostre a respectiva mensagem após a validação dos valores.
# Valores nao aceitos
# Valores aceitos

# Code
a,b,c,d = [int(e) for e in input().split()]

if b>c and d>a and c+d > a+b and c > 0 and d > 0 and a % 2 == 0:
    print("Valores aceitos") 
else:
    print("Valores nao aceitos")