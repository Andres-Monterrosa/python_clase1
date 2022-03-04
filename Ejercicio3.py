# ********************************************
#               Manejo de Listas
# ********************************************
"""
**********************************************
                Manejos de Listas
**********************************************
"""
def listas():
    lista1 = []
    lista2 = list()

    listaconElementos = [30, 2000000, "Andres Monterrosa", "estudiante", True, ["Bachiller", "Estudiante de ingenieria"]]

    # print(listaconElementos)

    # Utilizando el ciclo for
    print("mostrar elemostos con ciclo for")
    for i in range(len(listaconElementos)):
        print(listaconElementos[i])
    
    print("")
    print("") 

    print("mostrar elemostos con ciclo while")
    j=0
    while j < len(listaconElementos):
        print(listaconElementos[j])
        j = j + 1
    
    listaconElementos[1] = listaconElementos[1] + 200000

    print("")
    print(listaconElementos[-1][1])
    print("")
    print(listaconElementos[0:3]) # Musta la posicion de la 0 a la 3
    print("")
    print(listaconElementos[1:6:2])
    print("")
    print(listaconElementos[0:6:2])
    print("")
    # Agrega elemento al final de la lista 
    listaconElementos.append(["sede Riohacha", "Miguel soto"])
    print("")
    # Agrega elemento en la posicion x
    listaconElementos.insert(2,["sede Riohacha", "Miguel soto"])
    print(listaconElementos)
    print("")
    # Elininar elemento en la posicion x
    del listaconElementos[2]
    print(listaconElementos)
    print("")
    # Elimina elementos de la lista 
    listaconElementos.remove("estudiante")
    print(listaconElementos)

def main():
    listas()



if __name__ == "__main__":
    main()