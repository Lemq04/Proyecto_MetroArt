from museo import Museo
from api import api

def main():
    museo=Museo(api)
    museo.menu()

main()