class Departamento:
    def __init__(self, id_departamento, nombre_departamento):
        self.id_departamento = id_departamento
        self.nombre_departamento = nombre_departamento

    def show(self):
        print(f"ID de Departamento: {self.id_departamento}")
        print(f"Nombre del Departamento: {self.nombre_departamento}")