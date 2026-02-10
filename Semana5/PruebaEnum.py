from enum import Enum, auto

class EstadoAuto(Enum):
    VERDE = auto()
    AMARILLO = auto()
    ROJO = auto()  

estado = EstadoAuto.VERDE

if estado == EstadoAuto.ROJO:
    print("siga")
else:
    print("nigga")