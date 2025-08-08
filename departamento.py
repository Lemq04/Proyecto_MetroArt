class Departamento:
    def __init__(self, id_departamento, nombre_departamento):
        """Inicializar las variables de la clase Departamento 

        Args:
            id_departamento (int): ID del departamento
            nombre_departamento (str): Nombre del departamento
        """
        self.id_departamento = id_departamento
        self.nombre_departamento = nombre_departamento

    def show(self):
        """Muestra la informacion de los departamentos(ID y el nombre)
        """ 
        print(f"ID de Departamento: {self.id_departamento}")
        print(f"Nombre del Departamento: {self.nombre_departamento}")