# Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias
#OBS: para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias
#OBS: Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, 
#como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

# Entrada
# O arquivo de entrada contém um valor inteiro.

# Saída
# Imprima a saída conforme exemplo fornecido.
#1 ano(s)
#1 mes(es)
#5 dia(s)

# Code
diasTotais = int(input())

anos = diasTotais // 365
diasTotais %= 365
meses = diasTotais // 30
diasTotais %= 30
dias = diasTotais

print(anos, "ano(s)")
print(meses, "mes(es)")
print(dias, "dia(s)")