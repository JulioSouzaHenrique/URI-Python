# Entrada
# leia o número de um funcionário(int), seu número de horas trabalhadas(int), o valor que recebe por hora(float)
# numFuncionario, numHorasTrabalhadas, vaHora

# Cálculo 
# calcula o salário desse funcionário
# salario = numHorasTrabalhadas * vaHora

# Saída
# mostre o número e o salário do funcionário, com duas casas decimais.
#NUMBER = numFuncionario
#SALARY = U$ salario(2 casas decimais)

# Código
numFuncionario = int(input())
numHorasTrabalhadas = int(input())
vaHora = float(input())

salario = numHorasTrabalhadas * vaHora

print("NUMBER =", numFuncionario)
print("SALARY = U$ " + "{:.2f}".format(salario))