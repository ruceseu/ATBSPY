import random,sys

while True:
    print("Bienvenida")
    while True:
        clima=input("Introduzca el tipo de clima que hace hoy")
        if clima=="4":
            sys.exit()
        if clima=="1" or clima=="2" or clima== "3":
            break
        else:
            print("Introduzca 1,2,3 o 4")
    if clima=="1":
        print(random.randint(1,33))
    elif clima=="2":
        print(random.randint(33,66))
    elif clima =="3":
        print(random.randint(66,99))

