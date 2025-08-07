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
        

    def show_detail(self):
        print(f"\n--- Detalles de la Obra ---")
        print(f"Título: {self.titulo}")
        print(f"Nombre del Artista: {self.autor_obra.nombre_autor}")
        print(f"Nacionalidad del Artista: {self.autor_obra.nationality}")
        print(f"Fecha de Nacimiento del Artista: {self.autor_obra.birthDate}")
        print(f"Fecha de Muerte del Artista: {self.autor_obra.fecha_muerte}")
        print(f"Tipo (Classification): {self.tipo}")
        print(f"Año de Creación (Object Date): {self.anio_creacion}")
      