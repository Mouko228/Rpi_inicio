import RPi.GPIO as GPIO
import time

class Led:
    def __init__(self, pin):
        self.pin = pin
        
        GPIO.setup(self.pin, GPIO.OUT)
        
        self.apagar()
        
    def encender(self):
        GPIO.output(self.pin, GPIO.HIGH)
        print(f"Pin {self.pin} esta encendido")
    
    def apagar(self):
        GPIO.output(self.pin, GPIO.LOW)
        print(f"Pin {self.pin} esta apagado")
        
class Boton:
    def __init__(self,pin):
        self.pin = pin
        
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    def estado(self):
        return GPIO.input(self.pin)
    
    
        