import requests
from PIL import Image

class Obra:
    def __init__(self, id_obra, titulo, autor_obra, tipo, anio_creacion,imagen):
        """Inicializa las variables de la clase Obra.

        Args:
            id_obra (int): Identificacion de la obra
            titulo (str): Titulo de la obra
            autor_obra (Autor): Objeto Autor de la obra asociada 
            tipo (str): Tipo de obra(pintura, escultura, etc.)
            anio_creacion (str): Año de creacion de la obra 
            imagen (str): URL de la imagen de la obra 
        """
        self.id_obra = id_obra
        self.titulo = titulo
        self.autor_obra = autor_obra  
        self.tipo = tipo
        self.anio_creacion = anio_creacion
        self.imagen_url = None  
        self.imagen=imagen

    def show(self):
        """Despliega la informacion basica de la obra(ID, titulo y nombre del autor) 
        """
        print(f"ID de Obra: {self.id_obra}")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor_obra.nombre_autor}")
        

    def show_detalle(self):
        """Muestra informacion detallada de la obra y la imagen.
        """
        print(f"\n--- Detalles de la Obra ---")
        print(f"Título: {self.titulo}")
        print(f"Nombre del Artista: {self.autor_obra.nombre_autor}")
        print(f"Nacionalidad del Artista: {self.autor_obra.nacionalidad}")
        print(f"Fecha de Nacimiento del Artista: {self.autor_obra.fecha_nacimiento}")
        print(f"Fecha de Muerte del Artista: {self.autor_obra.fecha_muerte}")
        print(f"Tipo: {self.tipo}")
        print(f"Año de Creación: {self.anio_creacion}")
        opcion=input("Quiere ver la imagen?\n1.-Si\n2.-No\n")
        print()
        if opcion=="1":
            if self.imagen!="":
                imagen_guardada=self.guardar_imagen_desde_url()
                img = Image.open(imagen_guardada)
                img.show()
            else:
                print("La obra no tiene imagen")
      
    def guardar_imagen_desde_url(self):
        """Guarda la Ruta o URL de la imagen asociada a la obra

        Returns:
            _str: Nombre del archivo de la imagen guardada
        """
        
        try:
            response = requests.get(self.imagen, stream=True)
            response.raise_for_status()

            content_type = response.headers.get('Content-Type')
            extension = '.png'  
            if content_type:
                if 'image/png' in content_type:
                    extension = '.png'
                elif 'image/jpeg' in content_type:
                    extension = '.jpg'
                elif 'image/svg+xml' in content_type:
                    extension = '.svg'
                
            nombre_archivo_final = f"{self.titulo}{extension}"

            with open(nombre_archivo_final, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        file.write(chunk)
            print(f"Imagen guardada '{nombre_archivo_final}'")


        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
        except IOError as e:
            print(f"Error: {e}")
        return nombre_archivo_final