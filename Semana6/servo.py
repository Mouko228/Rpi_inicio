import RPi.GPIO as GPIO
import time

servo_pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

pwm_servo = GPIO.PWM(servo_pin, 50)

pwm_servo.start(0)

def mover_angulo(angle):
    duty = 2.5 + (angle / 18.0)
    
    pwm_servo.ChangeDutyCycle(duty)
    time.sleep(0.7) 

    pwm_servo.ChangeDutyCycle(0) # Deja de empujar para no calentar
    
try:
    print("Moviendo servo...")
    while True:
        print("0 Grados")
        mover_angulo(0)
        time.sleep(1)
        
        print("90 Grados")
        mover_angulo(90)
        time.sleep(1)
        
        print("180 Grados")
        mover_angulo(180)
        time.sleep(1)

except KeyboardInterrupt:
    pwm_servo.stop()
    GPIO.cleanup()
