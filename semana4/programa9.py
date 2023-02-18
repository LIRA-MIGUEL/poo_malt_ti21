"""
programa9.py 
Nombre:Miguel Angel Lira Tellez
Fecha:7/0/2023
Descripcion: Formas de resolver un problema 
"""
#Forma numero1, comando if 
numero1=int(input("Numero1: ")) #se asignan las variables 
numero2=int(input("Numero2: "))
if numero1 > numero2: # se usa el if para poner una condicion 
    print(numero1)
if numero2>numero1: # si la primera condicion no se cumple, se pasa a la siguiente 
    print(numero2)
if numero1==numero2: #pero si las primeras condiciones son falsas pasa a la siguiente condicion y se imprime None 
    print(None)

#Forma 2 con else al final
if numero2>numero1: # se asigna una condicon si se cumple se imprime el mayor 
    print(numero2)
if numero1>numero2: # si no se cumple se pasa a la siguiente condicion 
    print(numero2)
else: # se usa el comando else, el cual sirve para cuando las primeras condiciones no se cumplen automaticamente pasa a imprimir el None 
    print(None)

#Forma 3 con elif y else
if numero1>numero2: # se establece la primera condicion 
    print(numero1) # se imprime el resultadfo de la condicion 
elif numero2>numero1: #Esta es la siguiente condición, que se verifica solo si la primera condición es falsa.
    print(numero2)
else: # si las dos primeras condicones no se cumplen pasa a imprimir None 
    print(None)

#Forma 4 con igual primero
if numero1==numero2: # se asigna la primera condicon, si los dos numeros son iguales imprime None 
    print(None)
elif numero1>numero2: # si no son iguales pasa a la siguiente condicon 
    print(numero1) 
elif numero2>numero1:  # si no se cumple las primeras condiciones pasa a imprimir la ultima condicion 
    print(numero2)

#Forma 5 cambiando el simbolo mayor que al menor que 
if numero1<numero2: #se asigna condiciones, y la que se cumpla se imprime 
    print(numero2)
if numero2<numero1: #se asigna condiciones, y la que se cumpla se imprime
    print(numero1)
if numero1==numero2: #se asigna condiciones, y la que se cumpla se imprime
    print(None)

#Forma 6 cambiando un simbolo mayor que 
if numero2>numero1: # se asigna una condicion
    print(numero2)
if numero2<numero1:# si no se cumple la primera pasa con la segunda 
    print(numero1)
else: # si no es ninguna de las condiciones anteriores, imprime None 
    print(None)

#Forma 7 la que propuso el compañero
if(numero2<numero1>numero2): #Si numero1 es mayor que numero2 y numero1 es mayor que cualquier otro número que sea menor que numero1, entonces la condición es verdadera y el siguiente bloque de código se ejecutará.
    print(numero1)
if(numero1<numero2>numero1): #Si numero2 es mayor que numero1 y numero2 es mayor que cualquier otro número que sea menor que numero2, entonces la condición es verdadera y el siguiente bloque de código se ejecutará.
    print(numero2)
else: # Si ambas condiciones anteriores son falsas, se ejecutará el siguiente bloque de código.
    print(None)

#Forma 8 con if anidados
if numero1<=numero2: #si el  numero1 es menor o igual que numero2
    if numero1==numero2: # Si numero1 es igual a numero2, entonces la condición es verdadera
        print(None)
else: #Si ambas condiciones anteriores son falsas, se ejecutará el siguiente bloque de código.
    print(numero2)
    print(numero1)

#Forma 9 con simbolo de diferencia
if numero1<=numero2: # si el  numero1 es menor o igual que numero2
    print(None)
elif numero1!=numero2: # si el numero1 es diferente al numero 2 entonces es verdadera 
    print(numero1)
elif numero2!=numero1: #si el numero1 es diferente al numero 2 entonces es verdadera 
    print(numero2)