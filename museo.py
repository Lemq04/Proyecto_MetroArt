import requests
import json
from departamento import Departamento
from autor import Autor
from obra import Obra

class Museo:
    """Clase principal que representa el catálogo del Museo Metropolitano de Arte.
    
    Esta clase permite interactuar con la API del museo para buscar y mostrar
    información al usuario sobre departamentos, obras de arte y autores.
    """
    
    def __init__(self,api):
        """Se inicializa con la api del museo y se inicializan las listas globales (self) dentro de la clase Museo
        
        Args:
            api (str): URL base de la API del museo.
        """
        self.api=api
   
    def menu(self):
        while True:
            print("\n---- Menú Principal del Catálogo de Arte ----\n1.- Buscar obras por Departamento\n2.- Buscar obras por Nacionalidad del Autor\n3.- Buscar obras por Nombre del Autor\n4.- Salir")

            opcion = input("Ingrese su opción: ")

            if opcion == "1":
                self.buscar_por_departamento()
            elif opcion == "2":
                self.buscar_por_nacionalidad()
            elif opcion == "3":
                self.buscar_por_nombre_autor()
            elif opcion == "4":
                print("¡Gracias por visitar el catálogo del Museo metropolitano de Arte!")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

    def buscar_por_departamento(self):
        """Busca y muestra obras de arte por departamento del museo.
        
        Carga la lista de departamentos disponibles, permite al usuario seleccionar uno
        y muestra las obras asociadas a ese departamento.
        """
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
            
            print(f"Encontradas {data["total"]} obras.")
            self.mostrar_obras(data["objectIDs"])
        else:
            print("Error: Debe ingresar un número.")
    
    def buscar_por_nacionalidad(self):
        """Busca y muestra obras de arte por nacionalidad del autor.
        
        Carga la lista de nacionalidades disponibles, permite al usuario seleccionar una
        y muestra las obras creadas por autores de esa nacionalidad.
        """
        self.load_nacionalidades()
        print("\n---- Nacionalidades ----")
        for i, nacionalidad in enumerate(self.nacionalidades[0:225], 1):
            print(f"{i}. {nacionalidad}")
        
        nacionalidad_input = input("\nIngrese el número de la nacionalidad: ")
        
        if nacionalidad_input.isdigit():
            num = int(nacionalidad_input)
            if 1 <= num <= 225:
                nacionalidad_seleccionada = self.nacionalidades[num-1]
                print(f"Nacionalidad seleccionada: {nacionalidad_seleccionada}")
                
                response = requests.get(self.api + f"search?artistOrCulture=true&q={nacionalidad_seleccionada}") 
                data = response.json()
                    
                if data["total"]==0:
                    print(f"No se encontraron obras de artistas de nacionalidad {nacionalidad_seleccionada}.")
                    return
                
                print(f"Encontradas {data["total"]} obras.")
                self.mostrar_obras(data["objectIDs"])
                    
            else:
                print("Número inválido. Debe estar entre 1 y 225.")
        else:
            print("Caracter inválido. Debe ser un numero entre 1 y 225.")

    def buscar_por_nombre_autor(self):
        """Busca y muestra obras de arte por nombre del autor.
        
        Solicita al usuario un nombre de autor y muestra las obras asociadas
        a ese autor en la colección del museo.
        """
        nombre_autor = input("Ingrese el nombre del autor: ")
        if nombre_autor!="":
            response = requests.get(self.api + f"search?q={nombre_autor}")
            data = response.json()
                
            if data["total"]==0:
                print(f"No se encontraron obras del autor {nombre_autor}.")
                return 
            
            print(f"Encontradas {data["total"]} obras.")        
            self.mostrar_obras(data["objectIDs"])
            
        else:
            print("Error: Debe ingresar un nombre válido.")

    def load_departamentos(self):
        """Carga la lista de departamentos disponibles desde la API del museo.
        
        Los departamentos se almacenan como objetos Departamento en la lista departmentos.
        """  
        self.departmentos = []
        
        dept_response = requests.get(self.api + "departments")
        if dept_response.status_code==200:
            dept_data = dept_response.json()
            for dept in dept_data['departments']:
                self.departmentos.append(Departamento(dept['departmentId'], dept['displayName']))
        else:
            print("Error al imprimir departamentos")
            return

    def load_nacionalidades(self):
        """Carga la lista de nacionalidades desde un archivo de texto.
        
        Las nacionalidades se leen del archivo 'nacionalidades.txt' y se almacenan
        en la lista nacionalidades.
        """
        self.nacionalidades = []
        with open("nacionalidades.txt", "r") as nacionalidades:
            for nacionalidad in nacionalidades:
                    self.nacionalidades.append(nacionalidad)

    def mostrar_obras(self, obras_ids):
        """Muestra las obras de correspondientes a los IDs proporcionados.
        
        Args:
            obras_ids (list): Lista de IDs de las obras a mostrar.
            
        Muestra las obras en grupos de 10, permitiendo al usuario decidir si desea
        ver más obras o detener la visualización.
        """ 
        self.autor=[]
        self.obra=[]
        i=0
        v=0
        a=0
        print("cargando...mostrando de 10 en 10")
        print()
        for obra in obras_ids:
            
            response=requests.get(self.api+f"objects/{obra}")
            v+=1
            if response.status_code==200:
                data=response.json()
                
                if "objectID" not in data:
                    continue
                
                else:
                    i+=1
                    self.autor.append(Autor(data["artistDisplayName"],data["artistNationality"],data["artistBeginDate"],data["artistEndDate"]))
                    autor_obra=[]
                    for autor in self.autor:
                        autor_obra.append(autor)
                    self.obra.append(Obra(data["objectID"],data["title"],autor,data["classification"],data["objectDate"],data["primaryImage"]))
                    
                    if i%10==0:
                        for autor in self.obra[a:i]:
                            autor.show() 
                            print()
                            a=i
                        opcion=input("Desea ver mas obras:\n1.-Si\n2.-No\n")
                        if opcion=="1":
                            print("cargando...")
                        elif opcion=="2":
                            break
                        else:
                            print("Opcion no valida")
            
            if v==len(obras_ids):
                for autor in self.obra[a:i]:
                            autor.show() 
                            print()


        detalle=input("Desea ver mas detalles:\n1.-Si\n2.-No\n")
        if detalle == "1":
            opcion=input("ID de la obra:\n")
            print()
            self.ofrecer_detalles_obra(int(opcion))
        elif detalle=="2":
            pass
        else:
            print("Opcion no valida")
            

    def ofrecer_detalles_obra(self,opcion):
        """Ofrece detalles adicionales de la obra seleccionada.
        
        Args:
            opcion (list): Lista de obras a las que se les ofrece mostrar los detalles.
        """
        for obra in self.obra:
            if obra.id_obra==opcion:
                obra.show_detalle()


            