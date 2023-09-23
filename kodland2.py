import random
a="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
digitos=int(input("cuantos digitos quieres que tenga la contrasena? "))
contra=""
for i in range (digitos):
    indice=random.randint(0,len(a)-1)
    dato=a [indice]
    contra=contra+ dato
print(contra)
