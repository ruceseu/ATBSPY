def a():
    print("a() starts") 
    b()
    d()
    print("a() returns")

def b():
    print("b() starts")
    c()
    print("b() returns")

def c():
    print("c() starts")
    print("c() returns")

def d():
    print("d() starts")
    print("d() returns")

#hasta aquí el código no ha hecho nada, solo definir funciones
a()
#esto empieza la función prim 

