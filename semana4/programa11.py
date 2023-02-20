"""
programa11.py 
Nombre:Miguel Angel Lira Tellez
Fecha:7/0/2023
Descripcion: Formas de resolver un problema 
"""
def mayor(numero1:int,numero2:int): # se asignan los numeros, y se define una funcion 
     result=None
     if numero1>numero2:  #con el if se agrega una condicion 
        result=numero1
     elif numero2>numero1: #se agrega otra solucion
         result=numero2
     return result # la funcion se detiene y devuelve el valor return 
    
print(mayor(2,1))
print(mayor(1,2)) # se hacen las pruebas, si de cumplen todas significa que el rpoblema esta bien 
print(mayor(2,2))
print(mayor(2,-1))
print(mayor(-1,2))
print(mayor(-1,-1))
print(mayor(-2,-2))
print(mayor(-1,-2))
