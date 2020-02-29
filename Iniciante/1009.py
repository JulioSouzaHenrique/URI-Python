# Entrada
#leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro).
# nome (string), salarioFixo (double), vendas (double)

# Calcular
#Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.
# recebe 15% sobre vendas => vendas*0.15
# salarioTotal = salarioFixo + vendas * 0.15

# Saída
# Imprima o total que o funcionário deverá receber, conforme exemplo fornecido. (2 casas decimais)
# TOTAL = R$ 684.54 -> TOTAL = R$

# Code
nome = input()
salarioFixo = float(input())
vendas = float(input())

salarioTotal = salarioFixo + vendas * 0.15

print("TOTAL = R$ " + "{:.2f}".format(salarioTotal))