from ctypes.wintypes import PINT
from Librery import *

def main():
    # Aplicacion de los Dicionarios 
    #persona = {
    #    "nombre": "Andres",
    #    "apellido": "Monterrosa",
    #    "edad": "21"
    #}

    persona = {
        "datospersonales":{
            "nombre": "Andres",
            "apellido": "Monterrosa",
            "edad": "21"
        },
        "salarial": {
            "salario": 2000000,
            "subtransporte": 50000,
            "subalimentacion": 60000
        }
    }

    # print(persona["nombre"] + " " + persona["apellido"])
    print("")
    # persona["nombre"] = "Camilo"
    print(f"{persona['datospersonales']['nombre']} {persona['datospersonales']['apellido']}")




if __name__ == "__main__":
    main()