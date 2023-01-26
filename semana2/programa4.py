"""
programa4.py 
Nombre:Miguel Angel Lira Tellez
Fecha:26/01/2023
Descripcion:
"""
numero1=10
numero2=5
print("{}+{}=".format(numero1,numero2,numero1+numero2))#solo imprime la suma 
print("{}+{}={}".format(numero1,numero2,numero1+numero2))
print("{n1}+{n2}={suma}".format(n1=numero1,n2=numero2,suma=numero1+numero2))
print("{n2}+{n2}={n2}".format(n1=numero1,n2=numero2,suma=numero1+numero2))#canbiando las variables usando el nombre 
print("{n1}+{n2}={suma}".format(n1=numero1,n2=numero2,suma=numero1+numero2)) #key error es cuando no encuentra la varible o no esta signada 
print("{n1}+{n2}={suma}".format(n1=numero1,n2=numero2,suma=numero1+numero2))
print("{numero1}+{numero2}={suma}".format(numero1=numero1,numero2=numero2,suma=numero1+numero2))# se reemplazaron los n1 por el nombre completo,dando el mismo resultado
print("{}+{}={}".format(numero1,numero2,numero1+numero2))#no funciona por que no se crean variables, {numero1},{numero2}
