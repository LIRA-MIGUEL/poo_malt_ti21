class Alumno:

    __nombre = None
    __matricula = None
    __carrera = None


    def __init__(self):
        print("Alumnos\n")
        
    def setNombre(self, nombre):
        self.__nombre = nombre

    def getNombre(self):
        return self.__nombre

    def setMatricula(self, matricula):
        self.__matricula = matricula

    def getMatricula(self):
        return self.__matricula

    def setCarrera(self, carrera):
        self.__carrera = carrera

    def getCarrera(self):
        return self.__carrera


miguel = Alumno()




miguel.setNombre("Miguel Angel")
print(miguel.getNombre())
miguel.setMatricula("1722110271")
print(miguel.getMatricula())
miguel.setCarrera("Ingeniería en Desarrollo de Software Multiplataforma")
print(miguel.getCarrera())
