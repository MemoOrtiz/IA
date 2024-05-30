import random
#estados iniciales de las jarras
x = 0   #jarra de 4 galones
y = 0   #jarra de 3 galones
#contador para saber cuantos movimientos se hicieron
contador = 1

# Ejecutamos un while mientras jarra de 4 galones no sea igual a 2
while x != 2:
    #Se guarda el estado anterior
    x_anterior = x
    y_anterior = y

    #Se elige una regla al azar
    regla = random.randint(1, 8)

    #Aplicamos alguna regla seleccionada y se actualiza el estado de las jarras y el contador
    
    #Llenar 4G
    if regla == 1 and x < 4:
        x = 4
        print(f"{contador} El nuevo estado : ({x}, {y})")
        contador += 1
    #Llenar 3G    
    elif regla == 2 and y < 3:
        y = 3
        print(f"{contador} El nuevo estado : ({x}, {y})")
        contador += 1
    #Vaciar 4G     
    elif regla == 3 and x > 0:
        x = 0
        print(f"{contador} El nuevo estado : ({x}, {y})")
        contador += 1
    #Vaciar 3G
    elif regla == 4 and y > 0:
        y = 0
        print(f"{contador} El nuevo estado : ({x}, {y})")
        contador += 1
    #Vaciar 4G a 3G hasta que se llene
    elif regla == 5 and x > 0 and y < 3 and x + y >= 3:
        x = x_anterior - (3 - y_anterior)
        y = 3
        print(f"{contador} El nuevo estado : ({x}, {y})")
        contador += 1
    #Vaciar 3G a 4G hasta que se llene
    elif regla == 6 and x < 4 and y > 0 and x + y >= 4:
        y = y_anterior - (4 - x_anterior)
        x = 4
        print(f"{contador} El nuevo estado : ({x}, {y})")
        contador += 1
    #Vaciar todo de 4G a 3G 
    elif regla == 7 and x > 0 and y < 3 and x + y <= 3:
        y = x + y
        x = 0
        print(f"{contador} El nuevo estado : ({x}, {y})")
        contador += 1
    #Vaciar todo de 3G a 4G    
    elif regla == 8 and x < 4 and y > 0 and x + y <= 4:
        x = x + y
        y = 0
        print(f"{contador} El nuevo estado : ({x}, {y})")
        contador += 1
