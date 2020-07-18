import sys
subtot=float(input("Introduce el subtotal"))
ship=300

print("Tu subtotal es de "+ str(subtot))

if subtot>=1000:
    total=subtot-ship
    print ("¡Envío gratis! el total es de "+ str(total)+"MXN")
else:
    total=subtot+ship
    print ("El total es de "+ str(total)+"MXN, con"+str(ship)+" MXN de envío")

print("¿Deseas facturar tu compra?")
print("1. Si")
print("2. No")
fac=input()

if fac=="1":
    iva=total*.16
    totfac=total+iva
    print("El total ha cambiado a "+ str(totfac)+" MXN, con "+str(iva)+"de IVA")
elif fac=="2":
    print("No facturarás esta compra.")

print("Gracias por comprar con nosotras")
sys.exit()