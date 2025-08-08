import requests
from PIL import Image

class Obra:
    def __init__(self, id_obra, titulo, autor_obra, tipo, anio_creacion,imagen):
        self.id_obra = id_obra
        self.titulo = titulo
        self.autor_obra = autor_obra  
        self.tipo = tipo
        self.anio_creacion = anio_creacion
        self.imagen_url = None  
        self.imagen=imagen

    def show(self):
        print(f"ID de Obra: {self.id_obra}")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor_obra.nombre_autor}")
        

    def show_detalle(self):
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
            print(f"Imagen guardada exitosamente como '{nombre_archivo_final}'")


        except requests.exceptions.RequestException as e:
            print(f"Error al hacer el request: {e}")
        except IOError as e:
            print(f"Error al escribir el archivo: {e}")
        return nombre_archivo_final