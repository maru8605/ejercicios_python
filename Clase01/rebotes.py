altura_rebote = 60
num_rebotes = 1

while num_rebotes <= 10:
    print(altura_rebote)
    altura_rebote = altura_rebote - altura_rebote*40/100
    num_rebotes = num_rebotes + 1


# ej 1.6
nombre = input('ingresa tu nombre: ')
print('hola', nombre)
