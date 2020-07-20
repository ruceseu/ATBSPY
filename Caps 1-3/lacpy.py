equipo=("")
print("¿Eres equipo LAC, MOS o AMBOS?")
equipo=input()

if equipo=="LAC":
    print("¡Eres Luuces ,Sam, Mich, Montse, Eduardo o Fofo!")
elif equipo=="MOS":
    print("¡Eres Diego!")
elif equipo=="AMBOS":
   print("Eres Ricardo!")
elif equipo!= "MOS" or "LAC" or "AMBOS":
    print("La información dada no corresponde a ningún equipo")
