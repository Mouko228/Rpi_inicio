import RPi.GPIO as GPIO
import time

led_pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)

#crear objeto PWM
pwm_led = GPIO.PWM(led_pin, 100)


# INICIAR PWM
# pwm.start(duty_cycle_inicial)
pwm_led.start(0)

try:
    while True:
        for brillo in range (0, 101, 5):
            pwm_led.ChangeDutyCycle(brillo)
            time.sleep(0.1)
        
        for brillo in range (100, -1, -5):
            pwm_led.ChangeDutyCycle(brillo)
            time.sleep(0.1)

except KeyboardInterrupt:
    pwm_led.stop()
    GPIO.cleanup()