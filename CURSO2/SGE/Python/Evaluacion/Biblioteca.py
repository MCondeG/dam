import random

class Biblioteca:
    
    __nombre = []
    __estado = []
    __prestado = []
    __TAMAÑOMAX = 5
    __tamañoActual = 0
    
    
    def iniciar(self):
        
        self.__tamañoActual = 5
        
        self.__nombre.append("El Señor de los Anillos")
        self.__nombre.append("Harry Potter y la Piedra Filosofal")
        self.__nombre.append("Los Pilares de la Tierra")
        self.__nombre.append("Canción de Hielo y Fuego")
        self.__nombre.append("El Quijote")
        
        for i in range(0, self.__tamañoActual):
            self.__estado.append(int(random.randint(-1, 1)))
            self.__prestado.append(int(random.randint(0, 10)))
    
    
    def __init__(self):
        self.iniciar(5)
        
    
    def getNombre(self):
        return self.__nombre
    
    def getEstado(self):
        return self.__estado
    
    def getPrestado(self):
        return self.__prestado
    
    
    def buscaLibro(self, Nombre):
        
        for i in range(0, self.__tamañoActual):
            if (Nombre == self.__nombre[i]):
                
    
    def compraLibro(self, Nombre):
        
        if (self.__tamañoActual < self.__TAMAÑOMAX):
            self.__nombre.append(Nombre)
            self.__estado.append(int(0))
            self.__prestado.append(int(0))
            self.__tamañoActual += 1
        else:
            print("ERROR. Biblioteca completa")
            
    def tiraLibro(self, Nombre):
        
    def sacaLibro(self, Nombre):
        
    def devuelveLibro(self, Nombre):
        
    def libroMasPrestado(self):