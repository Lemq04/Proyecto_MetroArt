import requests
import json
from departamento import Departamento
from autor import Autor
from obra import Obra

class Museo:
    
    def __init__(self,api):
        self.api=api
        self.departmentos = []
        self.obras=[]
        self.autores=[]
        self.nacionalidades = []
   
    def menu(self):
        while True:
            print("v1.4.5")
            print("\n---- Menú Principal del Catálogo de Arte ----\n1.- Buscar obras por Departamento\n2.- Buscar obras por Nacionalidad del Autor\n3.- Buscar obras por Nombre del Autor\n4.- Salir")

            opcion = input("Ingrese su opción: ")

            if opcion == "1":
                self.buscar_por_departamento()
            elif opcion == "2":
                self.buscar_por_nacionalidad()
            elif opcion == "3":
                self.buscar_por_nombre_autor()
            elif opcion == "4":
                print("¡Gracias por visitar el catálogo del Museo Metropolitano de Arte!")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

    def buscar_por_departamento(self):
        pass
    
    def buscar_por_nacionalidad(self):
        pass
    
    def buscar_por_nombre_autor(self):
        pass
        