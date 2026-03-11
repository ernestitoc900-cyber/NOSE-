from entidades.empleado import Empleado

class Operador(Empleado):
    def __init__(self, nombre: str, id: int, sueldo_base: float, 
                 dias_trabajo: int, bono_dias: float):
        super().__init__(nombre, id, sueldo_base, dias_trabajo)
        self.bono_dias = bono_dias

    def sueldo_total(self) -> float:
        if 