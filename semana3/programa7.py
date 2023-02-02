"""
programa5.py 
Nombre:Miguel Angel Lira Tellez
Fecha:31/01/2023
Descripcion: Calcular el area y perimetro de un circulo y un cuadrado 
"""
print("inprime y calcula el area y perimetro de un cuadrado")
lado1=float(input("lado1: "))#idea original que consiste en pedir los 4 lados del cuadrado
lado2=float(input("lado2:"))
lado3=float(input("lado3: "))
lado4=float(input("lado4: "))
area=lado1**2 # al tener las mismas medidas solo es necesario elevar al cuadrado un solo lado
perimetro= lado1+lado2+lado3+lado4#el perimetro se suman los 4 lados
print("el area es ={}".format(area))
print("el perimetro es ={}".format(perimetro))

print("imprime y calcula area y perimetro de un circulo")
radio=float(input("radio: "))
pi=3.1416#se da valor a pi 
diametro=2 #asigne el valor dos a dimetro ya que es el doble del radio 
area=pi*radio**2#pi por radio elevado al cuadrado 
perimetro=pi*diametro*(radio)#pi por el diametro por el radio ya que es doble  
print("el area de un circulo es={}".format(area))
print("el perimetro de un circulo es={}".format(perimetro))


