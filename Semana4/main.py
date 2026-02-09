import RPi.GPIO as GPIO
import time
from hardware import Led
from hardware import Boton

GPIO.setmode(GPIO.BCM)

try:
    print("Iniciando prueba de boton...")
    
    led = Led(26)
    boton = Boton(17)
    
    while True:
        estado = boton.estado()
        time.sleep(0.1)
        
        if not estado: 
            led.encender()
            print("boton apretado")
        else:
            led.apagar()
            print("boton suelto")
            
    
except KeyboardInterrupt:
    print("\nDetenido por el usuario.")

finally:
    # SIEMPRE limpiar los pines al terminar
    GPIO.cleanup()
    print("GPIO Limpio. Adiós.")