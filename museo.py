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
        self.load_departamentos()
        for dept in self.departmentos:
            dept.show()
            print()
        dept_id = input("Indique el id del departamento: ")
        if dept_id.isdigit():
            response = requests.get(self.api + f"search?q=&departmentId={dept_id}")
            data = response.json()  
            if data["total"]==0:
                print("No se encontraron obras para este departamento.")
                return       
            self.mostar_obras(data["objectIDs"])
        else:
            print("Error: Debe ingresar un número.")
            return
    
    def buscar_por_nacionalidad(self):
        pass
    
    def buscar_por_nombre_autor(self):
        pass

    def load_departamentos(self):
        dept_response = requests.get(self.api + "departments")
        dept_data = dept_response.json()
        for dept in dept_data['departments']:
            self.departmentos.append(Departamento(dept['departmentId'], dept['displayName']))

    def mostrar_obras(self, obras_id):
        pass
        