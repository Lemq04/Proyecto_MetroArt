class Autor:
    def __init__(self, nombre_autor, nacionalidad, fecha_nacimiento, fecha_muerte):
        """Inicializa las variables de la clase Autor

        Args:
            nombre_autor (str): Nombre del autor
            nacionalidad (str): Nacionalidad del autor
            fecha_nacimiento (str): Fecha de nacimiento del autor
            fecha_muerte (str): Fecha de muerte del autor
        """
        self.nombre_autor = nombre_autor
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_muerte = fecha_muerte

    def show(self):
        """Muestra la informacion del autor(nombre, nacionalidad, fecha denacimiento y muerte)
        """
        print(f"Nombre del Autor: {self.nombre_autor}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print(f"Fecha de Nacimiento: {self.fecha_nacimiento}")
        print(f"Fecha de Muerte: {self.fecha_muerte}")