"""
programa10.py 
Nombre:Miguel Angel Lira Tellez
Fecha:09/02/2023
Descripcion: uso del comando def y return
"""
def mayor(numero1,numero2): # se asignan los numeros, y se define una funcion 
    result=None# se asigna una funcion 
    if numero1>numero2: # con el if se agrega una condicion 
        result=numero1
    elif numero2>numero1: # se agrega otra solucion
        result=numero2
    return result # la funcion se detiene y devuelve el valor return 
print(mayor(2,1)) #se hacen las pruebas
print(mayor(1,2)) # si todas las pruebas se cumplen entoces estan bien 
print(mayor(2,2))
print(mayor(2,-1))
print(mayor(-1,2))
print(mayor(-1,-1))
print(mayor(-2,-1))
print(mayor(-1,-2))
