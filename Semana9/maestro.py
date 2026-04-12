import serial
import time

PUERTO = '/dev/ttyACM0'
BAUD = 9600

class percentageError(Exception):
    pass

try:
    arduino = serial.Serial(PUERTO, BAUD, timeout = 1)
    time.sleep(2)
    print(f"Conectado a {PUERTO}")
    
    while True:
        try:
            porcentaje = int(input("a cuanto porcentaje quieres mover el motor?\nIngresa numero de -100 a 100"))
            
            if (porcentaje < -100) or (porcentaje > 100):
                raise percentageError
            
            comando = f"<M1:{porcentaje}>"
            
            arduino.write(comando.encode())
            time.sleep(0.1)
            
            if arduino.in_waiting > 0:
                mensaje = arduino.readline().decode('utf-8').strip()
                print(mensaje)
        except ValueError:
            print("ingresa un numero valido!")
        
        except percentageError:
            print("ingresa un numero de -100 a 100")
        
except serial.SerialException:
    print("ERROR: No se pudo conectar. Verifica el puerto o los permisos.")

except KeyboardInterrupt: 
    print("\nCerrando conexión...")
    
    if 'arduino' in locals():
        #deja de usar el puerto usb de arduino
        arduino.close()