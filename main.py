from entidades.empleado import Empleado
from entidades.operador import Operador
from entidades.supervisor import Supervisor

try:
    print("Esbribe su nombre")
    nombre = input()

    print("Escribe su id")
    id = int(input())

    print("Escribe su sueldo")
    sueldo_base = float(input())

    print("Escribe los dias trabajados")
    dias_trabajo = int(input())

    print("Escribe su bono de dias")
    bono_dias = float(input())

    empleado1 = Operador(nombre, id, sueldo_base, dias_trabajo, bono_dias)

    print(empleado1.sueldo_total())

    print("Esbribe su nombre")
    nombre2 = input()

    print("Escribe su id")
    id2 = int(input())

    print("Escribe su sueldo")
    sueldo_base2 = float(input())

    print("Escribe los dias trabajados")
    dias_trabajo2 = int(input())

    print("Escribe su bono de gasolina")
    bono_gasolina = float(input())

    empleado2 = Supervisor(nombre2, id2, sueldo_base2, dias_trabajo2, bono_gasolina)

    print(empleado2.sueldo_total())

except ValueError:
    print("Solo números decimales")
