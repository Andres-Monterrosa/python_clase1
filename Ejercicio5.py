import os

class Persona():
    def __init__(self):
        self.__perso = {}
        self.__listaPersonas = []


    def agregarPersona(self, Nombre, Apellido, Cedula, Direccion, Telefono):
        self.__perso = {
            "Nombre": Nombre,
            "Apellido": Apellido,
            "Cedula": Cedula,
            "Direccion": Direccion,
            "Telefono": Telefono,
        }
        self.__listaPersonas.append(self.__perso)

class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.__devengado = {}
        self.__deduccion = {}
        self.__listaEmpleados =[]

    def agregarEmpleados(self):
        Nombre = input("Digite el nombre")
        Apellido = input("Digite el apéllido")
        Cedula = input("Digite el cedula")
        Direccion = input("Digite el direccion")
        Telefono = input("Digite el telefono")
        Salario = float(input("Digite el salario"))

        per = {
            "Nombre": Nombre,
            "Apellido": Apellido,
            "Cedula": Cedula,
            "Direccion": Direccion,
            "Telefono": Telefono,
        }

        self.__devengado = {
            'salario': Salario,
            'alimentacion': 0,
            'transporte': 0
        }

        self.__deduccion = {
            'salud': 0,
            'pension': 0
        }

        super().agregarPersona(Nombre, Apellido, Cedula, Direccion, Telefono)

        self.__listaEmpleados.append([
            {"persona": per},
            {"devengado": self.__devengado}, 
            {"deduccion": self.__deduccion}
        ])

    def calcularDevengado(self):
        if self.__devengado['salario'] < 2000000: 
            self.__devengado['alimentacion'] = 80000
            self.__devengado['transporte'] = 70000

    def calcularDeducciones(self):
        self.__deducciones['salud'] = self.__devengado['salario'] * 4 / 100
        self.__deducciones['pension'] = self.__devengado['salario'] * 3.375 / 100


    def menu(self, opciones):
        while(True):
            os.system("clear")
            for item in range(len(opciones)):
                print(opciones[item])

            opcion = input("Digite una opcion correcta")

            if opcion == "1":
                os.system("clear")
                self.agregarEmpleados()
                self.calcularDeducciones()
                self.calcularDevengado()
            elif opcion == "2":
                os.system("clear")
                print(self.__listaEmpleados)
                input("Digite una tecla para continuar")



def menuPrincipal():
    os.system("clear")
    opciones = (
        "MENU PRINCIPAL",
        "1. Adicionar Empleodo",
        "2. Mostrar Empleado",
        "3. Eliminar Empleado",
        "5. Salir"
    )

    emp = Empleado()
    emp.menu(opciones)

def main():
    menuPrincipal()



if __name__ == "__main__":
    main()