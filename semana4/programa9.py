"""
programa9.py 
Nombre:Miguel Angel Lira Tellez
Fecha:7/0/2023
Descripcion: Formas de resolver un problema 
"""
#Forma numero1, comando if 
numero1=int(input("Numero1: "))
numero2=int(input("Numero2: "))
if numero1 > numero2:
    print(numero1)
if numero2>numero1:
    print(numero2)
if numero1==numero2:
    print(None)

#Forma 2 con else al final
if numero2>numero1:
    print(numero2)
if numero1>numero2:
    print(numero2)
else:
    print(None)

#Forma 3 con elif y else
if numero1>numero2:
    print(numero1)
elif numero2>numero1:
    print(numero2)
else:
    print(None)

#Forma 4 con igual primero
if numero1==numero2:
    print(None)
elif numero1>numero2:
    print(numero1)
elif numero2>numero1:
    print(numero2)

#Forma 5 cambiando el simbolo mayor que al menor que 
if numero1<numero2:
    print(numero2)
if numero2<numero1:
    print(numero1)
if numero1==numero2:
    print(None)

#Forma 6 cambiando un simbolo mayor que 
if numero2>numero1:
    print(numero2)
if numero2<numero1:
    print(numero1)
else:
    print(None)

#Forma 7 la que propuso el compañero
if(numero2<numero1>numero2):
    print(numero1)
if(numero1<numero2>numero1):
    print(numero2)
else:
    print(None)

#Forma 8 con if anidados
if numero1<=numero2:
    if numero1==numero2:
        print(None)
else:
    print(numero2)
    print(numero1)

#Forma 9 con simbolo de diferencia
if numero1<=numero2:
    print(None)
elif numero1!=numero2:
    print(numero1)
elif numero2!=numero1:
    print(numero2)