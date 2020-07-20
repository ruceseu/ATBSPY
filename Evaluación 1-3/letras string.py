def contar():
    largo=len(strings)
    if largo<5:
        print("Menos de 5")
    elif largo>=5 and largo<=10:
        print("Entre 5 y 10")
    else:
        print("Haz pasado el límite")

strings=input("Introduce tu string")
contar()


