

from ast import If


def calcularsueldo(salario, diastrabajados):
    sueldoPagar = salario/30 * diastrabajados
    return sueldoPagar

def main():
    SALARIO_MIN = 100000
    SUB_TRANS = 60000
    SUB_ALIM = 120000
    BONO = 50000
    nombre = input("Dijite el nombre " )
    salario = int(input("Dijite el salario " ))
    diastrabajados = int(input("Dijite los dias trabajados "))
    sueldoPagar = calcularsueldo(salario, diastrabajados)

    if  salario < (SALARIO_MIN * 2):
        sueldoPagar = sueldoPagar + SUB_ALIM + SUB_TRANS
    else:
        sueldoPagar = sueldoPagar + BONO


    print(f"Mi nombre es: {nombre} , mi salario es: {salario} y mi sueldo a pagar es: {sueldoPagar:.0f}")


if __name__ == "__main__":
    main()


