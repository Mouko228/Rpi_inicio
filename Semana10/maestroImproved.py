import serial
import time
import queue
import threading

PUERTO = '/dev/ttyACM0'
BAUD = 9600

class percentageError(Exception):
    pass

evento = threading.Event()
buzon = queue.Queue()

def input_worker():
    while not evento.is_set():
        try:
            porcentaje = int(input("\nA cuanto porcentaje quieres mover el motor?\nIngresa numero de -100 a 100\n"))
            
            if (porcentaje < -100) or (porcentaje > 100):
                raise percentageError
            
            comando = f"<M1:{porcentaje}>"
            
            buzon.put(comando)
            
        except ValueError:
            print("ingresa un numero valido!")
        
        except percentageError:
            print("ingresa un numero de -100 a 100")
            
def serial_worker():
    while not evento.is_set():
        try: 
            paquete = buzon.get(timeout = 1)
            arduino.write(paquete.encode())
            time.sleep(0.1)
            
            if arduino.in_waiting > 0:
                respuesta = arduino.readline().decode('utf-8').strip()
                print(respuesta)
        
        except queue.Empty:
            pass

try:
    arduino = serial.Serial(PUERTO, BAUD, timeout = 1)
    time.sleep(2)
    print(f"Conectado a {PUERTO}")

    t1 = threading.Thread(target = input_worker, daemon = True)
    t2 = threading.Thread(target = serial_worker, daemon = True)
        
    t1.start()
    t2.start()
    
    while True:
        time.sleep(0.4)
        
except serial.SerialException:
    print("ERROR: No se pudo conectar. Verifica el puerto o los permisos.")

except KeyboardInterrupt: 
    print("\nCerrando conexión...")
    arduino.write(b"<M1:0>")
    
    evento.set()
    t2.join()
    
    if 'arduino' in locals():
        #deja de usar el puerto usb de arduino
        arduino.close()
