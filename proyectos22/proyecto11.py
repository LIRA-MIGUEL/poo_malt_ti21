"""
proyecto11.py 
Nombre:Miguel Angel Lira Tellez
Fecha:15/02/2023
Descripcion: 
"""
class Pan: #definimos la clase pan
    def __init__(self, tipo, sabor, precio): #metodo constructor de las clases 
        self.tipo = tipo # se inician las instancias 
        self.sabor = sabor
        self.precio = precio

    def describir(self): #imprime una descripcion 
        print(f"Este es un pan de tipo {self.tipo}, sabor {self.sabor}, y precio {self.precio}.")

    def cambiar_precio(self, nuevo_precio):
        self.precio = nuevo_precio


        
    

    