class Autor:
    def __init__(self, nombre_autor, nacionalidad, fecha_nacimiento, fecha_muerte):
        self.nombre_autor = nombre_autor
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_muerte = fecha_muerte

    def show(self):
        print(f"Nombre del Autor: {self.nombre_autor}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print(f"Fecha de Nacimiento: {self.fecha_nacimiento}")
        print(f"Fecha de Muerte: {self.fecha_muerte}")