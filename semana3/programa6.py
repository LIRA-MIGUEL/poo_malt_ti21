"""
programa5.py 
Nombre:Miguel Angel Lira Tellez
Fecha:30/01/2023
Descripcion: calcular el area y perimetro de un triangulo
"""
base=float(input("medida de la base: "))# float(flotante) lo asigne asi para ver que pasaba. asigne el valor de la base
altura=float(input("medida de la altura: "))#el comandpo int se usa para convertir un dato y el input se usa para introducir un dato. asigne la altura 
lado1=float(input("medida del lado1: "))
lado2=float(input("medida del lado2: "))#solo asigne dos lados ya que conte la base como uno de los lados 
area=(base*altura)/2
perimetro=lado1+lado2+base
print("el area es ={}".format(area))# el comando format es para incluir cadenas de texto, se da el valor del area 
print("el perimetro es={}".format(perimetro))# te da el valor del perimetro 