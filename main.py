from museo import Museo
from api import api

def main():
    """Inicializa el programa
    """
    museo=Museo(api)
    museo.menu()

main()