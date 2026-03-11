from entidades.empleado import Empleado

class Supervisor(Empleado):
    def __init__(self, nombre: str, id: int, sueldo_base: float, 
                 dias_trabajo: int,bono_gasolina: float):
        super().__init__(nombre, id, sueldo_base, dias_trabajo)