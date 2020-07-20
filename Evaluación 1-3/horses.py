# 1 3 13 19 25
# 5 14 18 20 24
# 6 7 15 17 23
# 4 8 9 10 22
# 2 11 12 16 21
import random
#crea una lísta, con 3 listas adentro
#list_numbers=[]
#for i in range(3):#pasa este código 3 veces
    #list_numbers.append(list(range(1,6))) #agrega los números del 1 al 5 a la lista

#print(list_numbers)
#numbers= [i for i in range (1,26)] #hace la lista de 25 números
#random.shuffle(numbers) #desordena los números
shuffled=[1, 4, 10, 11, 25,
 21, 2, 17, 8, 23,
  13, 14, 16, 20, 5, 
  9, 6, 7, 22, 15, 
  18, 12, 24, 3, 19] 

# #horses=[[], 
# [], 
# [], 
# [], 
# [],
# ]

# # for i in horses:
#     for j in range(5):
#         horses[j].append(shuffled.pop())

horses=[[19, 15, 5, 23, 25], 
[3, 22, 20, 8, 11], 
[24, 7, 16, 17, 10],
[12, 6, 14, 2, 4], 
[18, 9, 13, 21, 1]]

for race in horses:
    (race.sort())
    print(race)

def last(x):
    return x[-1]

new_horses=sorted(horses,key=last,reverse=True)
print()

for race in new_horses:
    print(race)
