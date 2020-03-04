# Dois carros (X e Y) partem em uma mesma direção. O carro X sai com velocidade constante de 60 Km/h e 
#o carro Y sai com velocidade constante de 90 Km/h.

# x e y partem mesma direção
# velocidade_x = 60(km/h)
# velocidade_y = 90(km/h)

# Em uma hora (60 minutos) o carro Y consegue se distanciar 30 quilômetros do carro X, ou seja, consegue se afastar um quilômetro a cada 2 minutos

# Leia a distância (em Km) e calcule quanto tempo leva (em minutos) para o carro Y tomar essa distância do outro carro.

# Entrada
# distancia(km) (int)

# Calcular
# tempo (em minutos) para o carro Y distanciar 'distancia' do carro x.

# Saída
# 'tempo' minutos

# Code
velocidade_x = 60 #km/h
velocidade_y = 90 #km/h
dif_velocida = 30 #Km/h

distancia = int(input()) #km

#v = d/t
tempo = int( (distancia / dif_velocida) * 60) #(tempo em horas)*60 -> tempo em minutos  

print(tempo, "minutos")
