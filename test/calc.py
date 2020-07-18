def suma(x,y):
    return x+y
def resta(x,y):
    return x-y
def multiplica (x,y):
    return x*y
def divide (x,y):
    return x/y

print("Hola! ¿Qué operación quieres realizar?")
print("1.Suma")
print("2.Resta")
print("3.Multiplica")
print("4.Divide")

while True:
    oper=input("Introduce tu elección (1,2,3,o 4)")
    if oper=="1" or oper=="2" or oper=="3" or oper=="4":
        num1=float(input("Introduce el primer número"))
        num2=float(input("Introduce el segundo número"))
        
        if oper=="1":
            print(num1, "+", num2,"=", suma(num1,num2))
        elif oper=="2":
            print(num1, "-", num2,"=", resta(num1,num2))
        elif oper=="3":
            print(num1, "*", num2,"=", multiplica(num1,num2))
        elif oper=="4":
            print(num1, "/", num2,"=", divide(num1,num2))
    else:
        print("Introduce una elección válida")

        
    
