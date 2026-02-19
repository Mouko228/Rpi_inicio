from enum import Enum, auto 
import RPi.GPIO as GPIO
import time

class Estado(Enum):
    VERDE = auto()
    AMARILLO = auto()
    ROJO = auto() 
    
#pines GPIO
led_pin = 27
servo_pin = 17

#inicializar GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(servo_pin, GPIO.OUT)

#inicializar PWM
pwm_servo = GPIO.PWM(servo_pin, 50)

pwm_servo.start(0)

pwm_led = GPIO.PWM(led_pin, 6)
pwm_led.start(0)

#variables tiempo / contador
inicio = time.time()

estado_previo = None
tiempo_meta = 5

#funciones para el servo
def bajarBarra():
    angle = 90
    duty = (angle/18) + 2.5
    
    pwm_servo.ChangeDutyCycle(duty)
    time.sleep(0.3)
    
    pwm_servo.ChangeDutyCycle(0)
    
def subirBarra():
    angle = 0
    duty = (angle/18) + 2.5
    
    pwm_servo.ChangeDutyCycle(duty)
    time.sleep(0.3)
    
    pwm_servo.ChangeDutyCycle(0)

def prenderLED():
    pwm_led.ChangeDutyCycle(100)

def apagarLED():
    pwm_led.ChangeDutyCycle(0)

def parpadearLED():
    pwm_led.ChangeDutyCycle(50)


try:
    while True: 
        #epoch actual
        actual = time.time()
        
        #tiempo transcurrido desde el inicio
        tiempo_recorrido = actual - inicio

        if (tiempo_recorrido < tiempo_meta):
            estado = Estado.VERDE
        if (tiempo_recorrido > tiempo_meta and tiempo_recorrido <= tiempo_meta + 2):
            estado = Estado.AMARILLO
        if (tiempo_recorrido > tiempo_meta + 2 and tiempo_recorrido <= tiempo_meta + 7):
            estado = Estado.ROJO
        if (tiempo_recorrido > tiempo_meta + 7):
            inicio = time.time()
            
        if (estado != estado_previo):
            estado_previo = estado
            print(estado)
            
            if estado == Estado.VERDE:
                prenderLED()
                subirBarra()
            elif estado == Estado.AMARILLO:
                parpadearLED()
            elif estado == Estado.ROJO:
                apagarLED()
                bajarBarra()
            
        
        
        time.sleep(0.01)
    
except KeyboardInterrupt: 
    print("\ninterrumpido")
    pwm_led.stop()
    pwm_servo.stop()
    GPIO.cleanup()