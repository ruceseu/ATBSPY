def spam ():
    eggs=99

spam()
print(eggs)#esta es global
# parametros dentro de una función son locales (1)


def spam():
    eggs=99
    bacon()
    print (eggs)

def bacon ()
    ham=101
    eggs=0
    
spam()
#las dos eggs son diferentes (4)

def spam():
    print (eggs)

eggs=42
spam()
    #assignment statement en la función  = local
    #no assignment =global

def spam():
    global eggs
    eggs= "Hello"
    print (eggs)

eggs= 42
spam()
print(eggs)
#global 
