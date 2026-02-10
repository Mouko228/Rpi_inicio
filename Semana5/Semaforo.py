from enum import Enum, auto 
import RPi.GPIO as GPIO
import time

class Estado(Enum):
    VERDE = auto()
    AMARILLO = auto()
    ROJO = auto() 

#inicializacion de pin GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

inicio = time.time()

estado_previo = None
tiempo_meta = 5

try:
    while True: 
        #epoch actual
        actual = time.time()
        
        #tiempo transcurrido desde el inicio
        tiempo_recorrido = actual - inicio
        
        #lectura del boton
        boton_is_pressed = not GPIO.input(17)
        
        if (boton_is_pressed and tiempo_recorrido < tiempo_meta):
            tiempo_meta = tiempo_recorrido
        
        if (tiempo_recorrido < tiempo_meta):
            estado = Estado.VERDE
        if (tiempo_recorrido >= tiempo_meta and tiempo_recorrido <= tiempo_meta + 2):
            estado = Estado.AMARILLO
        if (tiempo_recorrido > tiempo_meta + 2 and tiempo_recorrido <= tiempo_meta + 7):
            estado = Estado.ROJO
        if (tiempo_recorrido > tiempo_meta + 7):
            inicio = time.time()
            tiempo_meta = 5
            
        if (estado != estado_previo):
            estado_previo = estado
            print(estado)
        
        time.sleep(0.01)
    
except KeyboardInterrupt: 
    print("\ninterrumpido")
    GPIO.cleanup()