"""
programa4.py 
Nombre:Miguel Angel Lira Tellez
Fecha:26/01/2023
Descripcion: se uso el comando format para hacer una cadena de texto o datos 
"""
numero1=10# se asignan variables 
numero2=5#codigo sin errores 
print("{}+{}={}".format(numero1,numero2,numero1+numero2))#solo imprime la suma 
print("{}+{}={}".format(numero1,numero2,numero1+numero2)) # imprime la suma de manera correcta,enj una sola linea, formando una cadena "10+5=15"

#codigo con algunos cambios de sintaxis, o cambiando el nombre de la avriable 
print("{n1}+{n2}={suma}".format(n1=numero1,n2=numero2,suma=numero1+numero2))
print("{n2}+{n2 {n2}".format(n1=numero1,n2=numero2,suma=numero1+numero2))#canbiando las variables usando el nombre, se cambio el n1,n2, suma por el n2
print("{n1}+{n2}={suma}".format(n1=numero1,n2=numero2,suma=numero1+numero2)) #key error es cuando no encuentra la varible o no esta signada 
print("{n1}+{n2}={suma}".format(n1=numero1,n2=numero2,suma=numero1+numero2))
print("{numero1}+{numero2}={suma}".format(numero1=numero1,numero2=numero2,suma=numero1+numero2))# se reemplazaron los n1 por el nombre completo,dando el mismo resultado
print("{}+{}={}".format(numero1,numero2,numero1+numero2))#no funciona por que no se crean variables, {numero1},{numero2}
