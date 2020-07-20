import random
numerosec = random.randint(1, 20)
print('Pienso en un número entre 1 y 20')


for int_adivina in range(1, 7):
    adivina=int(input(('Adivina el número que estoy pensando.')))

    if adivina < numerosec:
        print('Te fuiste muy abajo.')
    elif adivina > numerosec:
        print('Te fuiste muy arriba.')
    else:
        break

if adivina == numerosec:
    print('Chido! Adivinaste en ' + str(int_adivina) + ' intentos')
else:
    print('Nel. El número era ' + str(numerosec))