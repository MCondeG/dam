import random

class Biblioteca:
    
    __nombre = []
    __estado = []
    __prestado = []
    __TAMAÑOMAX = 5
    __tamañoActual = 0
    
    
    def iniciar(self):
        
        self.__tamañoActual = 5
        
        self.__nombre[0] = ("El Señor de los Anillos")
        self.__nombre[1] = ("Harry Potter y la Piedra Filosofal")
        self.__nombre[2] = ("Los Pilares de la Tierra")
        self.__nombre[3] = ("Canción de Hielo y Fuego")
        self.__nombre[4] = ("El Quijote")
        
        for i in range(0, self.__TAMAÑOMAX):
            self.__estado[i] = random.randint(-1, 1)
            self.__prestado[i] = random.randint(0, 10)
    
    
    def __init__(self):
        self.iniciar()